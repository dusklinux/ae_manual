"""Additional audit of text, reader portability, references, exact exports and navigation."""
import csv
import json
import pathlib
import re
import shutil
import subprocess
import unittest
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]

class SecondPassChecks(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.d=json.loads((ROOT/'manual_data.json').read_text(encoding='utf8'))
  cls.md=(ROOT/'ALL_CONTENT.md').read_text(encoding='utf8')
  cls.html=(ROOT/'index.html').read_text(encoding='utf8')

 def test_reader_platform_distinct_from_application_platform(self):
  self.assertEqual(self.d['meta']['platform'],'Windows')
  self.assertEqual(self.d['meta']['readerPlatforms'],['Linux','Windows'])
  self.assertIn('Linux', (ROOT/'README.md').read_text(encoding='utf8'))
  self.assertIn('Linux',self.html)
  self.assertNotIn('<script src=',self.html)
  self.assertNotIn('<link rel="stylesheet"',self.html)

 def test_version_discipline_and_historical_security_source(self):
  self.assertEqual(self.d['meta']['applicationVersion'],'25.6')
  self.assertIn('security25',self.d['sources'])
  self.assertIn('25.6.4',self.d['sources']['security25']['note'])
  self.assertIn('quick offset',str(self.d['recipes']).lower())
  for name in ('Quick Apply','Object Matte','Unmult','Curl Noise','Compressor','Gate'):
   self.assertNotIn(name.casefold(),{x['name'].casefold() for x in self.d['effects']})

 def test_effects_include_missing_critical_families(self):
  names={x['name'] for x in self.d['effects']}
  for name in ('3D Camera Tracker','CC Rainfall','CC Snowfall','Slider Control','Color Control','Dropdown Menu Control','Echo','CC Wide Time','Timecode','VR Converter','CC Environment'):
   self.assertIn(name,names)
  self.assertEqual(len(names),len(self.d['effects']))
  self.assertTrue(any(x['category'].startswith('Obsolete') for x in self.d['effects']))

 def test_lesson_keyframes_sequenced(self):
  ch=next(c for c in self.d['chapters'] if c['id']=='keys')
  self.assertIn('time 0',ch['steps'][1]);self.assertIn('first Opacity keyframe',ch['steps'][1])

 def test_markdown_deep_links_have_targets(self):
  ids=re.findall(r'<a id="([a-z0-9-]+)"></a>',self.md)
  links=re.findall(r'\]\(#(lesson-[a-z0-9-]+|topic-[a-z0-9-]+)\)',self.md)
  self.assertEqual(len(ids),len(set(ids)))
  self.assertTrue(set(links)<=set(ids),set(links)-set(ids))
  self.assertEqual(len([x for x in ids if x.startswith('lesson-')]),len(self.d['chapters']))
  self.assertEqual(len([x for x in ids if x.startswith('topic-')]),len(self.d['topics']))

 def test_csv_fields_match_json_not_just_ids(self):
  for kind in ('effects','shortcuts'):
   with (ROOT/f'{kind}.csv').open(encoding='utf8',newline='') as f:
    reader=csv.DictReader(f)
    rows=list(reader)
    for row,item in zip(rows,self.d[kind]):
     for key,val in row.items():self.assertEqual(val,str(item.get(key,'')),(kind,item['id'],key))

 def test_generated_website_needs_no_network(self):
  template=(ROOT/'web/template.html').read_text(encoding='utf8')
  js=(ROOT/'web/app.js').read_text(encoding='utf8')
  self.assertNotRegex(template,r'<(?:script|link)\b[^>]+(?:src|href)=')
  for token in ('fetch(', 'XMLHttpRequest(', 'WebSocket(', 'sendBeacon(', 'import('):
   self.assertNotIn(token,js)

 def test_zip_content_is_safe_and_complete(self):
  p=ROOT/'after_effects_25_6_windows_offline_manual.zip'
  with zipfile.ZipFile(p) as z:
   self.assertIsNone(z.testzip())
   files=[x for x in z.namelist() if not x.endswith('/')]
   self.assertIn('tests/browser_logic.cjs',files)
   for name in files:
    self.assertFalse(name.startswith('/') or '..' in pathlib.PurePosixPath(name).parts)
    self.assertEqual(z.read(name),(ROOT/name).read_bytes())

 @unittest.skipUnless(shutil.which('node'), 'Node.js optional; not required to read the manual')
 def test_js_syntax_and_app_logic_simulation(self):
  for args in (('node','--check','web/app.js'),('node','tests/browser_logic.cjs')):
   out=subprocess.run(args,cwd=ROOT,text=True,capture_output=True,timeout=30)
   self.assertEqual(out.returncode,0,out.stderr or out.stdout)

if __name__=='__main__':unittest.main()
