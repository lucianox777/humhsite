# HUMH — Guia de Instalação

Aplicação **ASP.NET Core (.NET 8)**, self-host (Kestrel), front em `wwwroot/` e **SQLite** em `App_Data/`.  
Publicação **manual** via **Visual Studio 2022** para **Azure App Service (Free F1)**.

## 1) Pré-requisitos

- **.NET SDK 8.x**  
- **Visual Studio 2022** (ASP.NET e desenvolvimento web)  
- **Git** (opcional, mas recomendado)

## 2) Estrutura do repositório

```
HUMH.sln
src/
  HUMH.Api/
    HUMH.Api.csproj
    wwwroot/
    App_Data/            # humh.db (não versionar)
README.md
```

## 3) Instalação local (DEV)

1. **Clonar / baixar código**
   ```bash
   git clone https://github.com/<usuario-ou-org>/humhsite.git
   cd humhsite
   ```

2. **Restaurar e executar**
   ```bash
   dotnet restore
   dotnet run --project src/HUMH.Api
   ```
   Acesse: `http://localhost:8080` (ou a porta do `launchSettings.json`).

3. **(Opcional) Configuração local de segredos**  
   Crie o arquivo **`src/HUMH.Api/secrets.local.json`** (este arquivo é **ignorado** pelo Git e **não é publicado**):
   ```json
   {
     "READ_ONLY": false,
     "API_WRITE_KEY": "LOCAL-GUID-EXEMPLO-2f9f2e4a-7d1a-4aa3-9a0c-1234567890ab",
     "SQLite": { "DbPath": "C:\\temp\\humh-local.db" },
     "Mail": {
       "Host": "smtp.exemplo.net",
       "User": "no-reply@exemplo.net",
       "Password": "SENHA-APENAS-LOCAL"
     }
   }
   ```
   > Se não criar esse arquivo, o app usa o **SQLite padrão** em `App_Data/humh.db` e `READ_ONLY=true` por default.

4. **E-mail de contato (frontend)**  
   No HTML (ex.: `wwwroot/index.html`), mantenha apenas:
   ```html
   <a href="mailto:contato@exemplo.net">contato@exemplo.net</a>
   ```

## 4) Banco de dados (SQLite)

- **Produção (Azure)**: o app resolve automaticamente o caminho  
  `/home/site/wwwroot/App_Data/humh.db` (equivale a `App_Data/humh.db` no projeto).
- **WAL** está habilitado e o **schema é criado** na inicialização, se necessário.
- **Não** versionar `App_Data/*.db*`.

## 5) Publicação no Azure (manual, sem CI)

1. **Criar o App Service** (Linux, .NET 8, plano **Free F1**).  
2. **Publicar pelo VS2022**  
   - Projeto **HUMH.Api** → **Publish** → Azure App Service (Linux) → **Publish**.  
   - Em **Settings** do perfil: **desmarque** *Remove additional files at destination* (preserva `App_Data`).
3. **Configurações no App Service**  
   - *Configuration → General settings* → **HTTPS Only = On**.  
   - *Configuration → Application settings*:
     - `READ_ONLY = true` (produção somente leitura)  
     - (Opcional) `API_WRITE_KEY = GUID` *(apenas se um dia habilitar escrita)*
4. **Pings (reduzir hibernação no Free F1)**  
   - Configure seu monitor (ex.: Uptime) para chamar `GET /api/health` a cada **5–10 min**.

## 6) Pós-instalação (checagem rápida)

- Acessar a URL do App Service: `https://<seuapp>.azurewebsites.net/`  
- `GET /api/health` deve retornar `{ ok: true, ... }`  
- `GET /api/eh/events` e `GET /api/eh/stats` respondem normalmente.  
- Nenhuma rota de **escrita** aparece em produção (`READ_ONLY=true`).

## 7) Atualizações futuras

- **Sempre manuais** pelo **VS2022 → Publish**.  
- Para **arquivos estáticos** (HTML/CSS/JS/imagens), é possível substituir **apenas o arquivo** via **Kudu/FTPS** (sem ZIP).  
- Evite sobrescrever `App_Data/` (mantenha *Remove additional files* **desmarcado**).

## 8) Boas práticas de segurança

- **Segredos no DEV**: `secrets.local.json` (ignorado pelo Git).  
- **Segredos no PROD**: *Application settings* do App Service (variáveis de ambiente).  
- **Nunca** commitar `*.PublishSettings`, perfis de publish, senhas ou o `.db`.

## 9) `.gitignore` (resumo recomendado)

```
bin/ obj/ .vs/ publish/
**/Properties/PublishProfiles/*.pubxml
*.PublishSettings
**/App_Data/*.db*
**/secrets.local.json
.env
*.pfx
*.log
*.tmp
```

---

Dúvidas: abra uma issue ou entre em contato por e-mail (`mailto:contato@exemplo.net`).

## Refatoração 2025-09-23
- Endpoints `/api/write/ingest` e `/api/write/test` agora são anônimos (sem `X-API-KEY`).
- A chave `API_WRITE_KEY` é usada apenas no servidor para habilitar/ocultar os endpoints.
- Lógica de escrita extraída para `Services/EventoService.cs`.
- `/api/health` agora exibe o caminho real do arquivo SQLite (Data Source).
- Comentários adicionados em `Program.cs` explicando decisões de segurança.
