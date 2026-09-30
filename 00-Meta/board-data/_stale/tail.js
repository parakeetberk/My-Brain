const rows=[...document.querySelectorAll('.row')];
const q=document.getElementById('q'),fu=document.getElementById('fu'),fl=document.getElementById('fl'),
 cnt=document.getElementById('count'),none=document.getElementById('none');
const hay=DATA.map(x=>(x.id+' '+x.desc+' '+x.owner_full+' '+x.category+' '+x.community+' '+x.sec+' '+x.lot+' '+x.state+' '+x.srctype).toLowerCase());

/* ---- multi-selects ---- */
const FIELD={fp:'priority',fc:'category',fm:'community',fo:'owner_short'};
const MS=[...document.querySelectorAll('.ms')].map(el=>({
  el, id:el.id, field:FIELD[el.id],
  btn:el.querySelector('.ms__btn'), panel:el.querySelector('.ms__panel'),
  sel:el.querySelector('.ms__sel'),
  boxes:[...el.querySelectorAll('input[type=checkbox]')]}));
function chosen(m){return new Set(m.boxes.filter(b=>b.checked).map(b=>b.value));}
function label(m){
  const c=m.boxes.filter(b=>b.checked);
  m.sel.textContent=c.length===0?'all':(c.length===1?c[0].value:c.length+' selected');
  m.el.classList.toggle('on',c.length>0);
}
function closeAll(except){MS.forEach(m=>{if(m!==except)m.panel.hidden=true;});}
MS.forEach(m=>{
  m.btn.addEventListener('click',ev=>{ev.stopPropagation();
    const open=m.panel.hidden;closeAll(m);m.panel.hidden=!open;});
  m.panel.addEventListener('click',ev=>ev.stopPropagation());
  m.boxes.forEach(b=>b.addEventListener('change',()=>{label(m);apply();}));
  m.el.querySelector('.ms__all').addEventListener('click',()=>{m.boxes.forEach(b=>b.checked=true);label(m);apply();});
  m.el.querySelector('.ms__none').addEventListener('click',()=>{m.boxes.forEach(b=>b.checked=false);label(m);apply();});
});
document.addEventListener('click',()=>closeAll(null));
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')closeAll(null);});

function apply(){
  const t=q.value.trim().toLowerCase(),u=fu.checked,l=fl.checked;
  const sets=MS.map(m=>[m.field,chosen(m)]).filter(p=>p[1].size>0);
  let n=0;
  rows.forEach(r=>{const i=+r.dataset.i,x=DATA[i];
    let ok=(!t||hay[i].includes(t))&&(!u||x.owner_short==='Unassigned')&&(!l||!!x.srcurl);
    if(ok)for(const [f,s] of sets){if(!s.has(x[f])){ok=false;break;}}
    r.hidden=!ok; if(ok)n++;});
  const act=t||u||l||sets.length>0;
  document.querySelectorAll('details.sub').forEach(s=>{
    const v=[...s.querySelectorAll('.row')].filter(r=>!r.hidden).length;
    s.hidden=v===0; s.querySelector('[data-rn]').textContent=v; if(v&&act)s.open=true;});
  document.querySelectorAll('details.reg').forEach(s=>{
    const v=[...s.querySelectorAll('.row')].filter(r=>!r.hidden).length;
    s.hidden=v===0; s.querySelector('summary [data-rn]').textContent=v; if(v&&act)s.open=true;});
  cnt.innerHTML='<b>'+n+'</b> shown'; none.hidden=n>0;
}
[q,fu,fl].forEach(el=>el.addEventListener('input',apply));
document.getElementById('reset').onclick=()=>{q.value='';fu.checked=false;fl.checked=false;
  MS.forEach(m=>{m.boxes.forEach(b=>b.checked=false);label(m);m.panel.hidden=true;});
  document.querySelectorAll('details.sub').forEach(s=>s.open=false);apply();};
let exp=false;
document.getElementById('expand').onclick=ev=>{exp=!exp;
  document.querySelectorAll('details').forEach(s=>s.open=exp);
  ev.target.textContent=exp?'Collapse all':'Expand all';};
function flash(el,txt){const o=el.textContent;el.classList.add('copied');el.textContent=txt;
  setTimeout(()=>{el.classList.remove('copied');el.textContent=o;},900);}
function copy(s){try{navigator.clipboard.writeText(s);}catch(e){
  const t=document.createElement('textarea');t.value=s;document.body.appendChild(t);t.select();
  try{document.execCommand('copy');}catch(_){}t.remove();}}
document.addEventListener('click',ev=>{
  const id=ev.target.closest('.rid');
  if(id){copy(id.textContent.trim());flash(id,'copied');return;}
  const cq=ev.target.closest('.cpq');
  if(cq){copy(cq.dataset.q);flash(cq,'copied');}
});
MS.forEach(label);
apply();
