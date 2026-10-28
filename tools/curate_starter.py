"""One-time editorial curation of the user's 26.5 notes, deliberately excludes later features.
Run only with --notes path. Review output against target version, then commit seed JSON.
"""
import argparse,json,re,pathlib
p=argparse.ArgumentParser();p.add_argument('--notes',required=True);p.add_argument('--out',default='data');args=p.parse_args()
text=pathlib.Path(args.notes).read_text(encoding='utf-8')
lines=text.splitlines()
# Shortcut section (Windows column only): version-gated and context-qualified.
shortcuts=[]; chapter=''; section=''; exclude_section=False
for line in lines:
 if line.startswith('# 03 —'):
  chapter='shortcuts';continue
 if line.startswith('# 04 —'):chapter='';continue
 if chapter!='shortcuts':continue
 if line.startswith('## '):
  section=line[3:].strip();exclude_section= ('2026' in section or '26.' in section or '3.13' in section or '3.14' in section);continue
 if line.startswith('### '):
  sub=line[4:].strip();exclude_section=('26.' in sub or '2026' in sub or 'Proportional Scrubbing' in sub or 'Conflicts' in sub)
  continue
 if exclude_section:continue
 if not (line.startswith('| ') and line.count('|')>=4):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if not cells or any(c.startswith('---') for c in cells) or cells[0].lower() in ('action','task','task and required context','tool/action','need to...','result','show only...','modify/action','to...','show only...','in graph editor','during a guide drag','goal at the playhead','windows','i need to…'):continue
 if section.startswith('3.'):category=section.split(' ',1)[-1]
 else:continue
 if len(cells)<2:continue
 action,key=cells[0],cells[1]
 if not key or key.lower() in ('go to','use','what it shows','clarification','windows shortcut','windows','meaning depends on context'):continue
 full=' '.join(cells)
 if any(w in full.lower() for w in ['26.0','26.2','26.3','26.5','2026','object matte','curl noise','quick apply','clipboard (','ctrl+enter','ctrl+alt+shift+f5','ctrl+w` locally','`ctrl+w`','proportional scrubbing','shift+[`','shift+]`','alt+shift+[`','alt+shift+]`','advanced 3d depth of field','color labels for effects']):continue
 if len(key)>115: continue
 detail='; '.join(cells[2:])
 shortcuts.append({'id':'key-'+str(len(shortcuts)+1).zfill(3),'category':category,'action':re.sub(r'\*\*','',action),'key':re.sub(r'\*\*','',key),'detail':re.sub(r'\*\*','',detail),'source':'shortcuts','verification':'Check installed 25.6 shortcut editor; focus, selection and custom presets matter.'})
# Deduplicate by key+action, collapse string conflicts only if identical.
unique=[]; seen=set()
for s in shortcuts:
 k=(s['category'],s['action'],s['key'])
 if k in seen:continue
 seen.add(k);unique.append(s)
for i,s in enumerate(unique,1):s['id']=f'key-{i:03}'

# Effects pages: parse two-column names/description from user supplied rough inventory, filter all 26.x additions.
effects=[];on=False;section=''
category_map={'5.3':'Blur & Sharpen','5.4':'Channel & Matte','5.5':'Keying','5.6':'Color Correction','5.7':'Distort & Transform','5.8':'Generate','5.9':'Noise & Grain','5.10':'Simulation','5.11':'Stylize, Time & Transition','5.12':'Perspective, 3D & Utility','5.13':'Audio','5.14':'Legacy & Compatibility'}
for line in lines:
 if line.startswith('## 5.'):
  section=line[3:].split(' ',1)[0];on=section in category_map;continue
 if line.startswith('# 06 —'):break
 if not on or not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=2 or cells[0].startswith('---') or cells[0].lower() in ['effect','use','when to use','what it does / choose it for','best use','typical appearance','name','effect name','when i...','task','category','i want to...','start with','type','purpose']:continue
 effect=re.sub(r'\*\*|`','',cells[0]).strip()
 desc=re.sub(r'\*\*','',cells[1]).strip()
 if len(effect)>75 or len(effect)<2:continue
 if any(s in (effect+' '+desc).lower() for s in ['26.0','26.2','26.3','26.5','new 26','curl noise','unmult','compositor (2026)','object matte','quick apply','new:','new —','new**']):continue
 if effect.startswith('|') or '|' in effect or effect.lower() in ['effect','use case','what it does','when to use','effect / use','alternative / problem']:continue
 if any(x in effect.lower() for x in ['\u2192',' / ', ' + ',' vs ', ' 2026']):
  # A few combined rows are not distinct native effect names.
  continue
 if section=='5.14':
  # Section 5.14 contains category clarifications, not primarily native effects.
  continue
 effects.append({'id':f'fx-{len(effects)+1:03}','name':effect,'category':category_map[section], 'summary':desc,'level':'Reference','version':'Available by 25.6 (review installed effect list)','source':'effects'})
# unique titles
seen=set();fx=[]
for item in effects:
 n=item['name'].lower()
 if n not in seen:seen.add(n);fx.append(item)
for i,s in enumerate(fx,1):s['id']=f'fx-{i:03}'
print('shortcuts',len(unique),'effects',len(fx))
print('effect categories', {c:sum(e['category']==c for e in fx) for c in category_map.values()})
print('last few', [x['name'] for x in fx[-25:]])
out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
(out/'shortcuts_seed.json').write_text(json.dumps(unique,indent=2,ensure_ascii=False),encoding='utf-8')
(out/'effects_seed.json').write_text(json.dumps(fx,indent=2,ensure_ascii=False),encoding='utf-8')
# Troubleshooting table from supplied note, excluding newer tool-only features.
troubles=[];in_section=False
for line in lines:
 if line.startswith('## 7.2 '):in_section=True;continue
 if in_section and line.startswith('## '):break
 if in_section and line.startswith('| ') and line.count('|')>=4:
  parts=[v.strip().replace('**','') for v in line.strip().strip('|').split('|')]
  if len(parts)<3 or parts[0].startswith('---') or parts[0]=='Symptom':continue
  if any(x in parts[0].lower() for x in ['object matte']):continue
  if any(x in ' '.join(parts).lower() for x in ['quick apply','26.2','26.3','26.5','2026','object matte']):continue
  troubles.append({'id':'trouble-'+str(len(troubles)+1).zfill(3),'symptom':parts[0],'checks':parts[1],'fix':parts[2]})
# Glossary table, excluding specifically 26.x features.
gloss=[];in_section=False
for line in lines:
 if line.startswith('## 11.1 '):in_section=True;continue
 if in_section and line.startswith('## '):break
 if in_section and line.startswith('| ') and line.count('|')>=3:
  parts=[v.strip().replace('**','') for v in line.strip().strip('|').split('|')]
  if len(parts)!=2 or parts[0].startswith('---') or parts[0]=='Term':continue
  if 'quick apply' in parts[0].lower() or any(t in ' '.join(parts).lower() for t in ['26.2','26.3','26.5']):continue
  gloss.append({'term':parts[0],'definition':parts[1]})
(out/'troubleshooting_seed.json').write_text(json.dumps(troubles,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'glossary_seed.json').write_text(json.dumps(gloss,ensure_ascii=False,indent=2),encoding='utf-8')
print('troubleshooting',len(troubles),'glossary',len(gloss))
