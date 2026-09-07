from pathlib import Path
import hashlib, json, zipfile
root = Path('source/HUMH.Api/wwwroot')
files = [
 'V3_social.html',
 'content/HUMH_Nucleo_1.9A.md',
 'content/teoria.md',
 'content/experimentos/atencao/v2.0.0/01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md',
 'content/experimentos/atencao/v2.0.0/01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json',
 'content/experimentos/atencao/v2.0.0/02_dependencias/HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md',
 'content/HUMH_VALIDACOES_v1_6_EXPANDIDO.md',
]
manifest = {}
with zipfile.ZipFile('/tmp/humh-v3-source-handoff.zip', 'w', zipfile.ZIP_DEFLATED) as z:
 for name in files:
  data = (root / name).read_bytes()
  manifest[name] = {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
  z.writestr(name, data)
 z.writestr('SOURCE_MANIFEST.json', json.dumps(manifest, indent=2, sort_keys=True) + '\n')
print(json.dumps(manifest, indent=2))
