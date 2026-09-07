#!/usr/bin/env python3
"""Prepare an external BehaviorSpace file. Never edit the native model code."""
import hashlib, json, sys
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT/'protocol.json').read_text())
SOURCE = Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'upstream/base-model.nlogo'
raw = SOURCE.read_bytes()
actual = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert actual == P['source_git_blob_sha1'], f'Native source SHA mismatch: {actual}'
text = raw.decode('utf-8')
assert 'to setup\n' in text and 'to go\n' in text and 'to receiveShare [sharedPiece]' in text
assert 'extensions [r Nw]' in text
assert 'if shouldInquire?' in text and 'if shouldShare?' in text
assert 'ifelse item sharedPiece [agent-evidence-list] of self != "-"' in text
(ROOT/'results').mkdir(exist_ok=True)
metrics = {
 'beliefs': '[agent-belief] of sort turtles',
 'initial_beliefs': '[initial-belief] of sort turtles',
 'heard': '[heard] of sort turtles',
 'recency': '[recency-list] of sort turtles',
 'evidence_holdings': '[agent-evidence-list] of sort turtles',
 'world_evidence': 'evidence-list',
 'world_truth': 'hypothesis-value',
 'optimal_posterior': 'optimal-posterior',
 'mean_belief': 'mean [agent-belief] of turtles',
 'D': 'mean [abs (agent-belief - mean [agent-belief] of turtles)] of turtles',
 'EH': '1 - abs (2 * mean [agent-belief] of turtles - 1)',
 'unique_evidence_receipts_after_initialization': 'sum [length heard - initial-draws] of turtles'
}
root = ET.Element('experiments')
for seed in P['seeds']:
 for arm, chat in P['arms'].items():
  name=f'seed{seed}_{arm}'
  e=ET.SubElement(root,'experiment',name=name,repetitions='1',runMetricsEveryStep='true')
  setup=f'''random-seed {seed}\nset show-me-? false\nsetup\nset curiosity 0\nset chattiness {chat}\nset show-me-? true'''
  ET.SubElement(e,'setup').text=setup
  ET.SubElement(e,'go').text='go'
  ET.SubElement(e,'final').text=f'''export-world "results/{name}_final_world.csv"\nexport-output "results/{name}_native_output.txt"\nr:stop'''
  ET.SubElement(e,'timeLimit',steps=str(P['ticks']))
  for k,v in metrics.items(): ET.SubElement(e,'metric').text=v
  for key,val in P['model_settings'].items():
   vs=ET.SubElement(e,'enumeratedValueSet',variable=key)
   if isinstance(val,bool): value='true' if val else 'false'
   elif isinstance(val,str): value=json.dumps(val)
   else: value=str(val)
   ET.SubElement(vs,'value',value=value)
xml=ET.tostring(root,encoding='unicode')
(ROOT/'experiments.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+xml+'\n')
ET.parse(ROOT/'experiments.xml')
manifest={'source_git_blob_sha1':actual,'source_sha256':hashlib.sha256(raw).hexdigest(),
          'protocol_sha256':hashlib.sha256((ROOT/'protocol.json').read_bytes()).hexdigest(),
          'experiment_names':[e.attrib['name'] for e in root], 'metrics':metrics,
          'native_source_modified':False}
(ROOT/'results/source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
