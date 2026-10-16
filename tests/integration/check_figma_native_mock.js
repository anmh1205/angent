#!/usr/bin/env node
// Validate the generated native Figma plugin JavaScript against a deterministic
// Plugin API-shaped fake. This is NEVER evidence of a live canvas write.
const fs = require('node:fs');
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const file=process.argv[2];
if (!file) {console.error('Usage: node check_figma_native_mock.js PATH_TO_GENERATED.js');process.exit(2)}
const source=fs.readFileSync(file,'utf8');
let counter=0;
function mock() {
  const page={type:'PAGE',id:'page-1',children:[],async loadAsync(){}};
  let fontLoaded=false,failReadback=false;
  const nodes = new Map();
  const make = type => {
    const node={type,id:'node-'+(++counter),name:'',children:[],parent:page,removed:false,
      resize(w,h){this.width=w;this.height=h},
      appendChild(child) {
        if (child.parent) child.parent.children=child.parent.children.filter(x=>x!==child);
        this.children.push(child); child.parent=this;
      },
      remove() {
        if (this.parent) this.parent.children=this.parent.children.filter(x=>x!==this);
        this.removed=true;
        nodes.delete(this.id);
      }};
    Object.defineProperty(node,'characters',{
      get(){return this._characters},
      set(s){if(!fontLoaded)throw Error('Font not loaded');this._characters=s}
    });
    page.children.push(node); nodes.set(node.id,node);return node;
  };
  const figma={
    currentPage:page,
    createFrame:()=>make('FRAME'),
    createText:()=>make('TEXT'),
    async loadFontAsync({family,style}) {
      if (family!=='Inter'||style!=='Regular')throw Error('Unexpected font');
      fontLoaded=true;
    },
    async getNodeByIdAsync(id) {return failReadback?null:nodes.get(id)||null}
  };
  return {figma,page,setFailReadback:v=>{failReadback=v}};
}
const context=mock();
const logs=[];
const executor = new AsyncFunction('figma','console',source+'\nreturn angentReceipt;');
async function run() {
  const out=await executor(context.figma,{log:s=>logs.push(s)});
  if (out.created!==3||out.unchanged!==0||out.receipts.length!==3 ||
      !out.receipts.every(x=>x.action==='created-and-read-back')) {
    throw Error('First application did not create three verified frames');
  }
  if(context.page.children.filter(x=>x.type==='FRAME').length!==3)throw Error('Wrong root count');
  const twice=await executor(context.figma,{log:s=>logs.push(s)});
  if(twice.created!==0||twice.unchanged!==3)throw Error('Retry is not idempotent');
  const root=context.page.children.find(x=>x.name===out.receipts[0].screen_id?false:true);
  const first=context.page.children.find(x=>x.name.startsWith('ANGENT BA / login /'));
  if(!first)throw Error('Cannot find created login frame');
  const label=first.children.find(x=>x.name.startsWith('control:')).children.find(x=>x.type==='TEXT');
  label.characters='STALE CUSTOM EDIT';
  let blocked=false;
  try {await executor(context.figma,{log:s=>logs.push(s)})}catch(e){blocked=/source|conflict|differs/.test(String(e))}
  if(!blocked||context.page.children.filter(x=>x.type==='FRAME').length!==3) {
    throw Error('Existing human edit was overwritten or duplicated');
  }
  // The generator never supplies real credentials; escaping is checked elsewhere.
  const fresh=mock(); fresh.setFailReadback(true);
  let failed=false;
  try {await executor(fresh.figma,{log:s=>logs.push(s)})}catch(e){failed=/read-back/.test(String(e))}
  if(!failed||fresh.page.children.length!==0)throw Error('Failed native read-back must rollback fresh nodes');
  return {ok:true,native_plugin_api_mock_only:true,created:3,unchanged_on_retry:3,
          conflict_blocked:true,partial_creation_rolled_back:true,
          live_figma_writes:0};
}
run().then(value=>console.log(JSON.stringify(value))).catch(err=>{console.error(String(err.stack||err));process.exitCode=1});
