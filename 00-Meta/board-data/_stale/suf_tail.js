const rows=[...document.querySelectorAll('.row')];
const q=document.getElementById('q'),fp=document.getElementById('fp'),fc=document.getElementById('fc'),
 fm=document.getElementById('fm'),fo=document.getElementById('fo'),fu=document.getElementById('fu'),
 fl=document.getElementById('fl'),cnt=document.getElementById('count'),none=document.getElementById('none');
const hay=DATA.map(x=>(x.id+' '+x.desc+' '+x.owner_full+' '+x.category+' '+x.community+' '+x.sec+' '+x.lot+' '+x.state+' '+x.srctype).toLowerCase());
function apply(){
  const t=q.value.trim().toLowerCase(),p=fp.value,c=fc.value,m=fm.value,o=fo.value,u=fu.checked,l=fl.checked;
  let n=0;
  rows.forEach(r=>{const i=+r.dataset.i,x=DATA[i];
    const ok=(!t||hay[i].includes(t))&&(!p||x.priority===p)&&(!c||x.category===c)&&(!m||x.community===m)
      &&(!o||x.owner_short===o)&&(!u||x.owner_short==='Unassigned')&&(!l||!!x.srcurl);
    r.hidden=!ok; if(ok)n++;});
  const act=t||p||c||m||o||u||l;
  document.querySelectorAll('details.sub').forEach(s=>{
    const v=[...s.querySelectorAll('.row')].filter(r=>!r.hidden).length;
    s.hidden=v===0; s.querySelector('[data-rn]').textContent=v; if(v&&act)s.open=true;});
  document.querySelectorAll('details.reg').forEach(s=>{
    const v=[...s.querySelectorAll('.row')].filter(r=>!r.hidden).length;
    s.hidden=v===0; s.querySelector('summary [data-rn]').textContent=v; if(v&&act)s.open=true;});
  cnt.innerHTML='<b>'+n+'</b> shown'; none.hidden=n>0;
}
[q,fp,fc,fm,fo,fu,fl].forEach(el=>el.addEventListener('input',apply));
document.getElementById('reset').onclick=()=>{q.value='';fp.value='';fc.value='';fm.value='';fo.value='';
  fu.checked=false;fl.checked=false;document.querySelectorAll('details.sub').forEach(s=>s.open=false);apply();};
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
apply();
</script>
</body></html>