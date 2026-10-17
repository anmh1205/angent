// ANGENT: Figma Plugin API candidate. Generated locally, never run by generator.
// Paste into a real authorized Figma JS execution host (e.g. use_figma).
// "__ANGENT_SCREEN_SPEC_JSON__" is replaced with JSON, not executable code.
const angentScreens = __ANGENT_SCREEN_SPEC_JSON__;
const angentApply = async (figma) => {
  if (!figma || !figma.currentPage || typeof figma.createFrame !== 'function' ||
      typeof figma.createText !== 'function' || typeof figma.loadFontAsync !== 'function') {
    throw new Error('Native Figma Plugin API unavailable');
  }
  const page = figma.currentPage;
  if (typeof page.loadAsync === 'function') await page.loadAsync();
  const nameOf = c => 'control:' + c.type + ':' + c.id;
  const plan = [];
  for (const s of angentScreens) {
    // Stable screen ID, not a mutable title, is the Figma handoff identity.
    const prefix = 'ANGENT BA / ' + s.id + ' / ';
    const matches = page.children.filter(n => n.type === 'FRAME' && n.name.startsWith(prefix));
    if (matches.length > 1) throw new Error('Duplicate target screen ID: ' + s.id);
    const existing = matches[0] || null;
    if (existing && existing.name !== s.name) {
      throw new Error('Existing frame title conflicts with source screen ID: ' + s.id);
    }
    if (existing) {
      const headings = existing.children.filter(n => n.type === 'TEXT' && n.name === 'screen:title');
      if (headings.length !== 1 || headings[0].characters !== s.title) {
        throw new Error('Existing frame title text differs from source: ' + s.id);
      }
      const controls = existing.children.filter(n => n.name.startsWith('control:'));
      if (controls.length !== s.controls.length || controls.some((n,i) =>
          n.type !== 'FRAME' || n.name !== nameOf(s.controls[i]) ||
          !n.children.some(t => t.type === 'TEXT' &&
             t.characters === (s.controls[i].type === 'checkbox' ? '☐ ' : '') + s.controls[i].label))) {
        throw new Error('Existing frame differs from source, refusing overwrite: ' + s.name);
      }
    }
    plan.push({spec:s, existing});
  }
  // The font must be available before setting TextNode.characters/fontSize.
  await figma.loadFontAsync({family:'Inter', style:'Regular'});
  const paint = (r,g,b) => [{type:'SOLID',color:{r,g,b}}];
  const textNode = (name,characters,fontSize) => {
    // Figma creates TextNodes on the current page immediately. If setting
    // text fails before adoption by the target frame, remove that orphan.
    const t=figma.createText();
    try {
      t.autoRename=false;
      t.name=name;
      t.fontName={family:'Inter',style:'Regular'};
      t.fontSize=fontSize;
      t.characters=characters;
      t.fills=paint(0.13,0.18,0.25);
      return t;
    } catch (error) {
      try { t.remove(); } catch (ignored) {}
      throw error;
    }
  };
  const created=[];
  const receipts=[];
  try {
    for (let i=0;i<plan.length;i++) {
      const item=plan[i], s=item.spec;
      if (item.existing) {
        receipts.push({screen_id:s.id,node_id:item.existing.id,action:'unchanged',controls:s.controls.length});
        continue;
      }
      const root=figma.createFrame();
      created.push(root);
      root.name=s.name;
      root.resize(390,Math.max(350,140+s.controls.length*80));
      root.x=80+(i%4)*460;
      root.y=80+Math.floor(i/4)*850;
      root.fills=paint(1,1,1);
      root.layoutMode='VERTICAL';
      root.paddingTop=20;root.paddingBottom=20;
      root.paddingLeft=20;root.paddingRight=20;
      root.itemSpacing=12;
      root.appendChild(textNode('screen:title',s.title,20));
      for (const c of s.controls) {
        const box=figma.createFrame();
        box.name=nameOf(c);
        box.resize(350,64);
        box.layoutMode='VERTICAL';
        box.paddingTop=12;box.paddingBottom=12;
        box.paddingLeft=12;box.paddingRight=12;
        box.fills=paint(0.96,0.97,0.99);
        root.appendChild(box);
        const label=(c.type==='checkbox'?'☐ ':'')+c.label;
        box.appendChild(textNode('label:'+c.id,label,14));
      }
      const found=typeof figma.getNodeByIdAsync==='function'
          ? await figma.getNodeByIdAsync(root.id)
          : page.children.find(n => n.id === root.id);
      if (!found || found.type!=='FRAME' || found.name!==s.name) {
        throw new Error('Figma frame read-back failed: '+s.id);
      }
      const headingNodes=found.children.filter(n=>n.type==='TEXT' && n.name==='screen:title');
      if (headingNodes.length!==1 || headingNodes[0].characters!==s.title) {
        throw new Error('Figma title read-back failed: '+s.id);
      }
      const actual=found.children.filter(n=>n.name.startsWith('control:'));
      if (actual.length!==s.controls.length || actual.some((n,j)=>
          n.name!==nameOf(s.controls[j]) ||
          !n.children.some(t=>t.type==='TEXT' &&
             t.characters===(s.controls[j].type==='checkbox'?'☐ ':'')+s.controls[j].label))) {
        throw new Error('Figma controls incomplete after read-back: '+s.id);
      }
      receipts.push({screen_id:s.id,node_id:root.id,action:'created-and-read-back',controls:actual.length});
    }
  } catch (error) {
    // Best effort rollback only for nodes created by this operation.
    for (const frame of created.reverse()) {
      try { frame.remove(); } catch (ignored) {}
    }
    throw error;
  }
  return {ok:true,provider:'Figma Plugin API',scope:'current-page',
          created:created.length, unchanged:receipts.length-created.length,
          verified_in_host:true, receipts,
          not_implemented:['prototype reactions','live authentication','component library']};
};
const angentReceipt = await angentApply(figma);
console.log(JSON.stringify(angentReceipt));
