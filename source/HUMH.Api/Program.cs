// ==================== HUMH v1.0 - EXPERIMENTO FINAL ====================
// Versão: 1.0 (Julho 2026)
// Autor: Luciano Vianna (luciano.vianna@outlook.com)
//
// (resto do cabeçalho igual ao seu)


using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Drawing;
using System.Linq;
using System.Net.Http.Headers;
using System.Reflection;
using System.Text;
using System.Text.Json;


var builder = WebApplication.CreateBuilder(args);

// ==================== C O N F I G  D E  A C E S S O ====================
bool readOnly = builder.Configuration.GetValue("READ_ONLY", false);
string? writeKey = builder.Configuration["API_WRITE_KEY"];

Console.WriteLine($"[HUMH v1.0] READ_ONLY: {readOnly}");
Console.WriteLine($"[HUMH v1.0] API_WRITE_KEY configurado: {!string.IsNullOrWhiteSpace(writeKey)}");

// ==================== C O R S  ====================
var MyAllowSpecificOrigins = "_myAllowSpecificOrigins";
builder.Services.AddCors(options =>
{
    options.AddPolicy(name: MyAllowSpecificOrigins, policy =>
    {
        policy.WithOrigins(
            "http://localhost:5000",
            "http://127.0.0.1:5000",
            "http://127.0.0.1:5500",
            "http://localhost:5500",
            "http://localhost:5107",
            "http://127.0.0.1:5107",
            "https://app.prolific.co",
            "https://app.prolific.com",
            "https://humh-deg8f0a6hzhtgyfu.brazilsouth-01.azurewebsites.net"
        )
        .WithMethods("POST", "GET", "OPTIONS")
        .WithHeaders("Content-Type", "Authorization", "X-API-KEY", "X-Requested-With", "X-HUMH-Version")
        .AllowCredentials();
    });
});

builder.Services.AddRouting();
builder.Services.AddHttpClient();

var app = builder.Build();

app.UseDefaultFiles();
app.UseStaticFiles();
app.UseCors(MyAllowSpecificOrigins);

// ==================== S Q L I T E  P A T H ====================
string ResolveDbPath()
{
    var fromConfig = builder.Configuration["SQLite:DbPath"];
    if (!string.IsNullOrWhiteSpace(fromConfig))
    {
        var dir = Path.GetDirectoryName(fromConfig)!;
        if (!Directory.Exists(dir)) Directory.CreateDirectory(dir);
        return fromConfig;
    }

    var baseDir = app.Environment.ContentRootPath;
    var dbDir = Path.Combine(baseDir, "App_Data");
    Directory.CreateDirectory(dbDir);
    return Path.Combine(dbDir, "humh.sqlite");
}

var connString = builder.Configuration.GetConnectionString("SQLite");
if (string.IsNullOrWhiteSpace(connString))
{
    var dbPath = ResolveDbPath();
    connString = $"Data Source={dbPath};Cache=Shared;Journal Mode=WAL;Foreign Keys=True";
}

Console.WriteLine($"[HUMH v1.0] SQLite => {connString}");

var mem = new Dictionary<string, string?>
{
    ["ConnectionStrings:Resolved:SQLite"] = connString
};
builder.Configuration.AddInMemoryCollection(mem);

// ==================== H E L P E R S  D E  M I G R A T I O N ====================
bool ColumnExists(SQLiteConnection conn, string tableName, string columnName)
{
    using var cmd = conn.CreateCommand();
    cmd.CommandText = $"PRAGMA table_info({tableName})";
    using var reader = cmd.ExecuteReader();
    while (reader.Read())
    {
        var colName = reader.GetString(1);
        if (colName.Equals(columnName, StringComparison.OrdinalIgnoreCase))
            return true;
    }
    return false;
}

void AddColumnIfNotExists(SQLiteConnection conn, string tableName, string columnName, string columnDefinition)
{
    if (!ColumnExists(conn, tableName, columnName))
    {
        using var cmd = conn.CreateCommand();
        cmd.CommandText = $"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnDefinition}";
        cmd.ExecuteNonQuery();
        Console.WriteLine($"[HUMH v1.0] ✅ Coluna '{columnName}' adicionada à tabela '{tableName}'");
    }
    else
    {
        Console.WriteLine($"[HUMH v1.0] ℹ️ Coluna '{columnName}' já existe em '{tableName}'");
    }
}

void EnsureSchema()
{
    using var conn = new SQLiteConnection(connString);
    conn.Open();

    using (var cmd = conn.CreateCommand())
    {
        cmd.CommandText = @"
        PRAGMA journal_mode=WAL;
        
        CREATE TABLE IF NOT EXISTS eh_eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            user_id TEXT NOT NULL,
            ctx TEXT NOT NULL,
            p_est REAL NOT NULL,
            EH REAL NOT NULL,
            cost_ms INTEGER,
            cost_clicks INTEGER,
            seed_public TEXT,
            sig TEXT,
            user_agent TEXT,
            url TEXT
        );
        
        CREATE TABLE IF NOT EXISTS experimento_framing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            prolific_pid TEXT,
            study_id TEXT,
            session_id_prolific TEXT,
            grupo TEXT NOT NULL,
            phase TEXT,
            trial INTEGER NOT NULL,
            p_level REAL NOT NULL,
            nA_shown INTEGER,
            nB_shown INTEGER,
            spatial_seed TEXT,
            choice_a INTEGER,
            correct INTEGER,
            rt_ms INTEGER NOT NULL,
            confidence INTEGER,
            is_attention_check INTEGER NOT NULL,
            is_timeout INTEGER DEFAULT 0,
            spatial_entropy REAL,
            spatial_type TEXT,
            manipulation_check TEXT,
            timestamp TEXT NOT NULL,
            user_agent TEXT,
            UNIQUE(session_id, trial)
        );
            
        CREATE TABLE IF NOT EXISTS sessions_questionnaire (
            session_id TEXT PRIMARY KEY,
            prolific_pid TEXT,
            grupo TEXT,
            technical_issues TEXT,
            comments TEXT,
            timestamp TEXT NOT NULL
        );
        ";
        cmd.ExecuteNonQuery();
        Console.WriteLine("[HUMH v1.0] ✅ Tabelas base criadas/verificadas");
    }

    Console.WriteLine("[HUMH v1.0] 🔄 Verificando migrations...");
    AddColumnIfNotExists(conn, "experimento_framing", "pair_id", "TEXT");
    AddColumnIfNotExists(conn, "experimento_framing", "feedback_shown", "INTEGER");
    AddColumnIfNotExists(conn, "experimento_framing", "keypress_log", "TEXT");
    AddColumnIfNotExists(conn, "experimento_framing", "pair_lag", "INTEGER");

    using (var cmd = conn.CreateCommand())
    {
        cmd.CommandText = @"
            CREATE INDEX IF NOT EXISTS idx_eh_ctx ON eh_eventos(ctx);
            CREATE INDEX IF NOT EXISTS idx_eh_ts  ON eh_eventos(ts);

            CREATE INDEX IF NOT EXISTS idx_exp_session ON experimento_framing(session_id);
            CREATE INDEX IF NOT EXISTS idx_exp_pid ON experimento_framing(prolific_pid);
            CREATE INDEX IF NOT EXISTS idx_exp_grupo ON experimento_framing(grupo);
            CREATE INDEX IF NOT EXISTS idx_exp_phase ON experimento_framing(phase);
            CREATE INDEX IF NOT EXISTS idx_exp_pair ON experimento_framing(pair_id);
            CREATE INDEX IF NOT EXISTS idx_exp_timestamp ON experimento_framing(timestamp);

            CREATE INDEX IF NOT EXISTS idx_quest_pid ON sessions_questionnaire(prolific_pid);
        ";
        cmd.ExecuteNonQuery();
        Console.WriteLine("[HUMH v1.0] ✅ Índices criados/verificados");
    }

    Console.WriteLine("[HUMH v1.0] ✅ Schema completo verificado e atualizado");
}

EnsureSchema();


// ==================== E N D P O I N T S ====================
var api = app.MapGroup("/api");

// HEALTH
api.MapGet("/health", () =>
{
    try
    {
        using var conn = new SQLiteConnection(connString);
        conn.Open();
        return Results.Ok(new
        {
            status = "healthy",
            timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds(),
            version = "1.0"
        });
    }
    catch (Exception ex)
    {
        Console.WriteLine("[HUMH v1.0] ❌ Health check falhou: " + ex.Message);
        return Results.Problem(title: "Unhealthy", detail: ex.Message, statusCode: 503);
    }
});

api.MapGet("/data/all", () =>
{
    try
    {
        using var conn = new SQLiteConnection(connString);
        conn.Open();
        using var cmd = conn.CreateCommand();
        cmd.CommandText = "SELECT * FROM experimento_framing ORDER BY timestamp DESC LIMIT 1000";
        using var reader = cmd.ExecuteReader();

        var list = new List<Dictionary<string, object?>>();
        while (reader.Read())
        {
            var row = new Dictionary<string, object?>();
            for (int i = 0; i < reader.FieldCount; i++)
                row[reader.GetName(i)] = reader.IsDBNull(i) ? null : reader.GetValue(i);
            list.Add(row);
        }
        return Results.Ok(new { count = list.Count, data = list });
    }
    catch (Exception ex)
    {
        Console.WriteLine("[HUMH v1.0] Erro em /data/all: " + ex);
        return Results.Problem(title: "Erro ao buscar dados", detail: ex.Message, statusCode: 500);
    }
});


// ==================== /api/lunarcrush ====================
app.MapGet("/api/lunarcrush", async (IHttpClientFactory http, IConfiguration cfg) =>
{
    using var httpClient = http.CreateClient();

    try
    {
        var apiKey = cfg["lunarcrush:ApiKey"]; // ou "lunarcrush:Password", como você preferir

        if (string.IsNullOrWhiteSpace(apiKey))
        {
            return Results.Json(new
            {
                valor = -1.0,
                erro = "API key do LunarCrush não configurada (lunarcrush:ApiKey)."
            });
        }

        var url = "https://lunarcrush.com/api4/public/coins/list/v1";

        //Console.WriteLine($"[LunarCrush] URL: {url}");

        using var request = new HttpRequestMessage(HttpMethod.Get, url);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);
        request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

        using var response = await httpClient.SendAsync(request);

        var body = await response.Content.ReadAsStringAsync();

        if (!response.IsSuccessStatusCode)
        {
            // Console.WriteLine($"[LunarCrush] HTTP {(int)response.StatusCode}: {body}");
            return Results.Json(new
            {
                valor = -1.0,
                erro = $"LunarCrush retornou HTTP {(int)response.StatusCode} ({response.StatusCode})"
            });
        }

        // Console.WriteLine($"[LunarCrush] Response (500 chars): {body.Substring(0, Math.Min(500, body.Length))}");

        using var doc = JsonDocument.Parse(body);
        var root = doc.RootElement;

        // Estrutura típica: { "config": {...}, "data": [ {...}, {...} ] , ... }
        var data = root.GetProperty("data");

        if (data.ValueKind != JsonValueKind.Array)
        {
            return Results.Json(new
            {
                valor = -1.0,
                erro = "Formato inesperado: 'data' não é array."
            });
        }

        var btc = data.EnumerateArray()
                      .FirstOrDefault(e =>
                          e.TryGetProperty("symbol", out var sym) &&
                          string.Equals(sym.GetString(), "BTC", StringComparison.OrdinalIgnoreCase));

        if (btc.ValueKind == JsonValueKind.Undefined)
        {
            return Results.Json(new
            {
                valor = -1.0,
                erro = "BTC não encontrado na resposta do LunarCrush."
            });
        }

        // 🔎 Ajuste ESTE nome de campo depois de olhar o log completo
        // Alguns exemplos possíveis: "average_sentiment", "galaxy_score", etc.
        double sentimento;

        if (btc.TryGetProperty("galaxy_score", out var sProp) &&
            sProp.ValueKind == JsonValueKind.Number)
        {
            sentimento = sProp.GetDouble();
        }
        else
        {
            return Results.Json(new
            {
                valor = -1.0,
                erro = "Campo de sentimento não encontrado em BTC (verifique o JSON no console)."
            });
        }

        return Results.Json(new { valor = sentimento });
    }
    catch (Exception ex)
    {
        Console.WriteLine($"[LunarCrush] ERRO: {ex}");
        return Results.Json(new
        {
            valor = -1.0,
            erro = ex.Message
        });
    }
});

app.MapGet("/api/trends", async (IHttpClientFactory http, IConfiguration cfg) =>
{
    // 1) Credenciais (appsettings.json ou variáveis de ambiente)
    var login = cfg["DataForSEO:Login"];
    var password = cfg["DataForSEO:Password"];
    if (string.IsNullOrWhiteSpace(login) || string.IsNullOrWhiteSpace(password))
        return Results.Problem("Credenciais do DataForSEO ausentes", statusCode: 500);

    // 2) Client com Basic Auth
    var client = http.CreateClient();
    var authBytes = Encoding.UTF8.GetBytes($"{login}:{password}");
    client.DefaultRequestHeaders.Authorization =
        new AuthenticationHeaderValue("Basic", Convert.ToBase64String(authBytes));

    // 3) Payload: "btc" global; peça explicitamente o gráfico
    // Use "past_day" para capturar o ponto mais recente (muda ao longo do dia).
    // Se preferir janela ainda menor e suportada na sua conta, troque para "past_4_hours".
    var payload = new[]
    {
        new
        {
            keywords = new[] { "btc" },
            time_range = "past_day",
            item_types = new[] { "google_trends_graph" }
        }
    };

    using var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

    // 4) Live endpoint (resposta em segundos)
    var resp = await client.PostAsync("https://api.dataforseo.com/v3/keywords_data/google_trends/explore/live", content);
    if (!resp.IsSuccessStatusCode)
    {
        var errTxt = await resp.Content.ReadAsStringAsync();
        Console.WriteLine("[DataForSEO] HTTP " + (int)resp.StatusCode + " - " + errTxt);
        return Results.Problem("Falha ao consultar DataForSEO (HTTP)", statusCode: 502);
    }

    using var doc = await JsonDocument.ParseAsync(await resp.Content.ReadAsStreamAsync());
    var root = doc.RootElement;

    // 5) Validar envelope e achar o item do gráfico
    if (!root.TryGetProperty("tasks", out var tasks) || tasks.GetArrayLength() == 0)
        return Results.Problem("Resposta inesperada do DataForSEO (sem tasks)", statusCode: 502);

    var task0 = tasks[0];
    var statusCode = task0.GetProperty("status_code").GetInt32();
    if (statusCode != 20000)
    {
        var msg = task0.TryGetProperty("status_message", out var sm) ? sm.GetString() : "erro";
        return Results.Problem($"DataForSEO status {statusCode}: {msg}", statusCode: 502);
    }

    var result0 = task0.GetProperty("result")[0];
    var items = result0.GetProperty("items");

    JsonElement? graph = null;
    foreach (var it in items.EnumerateArray())
        if (it.TryGetProperty("type", out var t) && string.Equals(t.GetString(), "google_trends_graph", StringComparison.OrdinalIgnoreCase))
        { graph = it; break; }

    if (graph is null)
        return Results.Problem("Item 'google_trends_graph' não encontrado", statusCode: 502);

    var dataArray = graph.Value.GetProperty("data");
    if (dataArray.GetArrayLength() == 0)
        return Results.Problem("Gráfico sem pontos de dados", statusCode: 502);

    // 6) Último ponto da série (valor 0–100)
    var last = dataArray[dataArray.GetArrayLength() - 1];

    int popularity;
    if (last.TryGetProperty("values", out var vEl))
        popularity = vEl.ValueKind == JsonValueKind.Array ? vEl[0].GetInt32() : vEl.GetInt32();
    else if (last.TryGetProperty("value", out var vEl2))
        popularity = vEl2.GetInt32();
    else
        popularity = 0;

    // timestamp opcional, se existir
    string? ts = null;
    if (last.TryGetProperty("time", out var t1) && t1.ValueKind == JsonValueKind.String) ts = t1.GetString();
    else if (last.TryGetProperty("date", out var t2) && t2.ValueKind == JsonValueKind.String) ts = t2.GetString();

    return Results.Json(new { termo = "btc", popularidade = popularity, ts });
});


// ==================== /api/feargreed ====================
app.MapGet("/api/feargreed", async () =>
{
    using var httpClient = new HttpClient();
    try
    {
        var response = await httpClient.GetStringAsync("https://api.alternative.me/fng/?limit=1");
        using var doc = JsonDocument.Parse(response);
        var root = doc.RootElement;
        var data = root.GetProperty("data")[0];
        var valor = data.GetProperty("value").GetString();
        var classificacao = data.GetProperty("value_classification").GetString();

        return Results.Json(new
        {
            valor,
            classificacao
        });
    }
    catch
    {
        return Results.Json(new
        {
            valor = -1,
            classificacao = "erro"
        });
    }
});

// ===== CHECK: Prolific duplicate participation =====
api.MapGet("/check/prolific", (string pid) =>
{
    try
    {
        using var conn = new SQLiteConnection(connString);
        conn.Open();
        using var cmd = conn.CreateCommand();
        cmd.CommandText = @"
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN phase='main' THEN 1 ELSE 0 END) as total_main,
                COUNT(DISTINCT session_id) as sessions,
                MAX(timestamp) as last_ts
            FROM experimento_framing
            WHERE prolific_pid = @pid
        ";
        cmd.Parameters.AddWithValue("@pid", pid);
        using var rd = cmd.ExecuteReader();
        int total = 0, total_main = 0, sessions = 0;
        string? last_ts = null;
        if (rd.Read())
        {
            total = rd.IsDBNull(0) ? 0 : rd.GetInt32(0);
            total_main = rd.IsDBNull(1) ? 0 : rd.GetInt32(1);
            sessions = rd.IsDBNull(2) ? 0 : rd.GetInt32(2);
            last_ts = rd.IsDBNull(3) ? null : rd.GetString(3);
        }
        var exists = total > 0;
        var eligible = !exists;
        return Results.Ok(new { exists, eligible, total, total_main, sessions, last_ts });
    }
    catch (Exception ex)
    {
        return Results.Problem(ex.Message);
    }
});

api.MapGet("/export/csv", () =>
{
    try
    {
        using var conn = new SQLiteConnection(connString);
        conn.Open();
        using var cmd = conn.CreateCommand();
        cmd.CommandText = "SELECT * FROM experimento_framing ORDER BY session_id, trial";
        using var reader = cmd.ExecuteReader();

        var csv = new System.Text.StringBuilder();

        var headers = new List<string>();
        for (int i = 0; i < reader.FieldCount; i++)
            headers.Add(reader.GetName(i));
        csv.AppendLine(string.Join(",", headers));

        while (reader.Read())
        {
            var values = new List<string>();
            for (int i = 0; i < reader.FieldCount; i++)
            {
                var val = reader.IsDBNull(i) ? "" : reader.GetValue(i).ToString();
                if (val != null && (val.Contains(",") || val.Contains("\"") || val.Contains("\n")))
                    val = "\"" + val.Replace("\"", "\"\"") + "\"";
                values.Add(val ?? "");
            }
            csv.AppendLine(string.Join(",", values));
        }

        return Results.Text(csv.ToString(), "text/csv");
    }
    catch (Exception ex)
    {
        Console.WriteLine("[HUMH v1.0] Erro em /export/csv: " + ex);
        return Results.Problem(title: "Erro ao exportar CSV", detail: ex.Message, statusCode: 500);
    }
});

// ==================== E N D P O I N T S  D E  E S C R I T A ====================
if (!readOnly)
{
    var write = api.MapGroup("/write");

    Console.WriteLine("[HUMH v1.0] Write endpoints habilitados em /api/write/");

    write.MapPost("/experimento", async (HttpRequest req) =>
    {
        try
        {
            using var doc = await System.Text.Json.JsonDocument.ParseAsync(req.Body);
            var root = doc.RootElement;

            var sessionId = root.GetProperty("session_id").GetString()!;
            var prolificPid = root.TryGetProperty("prolific_pid", out var pp) ? pp.GetString() : null;
            var studyId = root.TryGetProperty("study_id", out var si) ? si.GetString() : null;
            var sessionProlific = root.TryGetProperty("session_id_prolific", out var sp) ? sp.GetString() : null;

            var grupo = root.GetProperty("group").GetString()!;
	    if (grupo != "FV" && grupo != "SF") return Results.BadRequest(new { ok = false, error = $"Grupo inválido: '{grupo}'. Esperado FV ou SF." });

            var trials = root.GetProperty("trials").EnumerateArray();
            var clientVersion = req.Headers.TryGetValue("X-HUMH-Version", out var __ver) ? __ver.ToString() : null;

            var userAgent = req.Headers.UserAgent.ToString().ToLowerInvariant();
            var mobileKeywords = new[] { "android", "iphone", "ipad", "mobile", "webos", "blackberry" };

            if (mobileKeywords.Any(k => userAgent.Contains(k)))
            {
                Console.WriteLine($"[HUMH v1.0] ⚠️ AVISO: Mobile detectado - {userAgent}");
                Console.WriteLine($"[HUMH v1.0] Session: {sessionId} | Prolific: {prolificPid}");
            }

            using var conn = new SQLiteConnection(connString);
            await conn.OpenAsync();
            using var tx = conn.BeginTransaction();

            int inserted = 0;
            foreach (var trial in trials)
            {
                using var cmd = conn.CreateCommand();
                cmd.Transaction = tx;
                cmd.CommandText = @"
                    INSERT OR REPLACE INTO experimento_framing 
                    (session_id, prolific_pid, study_id, session_id_prolific, 
                     grupo, phase, trial, p_level, nA_shown, nB_shown, spatial_seed, pair_id, pair_lag,
                     choice_a, correct, rt_ms, confidence, 
                     is_attention_check, is_timeout, feedback_shown, keypress_log,
                     timestamp, manipulation_check, spatial_entropy, spatial_type, user_agent)
                    VALUES 
                    (@session, @prolific_pid, @study_id, @session_prolific,
                     @grupo, @phase, @trial, @p_level, @nA, @nB, @spatial_seed, @pair_id, @pair_lag,
                     @choice_a, @correct, @rt_ms, @confidence,
                     @attention, @timeout, @feedback_shown, @keypress_log,
                     @timestamp, @manip_check, @spatial_entropy, @spatial_type, @ua)
                ";

                cmd.Parameters.AddWithValue("@session", sessionId);
                cmd.Parameters.AddWithValue("@prolific_pid", (object?)prolificPid ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@study_id", (object?)studyId ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@session_prolific", (object?)sessionProlific ?? DBNull.Value);
                cmd.Parameters.AddWithValue("@grupo", grupo);
                cmd.Parameters.AddWithValue("@phase", trial.TryGetProperty("phase", out var ph) ? (object?)(ph.ValueKind == JsonValueKind.String ? ph.GetString() : null) ?? DBNull.Value : DBNull.Value);
                cmd.Parameters.AddWithValue("@trial", trial.GetProperty("trial").GetInt32());
                cmd.Parameters.AddWithValue("@p_level", trial.GetProperty("p_level").GetDouble());
                cmd.Parameters.AddWithValue("@nA", trial.TryGetProperty("nA_shown", out var nA) ? (object?)nA.GetInt32() : DBNull.Value);
                cmd.Parameters.AddWithValue("@nB", trial.TryGetProperty("nB_shown", out var nB) ? (object?)nB.GetInt32() : DBNull.Value);
                cmd.Parameters.AddWithValue("@spatial_seed", trial.TryGetProperty("spatial_seed", out var ss) ? (object?)(ss.ValueKind == JsonValueKind.String ? ss.GetString() : ss.GetInt32().ToString()) ?? DBNull.Value : DBNull.Value);
                cmd.Parameters.AddWithValue("@pair_id", trial.TryGetProperty("pair_id", out var pid) && pid.ValueKind == JsonValueKind.String ? (object?)pid.GetString() : DBNull.Value);
                cmd.Parameters.AddWithValue("@pair_lag", trial.TryGetProperty("pair_lag", out var plag) && plag.ValueKind == JsonValueKind.Number ? (object?)plag.GetInt32() : DBNull.Value);

                if (trial.TryGetProperty("choice_a", out var ca) && ca.ValueKind != JsonValueKind.Null)
                    cmd.Parameters.AddWithValue("@choice_a", ca.GetBoolean() ? 1 : 0);
                else
                    cmd.Parameters.AddWithValue("@choice_a", DBNull.Value);

                if (trial.TryGetProperty("correct", out var cor) && cor.ValueKind != JsonValueKind.Null)
                    cmd.Parameters.AddWithValue("@correct", cor.GetBoolean() ? 1 : 0);
                else
                    cmd.Parameters.AddWithValue("@correct", DBNull.Value);

                cmd.Parameters.AddWithValue("@rt_ms", trial.GetProperty("rt_ms").GetInt32());
                if (trial.TryGetProperty("confidence", out var conf) && conf.ValueKind != JsonValueKind.Null)
                    cmd.Parameters.AddWithValue("@confidence", conf.GetInt32());
                else
                    cmd.Parameters.AddWithValue("@confidence", DBNull.Value);

                cmd.Parameters.AddWithValue("@attention", trial.GetProperty("is_attention_check").GetBoolean() ? 1 : 0);
                cmd.Parameters.AddWithValue("@timeout", trial.TryGetProperty("is_timeout", out var to) && to.GetBoolean() ? 1 : 0);
                cmd.Parameters.AddWithValue("@feedback_shown", trial.TryGetProperty("feedback_shown", out var fb) && fb.GetBoolean() ? 1 : 0);

                if (trial.TryGetProperty("keypress_log", out var kl))
                    cmd.Parameters.AddWithValue("@keypress_log", (object?)kl.GetString() ?? DBNull.Value);
                else if (trial.TryGetProperty("keylog", out kl))
                    cmd.Parameters.AddWithValue("@keypress_log", (object?)kl.GetString() ?? DBNull.Value);
                else
                    cmd.Parameters.AddWithValue("@keypress_log", DBNull.Value);

                cmd.Parameters.AddWithValue("@timestamp", trial.GetProperty("timestamp").GetString()!);
                cmd.Parameters.AddWithValue("@spatial_entropy", trial.TryGetProperty("spatial_entropy", out var se) ? (object?)se.GetDouble() : DBNull.Value);
                cmd.Parameters.AddWithValue("@spatial_type", trial.TryGetProperty("spatial_type", out var st) ? (object?)(st.ValueKind == JsonValueKind.String ? st.GetString() : null) ?? DBNull.Value : DBNull.Value);
                cmd.Parameters.AddWithValue("@manip_check", trial.TryGetProperty("manipulation_check", out var mc) ? (object?)mc.GetString() ?? DBNull.Value : DBNull.Value);
                cmd.Parameters.AddWithValue("@ua", req.Headers.UserAgent.ToString());

                inserted += await cmd.ExecuteNonQueryAsync();
            }

            await tx.CommitAsync();

            Console.WriteLine($"[HUMH v1.0] ✅ Experimento salvo: {inserted} trials | Session: {sessionId} | Prolific: {prolificPid ?? "N/A"} | Grupo: {grupo}");

            return Results.Ok(new
            {
                ok = true,
                inserted,
                session_id = sessionId,
                prolific_pid = prolificPid,
                grupo = grupo,
                client_version = clientVersion
            });
        }
        catch (Exception ex)
        {
            Console.WriteLine("[HUMH v1.0] ❌ Erro ao salvar experimento: " + ex);
            return Results.Problem(title: "Falha ao salvar experimento", detail: ex.Message, statusCode: 500);
        }
    });

    write.MapGet("/test", () =>
    {
        return Results.Ok(new { ok = true, msg = "Write OK", ts = DateTimeOffset.UtcNow, version = "1.0" });
    });
}
else
{
    Console.WriteLine("[HUMH v1.0] Write endpoints DESABILITADOS");
}

Console.WriteLine("[HUMH v1.0] Servidor iniciando...");

app.Run();
