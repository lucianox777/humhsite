from pathlib import Path
import hashlib, json

root = Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v = root/'v2.0.0'
specp = v/'01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep = v/'01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
lockp = v/'02_dependencias/DEPENDENCIES.lock.json'
rootsha = v/'HUMH_A0_A1_v2.0.0.sha256'
sumsp = v/'03_integridade/SHA256SUMS.txt'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

spec = specp.read_text(encoding='utf-8')
a = spec.index('## 5.1.13. Parâmetros numéricos pendentes')
b = spec.index('## 5.1.14. Barreira síncrona do ciclo lógico', a)
new = '''## 5.1.13. Parâmetros numéricos pendentes\n\nA semântica e o regime de isolamento já estão congelados. Antes do run ainda devem ser congelados:\n\n```text\nbasal_eta0_bound_admissibility\nobserver_buffer_capacity_value\nrequired_work_rule\nrequired_work_range_or_distribution\nobserver_opportunity_arm_rules\nABENCH0_opportunity_candidate_rules\nL_A\nW\nnumber_of_arms\ninstrumental_contrast_criteria\nsaturation_avoidance_criteria\n```\n\nStatus:\n\n```text\nATTENTION_INSTRUMENT_SEMANTICS = FROZEN\nOBSERVER_PROCESSING_CAPACITY_SEMANTICS = FROZEN_AUXILIARY\nOBSERVER_BUFFER_HETEROGENEITY_REGIME = HOMOGENEOUS_FROZEN_FOR_FIRST_A1\nATTENTION_INSTRUMENT_ALGORITHM = FROZEN_OPPORTUNITY_ALLOCATION\nATTENTION_INSTRUMENT_NUMERICS = UNFROZEN_REQUIRED_BEFORE_RUN\n```\n\n'''
spec = spec[:a] + new + spec[b:]

# Consistency assertions on current normative state.
assert 'OBSERVER_BUFFER_HETEROGENEITY_REGIME = UNFROZEN_REQUIRED_BEFORE_RUN' not in spec
assert 'observer_microdynamic_contract' not in spec
assert '2.0.1_RUN_READY' not in spec
assert 'ATTENTION_INSTRUMENT = FROZEN_LOGICAL_WORK_BUDGET' not in spec
assert 'ADIST0.DERIVATIONAL_CONTENT_AUDIT_STRUCTURAL' in spec
assert 'SYNCHRONOUS_SNAPSHOT_BARRIER' in spec

specp.write_text(spec, encoding='utf-8')

lock = json.loads(lockp.read_text(encoding='utf-8'))
for item in lock.get('normative_artifacts', []):
    if item['path'].endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'):
        item['sha256'] = sha(specp)
    if item['path'].endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'):
        item['sha256'] = sha(tracep)
lockp.write_text(json.dumps(lock, ensure_ascii=False, indent=2), encoding='utf-8')

rootsha.write_text(f'{sha(specp)}  {specp.name}\n{sha(tracep)}  {tracep.name}\n', encoding='utf-8')
files = sorted(p for p in v.rglob('*') if p.is_file() and p != sumsp)
sumsp.write_text('\n'.join(f'{sha(p)}  {p.relative_to(v).as_posix()}' for p in files)+'\n', encoding='utf-8')
print('SPEC_SHA256', sha(specp))
print('TRACE_SHA256', sha(tracep))
