/* Offline app logic smoke test with a minimal DOM mock; no browser engine required. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const DATA=JSON.parse(fs.readFileSync(path.join(root,'manual_data.json'),'utf8'));
const elements={
 guideData:{textContent:JSON.stringify(DATA)},
 main:{innerHTML:'',addEventListener(){}},
 nav:{innerHTML:''},
 toggleMenu:{setAttribute(){},addEventListener(){}},
 globalSearch:{value:'',addEventListener(){},focus(){},setSelectionRange(){}}
};
let storage={};const mockClassList={toggle(){},remove(){},contains(){return false}};
const ctx={
 document:{title:'',getElementById(id){return elements[id]??null},body:{classList:mockClassList},addEventListener(){}},
 window:{scrollTo(){},addEventListener(){}},
 localStorage:{getItem(k){return storage[k]??null},setItem(k,v){storage[k]=v}},
 location:{hash:''},history:{replaceState(){}},
 console,Number,Math,Date,JSON,encodeURIComponent,decodeURIComponent,Array,Set,Map,URL,
 confirm(){return true},alert(){},setTimeout(){}
};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(root,'web/app.js'),'utf8'),ctx,{timeout:5000});
assert.match(elements.main.innerHTML,/Learn the system/);
const visit=(route)=>{
 ctx.location.hash='#'+route;
 vm.runInContext('render(false)',ctx,{timeout:5000});
 assert.ok(elements.main.innerHTML.length>200,'Empty view '+route);
};
for(const route of ['home','lessons','topics','recipes','effects','shortcuts','troubleshoot','glossary','quiz','lab','audit','settings'])visit(route);
for(const ch of DATA.chapters){visit('lesson/'+ch.id);assert.ok(elements.main.innerHTML.includes(ch.title))}
for(const topic of DATA.topics){visit('topic/'+topic.id);assert.ok(elements.main.innerHTML.includes(topic.title))}
for(const recipe of DATA.recipes){visit('recipe/'+recipe.id);assert.ok(elements.main.innerHTML.includes(recipe.title))}
visit('search/'+encodeURIComponent('graph editor'));
assert.ok(elements.main.innerHTML.includes('Graph Editor'));
visit('lesson/'+DATA.chapters[0].id);
vm.runInContext(`updateStep('${DATA.chapters[0].id}:0',true)`,ctx,{timeout:5000});
assert.ok(JSON.parse(storage['ae_25_6_windows_manual_progress_v1']).steps[DATA.chapters[0].id+':0']);
visit('quiz');vm.runInContext('updateQuiz(0,1)',ctx,{timeout:5000});
assert.equal(JSON.parse(storage['ae_25_6_windows_manual_progress_v1']).answers[0],1);
ctx.location.hash='#%bad%zz';vm.runInContext('render(false)',ctx,{timeout:5000});
assert.match(elements.main.innerHTML,/Learn the system/);
console.log(`PASS: ${12+DATA.chapters.length+DATA.topics.length+DATA.recipes.length+2} routes, search, step state, quiz state, malformed URL hash`);
