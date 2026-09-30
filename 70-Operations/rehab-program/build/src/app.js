(function(){
var D = JSON.parse(document.getElementById('rehab').textContent);
var T = D.totals;
var $ = function(s,r){return (r||document).querySelector(s)};
var money=function(v){return '$'+Math.round(v).toLocaleString('en-US')};
var moneyK=function(v){var n=Math.abs(v),g=v<0?'\u2212':'';return n>=1000000?(g+'$'+(n/1000000).toFixed(2)+'M'):n>=1000?(g+'$'+Math.round(n/1000)+'K'):(g+'$'+Math.round(n))};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]})};
var el=function(t,a,h){var e=document.createElement(t);if(a)for(var k in a)e.setAttribute(k,a[k]);if(h!=null)e.innerHTML=h;return e};
var SVGNS='http://www.w3.org/2000/svg';
function sv(t,a){var e=document.createElementNS(SVGNS,t);for(var k in a)e.setAttribute(k,a[k]);return e}

/* ---------- stat tiles ---------- */
(function(){
  var host=$('#tiles'); if(!host) return;
  var pct=Math.round(T.turnOk/T.turnAll*100);
  var tiles=[
    {c:'g',lab:'Rehabs completed 2026',val:T.goalDone,sub:'against a 100+ board goal · 9.6/month pace puts the year near 115',bar:[T.goalDone/100,'var(--good-mark)']},
    {c:'g',lab:'60-day turn rate',val:pct+'%',sub:T.turnOk+' of '+T.turnAll+' measurable turns at or under 60 days · median 31 days',bar:[pct/100,'var(--good-mark)']},
    {c:'b',lab:'Open past 60 days',val:T.past60,sub:T.past90+' of them past 90 · ten are one Silver Breeze batch frozen on 2026-04-17'},
    {c:'b',lab:'Open with no start date',val:T.noStart,sub:money(T.noStartRem)+' of modelled scope not on the 60-day clock at all'},
    {c:'b',lab:'Three-way cost variance',val:'$274K',sub:'GL vs Rent Manager vs vendor tracker, same 219 units'},
    {c:'b',lab:'GL against finished homes',val:'$990K',sub:T.wipDoneN+' complete units still carrying GL spend · in WIP or capitalised is unknown'}
  ];
  tiles.forEach(function(t){
    var d=el('div',{class:'tile '+t.c});
    d.innerHTML='<p class="lab">'+esc(t.lab)+'</p><div class="val">'+esc(t.val)+'</div>'
      +(t.bar?'<div class="meter"><i style="width:'+Math.min(t.bar[0]*100,100).toFixed(0)+'%;background:'+t.bar[1]+'"></i></div>':'')
      +'<p class="sub2">'+esc(t.sub)+'</p>';
    host.appendChild(d);
  });
})();

/* ---------- three-way ---------- */
(function(){
  var host=$('#threeway_c'); if(!host) return;
  var items=[
    {s:'General ledger',a:T.gl,c:'What Accounting booked. The closest thing to truth on this page, and 30 to 45 days in arrears.'},
    {s:'Rent Manager',a:T.rm,c:'What ops typed on the issue. Only '+T.rmReal+' of 219 rows carry a real number — '+T.rmPlaceholder+' hold placeholder text. Dividing this by 219 is wrong by nearly a factor of three.'},
    {s:'Vendor tracker',a:T.tc,c:'What High Pace\u2019s own sheet says. A point-in-time export of a live shared sheet, and the sheet the weekly call reads from.'}
  ];
  items.forEach(function(i){
    var d=el('div',{class:'tw'});
    d.innerHTML='<p class="src">'+esc(i.s)+'</p><div class="amt">'+money(i.a)+'</div><p class="cav">'+i.c+'</p>';
    host.appendChild(d);
  });
  var sp=el('div',{class:'tw spread'});
  sp.innerHTML='<p class="src">The spread</p><div class="amt">'+money(Math.max(T.gl,T.rm,T.tc)-Math.min(T.gl,T.rm,T.tc))+'</div>'
    +'<p class="cav">Highest minus lowest. <b>Nobody owns the reconciliation between them</b> — the work is John Clark\u2019s, the money is the Controller seat\u2019s, and that seat is in transition. <span class="pill">PD-24</span><span class="pill">KP-0040</span></p>';
  host.appendChild(sp);
})();

/* ---------- completions vs goal ---------- */
(function(){
  var host=$('#chartCompletions'); if(!host) return;
  var d=D.completions, W=820, H=232, ml=34, mr=14, mt=16, mb=34;
  var iw=W-ml-mr, ih=H-mt-mb, max=20, bw=Math.min(52, iw/d.length-14);
  var s=sv('svg',{viewBox:'0 0 '+W+' '+H, role:'img','aria-label':'Rehabs completed per month in 2026 against a monthly pace of 12.5 needed for the 100-unit board goal'});
  [0,5,10,15,20].forEach(function(g){
    var y=mt+ih-(g/max)*ih;
    s.appendChild(sv('line',{x1:ml,x2:W-mr,y1:y,y2:y,class:'gl'}));
    var t=sv('text',{x:ml-8,y:y+4,class:'ax','text-anchor':'end'}); t.textContent=g; s.appendChild(t);
  });
  var ty=mt+ih-(12.5/max)*ih;
  s.appendChild(sv('line',{x1:ml,x2:W-mr,y1:ty,y2:ty,class:'tgt'}));
  var tl=sv('text',{x:ml+6,y:ty-7,class:'tgtlab','text-anchor':'start'}); tl.textContent='12.5/mo needed for 100'; s.appendChild(tl);
  d.forEach(function(m,i){
    var x=ml+(i+0.5)*(iw/d.length)-bw/2, h=(m.n/max)*ih, y=mt+ih-h;
    var g=sv('g',{}); g.appendChild(sv('title',{})).textContent=m.m+': '+m.n+' completed';
    var r=sv('rect',{x:x,y:y,width:bw,height:Math.max(h,2),rx:4,fill:'var(--s1)',class:'bar'});
    if(m.n>=13) r.setAttribute('fill','var(--s3)');
    g.appendChild(r);
    var v=sv('text',{x:x+bw/2,y:y-6,class:'dl','text-anchor':'middle'}); v.textContent=m.n; g.appendChild(v);
    var lx=sv('text',{x:x+bw/2,y:mt+ih+17,class:'ax','text-anchor':'middle'});
    lx.textContent=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][parseInt(m.m.slice(5),10)-1];
    g.appendChild(lx); s.appendChild(g);
  });
  host.appendChild(s);
})();

/* ---------- WIP by vehicle ---------- */
(function(){
  var host=$('#chartWip'); if(!host) return;
  var d=D.wip, W=820, H=250, ml=64, mr=14, mt=16, mb=42;
  var iw=W-ml-mr, ih=H-mt-mb;
  var max=600000, gw=iw/d.length, bw=Math.min(38,(gw-26)/2);
  var s=sv('svg',{viewBox:'0 0 '+W+' '+H, role:'img','aria-label':'GL spend by fund vehicle, split between open units where work-in-progress is expected and completed units where it should already have rolled out'});
  [0,150000,300000,450000,600000].forEach(function(g){
    var y=mt+ih-(g/max)*ih;
    s.appendChild(sv('line',{x1:ml,x2:W-mr,y1:y,y2:y,class:'gl'}));
    var t=sv('text',{x:ml-8,y:y+4,class:'ax','text-anchor':'end'}); t.textContent=g?moneyK(g):'$0'; s.appendChild(t);
  });
  d.forEach(function(v,i){
    var cx=ml+(i+0.5)*gw;
    [['open','var(--s1)',v.open,v.openN,'open units'],['done','var(--s2)',v.done,v.doneN,'complete units']].forEach(function(p,j){
      var x=cx-bw-1+j*(bw+2), h=(p[2]/max)*ih, y=mt+ih-h;
      var g=sv('g',{});
      g.appendChild(sv('title',{})).textContent=v.v+' — '+p[4]+': '+money(p[2])+' across '+p[3]+' units';
      g.appendChild(sv('rect',{x:x,y:y,width:bw,height:Math.max(h,2),rx:4,fill:p[1],class:'bar'}));
      var t=sv('text',{x:x+bw/2,y:y-6,class:'dl','text-anchor':'middle'}); t.textContent=moneyK(p[2]); g.appendChild(t);
      s.appendChild(g);
    });
    var lx=sv('text',{x:cx,y:mt+ih+17,class:'ax','text-anchor':'middle'}); lx.textContent=v.v; s.appendChild(lx);
    var l2=sv('text',{x:cx,y:mt+ih+31,class:'ax','text-anchor':'middle'});
    l2.textContent=v.tc===0?'no tracker coverage':((v.glAll-v.tc>=0?'+':'')+moneyK(v.glAll-v.tc)+' vs tracker');
    s.appendChild(l2);
  });
  host.appendChild(s);
})();

/* ---------- rollup tables ---------- */
function rollup(hostId, arr, label, limit){
  var host=$(hostId); if(!host) return;
  var rows=arr.filter(function(r){return r.k}).slice(0,limit||99);
  var mx=Math.max.apply(null,rows.map(function(r){return r.rem}))||1;
  var t=el('table',{class:'tbl'});
  t.innerHTML='<thead><tr><th>'+label+'</th><th class="num">Units</th><th class="num">Open</th>'
    +'<th class="num">GL booked</th><th class="num">Tracker</th><th>Modelled remaining <span style="text-transform:none;letter-spacing:0;font-weight:400">(model, not budget)</span></th></tr></thead>';
  var tb=el('tbody');
  rows.forEach(function(r){
    var tr=el('tr');
    tr.innerHTML='<td>'+esc(r.k)+(r.k==='UNRESOLVED'?' <span class="flagtag">code not resolvable</span>':'')+'</td>'
      +'<td class="num">'+r.n+'</td><td class="num">'+r.open+'</td>'
      +'<td class="num">'+(r.gl?money(r.gl):'—')+'</td>'
      +'<td class="num">'+(r.tc?money(r.tc):'—')+'</td>'
      +'<td class="barcell"><i style="width:'+(r.rem/mx*100).toFixed(1)+'%"></i><span>'+money(r.rem)+'</span></td>';
    tb.appendChild(tr);
  });
  t.appendChild(tb);
  host.appendChild(el('div',{class:'scroll'})).appendChild(t);
}
rollup('#tblCommunity', D.byCommunity, 'Community (codes resolved where possible)');
rollup('#tblVendor', D.byVendor, 'Vendor');
rollup('#tblTier', D.byTier, 'Tier');

/* ---------- aging ---------- */
(function(){
  var host=$('#tblAging'); if(!host) return;
  var mx=Math.max.apply(null,D.aging.map(function(r){return r.rem}))||1;
  var t=el('table',{class:'tbl'});
  t.innerHTML='<thead><tr><th>Days since start</th><th class="num">Open units</th><th>Modelled remaining</th></tr></thead>';
  var tb=el('tbody');
  D.aging.forEach(function(r){
    var bad=(r.b==='90+'||r.b==='no start');
    var tr=el('tr');
    tr.innerHTML='<td'+(bad?' style="font-weight:700"':'')+'>'+esc(r.b==='no start'?'No start date at all':r.b+' days')+'</td>'
      +'<td class="num"'+(bad?' style="color:var(--bad);font-weight:700"':'')+'>'+r.n+'</td>'
      +'<td class="barcell"><i style="width:'+(r.rem/mx*100).toFixed(1)+'%;background:'+(bad?'var(--bad-mark)':'var(--s1)')+'"></i><span>'+money(r.rem)+'</span></td>';
    tb.appendChild(tr);
  });
  t.appendChild(tb); host.appendChild(el('div',{class:'scroll'})).appendChild(t);
})();

/* ---------- gaps ---------- */
(function(){
  var host=$('#gaps'); if(!host) return;
  var byU={}; D.units.forEach(function(u){byU[u.u]=u});
  D.gaps.forEach(function(g){
    var us=g.ids.map(function(i){return byU[i]}).filter(Boolean);
    var gl=us.reduce(function(a,u){return a+u.gl},0), rem=us.reduce(function(a,u){return a+u.rem},0);
    var d=el('details',{class:'gap'});
    var sm=el('summary',{});
    sm.innerHTML='<span class="gt">'+esc(g.t)+'</span><span class="gn">'+us.length+'</span>'
      +'<span class="gm">'+(gl?'GL '+money(gl):'')+(gl&&rem?' · ':'')+(rem?'model '+money(rem):'')+'</span>';
    d.appendChild(sm);
    var b=el('div',{class:'gbody'});
    b.appendChild(el('p',{class:'gd'},esc(g.d)));
    b.appendChild(el('p',{class:'own'},'<b>Owner:</b> '+esc(g.own)+' &nbsp;·&nbsp; <b>Task:</b> <span class="pill">'+esc(g.td)+'</span>'));
    var t=el('table',{class:'tbl'});
    t.innerHTML='<thead><tr><th>Unit</th><th>Community</th><th>Fund</th><th>Status</th><th>Vendor</th>'
      +'<th class="num">GL</th><th class="num">Tracker</th><th class="num">Model</th><th class="num">Age</th><th>WIP code</th></tr></thead>';
    var tb=el('tbody');
    us.sort(function(a,c){return (c.gl-a.gl)||(c.age-a.age)}).forEach(function(u){
      var tr=el('tr');
      tr.innerHTML='<td class="u">'+esc(u.u)+'</td><td>'+esc(u.cc)+(u.coh?' <span class="chip coh">cohort</span>':'')+'</td>'
        +'<td>'+esc(u.v)+'</td><td><span class="chip '+(u.s==='Complete'?'cp':u.s==='In Progress'?'ip':'ns')+'">'+esc(u.s)+'</span></td>'
        +'<td>'+esc(u.vd)+'</td><td class="num">'+(u.gl?money(u.gl):'—')+'</td><td class="num">'+(u.tc?money(u.tc):'—')+'</td>'
        +'<td class="num">'+(u.rem?money(u.rem):'—')+'</td><td class="num">'+(u.st?u.age+'d':'—')+'</td>'
        +'<td class="u">'+(u.code?esc(u.code):'<span class="flagtag">none</span>')+'</td>';
      tb.appendChild(tr);
    });
    t.appendChild(tb);
    b.appendChild(el('div',{class:'scroll'})).appendChild(t);
    d.appendChild(b); host.appendChild(d);
  });
})();

/* ---------- every unit, filterable ---------- */
(function(){
  var host=$('#allUnits'); if(!host) return;
  var uniq=function(k){var s={};D.units.forEach(function(u){if(u[k])s[u[k]]=1});return Object.keys(s).sort()};
  var defs=[['s','Status'],['v','Fund'],['cc','Community'],['vd','Vendor'],['t','Tier'],['band','Age band'],['cat','Category']];
  var bar=$('#unitFilters');
  var state={q:''};
  defs.forEach(function(d){
    var sel=el('select',{'data-k':d[0],'aria-label':d[1]});
    sel.appendChild(el('option',{value:''},'All '+d[1].toLowerCase()));
    (d[0]==='band'?['0-30','31-60','61-90','90+','no start']:uniq(d[0])).forEach(function(v){
      sel.appendChild(el('option',{value:v},esc(v)));
    });
    sel.addEventListener('change',function(){state[d[0]]=sel.value;render()});
    bar.appendChild(sel);
  });
  var flg=el('select',{'data-k':'flag','aria-label':'Flag'});
  [['','All rows'],['any','Flagged only'],['coh','Cohort rows only'],['nocode','No WIP code'],['notrk','Not in vendor tracker'],['glnorm','GL but no RM cost'],['clean','Clean rows only']]
    .forEach(function(o){flg.appendChild(el('option',{value:o[0]},o[1]))});
  flg.addEventListener('change',function(){state.flag=flg.value;render()});
  bar.appendChild(flg);
  var q=el('input',{type:'search',placeholder:'Search unit, community, vendor, flag…','aria-label':'Search'});
  q.addEventListener('input',function(){state.q=q.value.toLowerCase();render()});
  bar.appendChild(q);
  var rst=el('button',{type:'button'},'Reset');
  rst.addEventListener('click',function(){state={q:''};bar.querySelectorAll('select').forEach(function(s){s.value=''});q.value='';render()});
  bar.appendChild(rst);
  var cnt=el('span',{class:'count'}); bar.appendChild(cnt);

  var head='<thead><tr><th>Unit</th><th>Community</th><th>Fund</th><th>Status</th><th>Tier</th><th>Vendor</th>'
    +'<th class="num">GL</th><th class="num">RM</th><th class="num">Tracker</th><th class="num">Model rem.</th>'
    +'<th class="num">Age</th><th>WIP code</th><th>Flags</th></tr></thead>';
  var wrapEl=el('div',{class:'scroll'}); host.appendChild(wrapEl);
  function render(){
    var rows=D.units.filter(function(u){
      for(var k in state){
        if(k==='q'||k==='flag'||!state[k]) continue;
        if(String(u[k])!==state[k]) return false;
      }
      if(state.flag==='any'&&!u.fl.length) return false;
      if(state.flag==='clean'&&u.fl.length) return false;
      if(state.flag==='coh'&&!u.coh) return false;
      if(state.flag==='nocode'&&u.code) return false;
      if(state.flag==='notrk'&&u.intrk) return false;
      if(state.flag==='glnorm'&&!u.fl.some(function(f){return f.indexOf('GL has spend but Rent Manager')>-1})) return false;
      if(state.q){
        var hay=(u.u+' '+u.cc+' '+u.c+' '+u.vd+' '+u.v+' '+u.t+' '+u.s+' '+u.code+' '+u.fl.join(' ')).toLowerCase();
        if(hay.indexOf(state.q)<0) return false;
      }
      return true;
    });
    rows.sort(function(a,b){return (b.gl-a.gl)||(b.rem-a.rem)});
    var glS=rows.reduce(function(a,u){return a+u.gl},0), remS=rows.reduce(function(a,u){return a+u.rem},0);
    cnt.textContent=rows.length+' of '+D.units.length+' units · GL '+money(glS)+' · model '+money(remS);
    var t=el('table',{class:'tbl'}); t.innerHTML=head;
    var tb=el('tbody');
    if(!rows.length) tb.appendChild(el('tr',{},'<td colspan="13" style="color:var(--muted);padding:22px 10px">No units match. Reset the filters.</td>'));
    rows.forEach(function(u){
      var tr=el('tr');
      tr.innerHTML='<td class="u">'+esc(u.u)+'</td>'
        +'<td>'+esc(u.cc)+(u.coh?' <span class="chip coh">cohort</span>':'')+'</td>'
        +'<td>'+esc(u.v)+'</td>'
        +'<td><span class="chip '+(u.s==='Complete'?'cp':u.s==='In Progress'?'ip':'ns')+'">'+esc(u.s)+'</span></td>'
        +'<td>'+esc(u.t)+'</td><td>'+esc(u.vd)+'</td>'
        +'<td class="num">'+(u.gl?money(u.gl):'—')+'</td>'
        +'<td class="num">'+(u.rms==='RM UDF'?money(u.rm):'<span style="color:var(--muted)">'+esc(u.rms)+'</span>')+'</td>'
        +'<td class="num">'+(u.tc?money(u.tc):'—')+'</td>'
        +'<td class="num">'+(u.rem?money(u.rem):'—')+'</td>'
        +'<td class="num">'+(u.st?u.age+'d':'<span style="color:var(--bad)">none</span>')+'</td>'
        +'<td class="u">'+(u.code?esc(u.code):'<span class="flagtag">none</span>')+'</td>'
        +'<td>'+(u.fl.length?u.fl.map(function(f){return '<span class="flagtag">'+esc(f)+'</span>'}).join(''):'<span style="color:var(--muted)">—</span>')+'</td>';
      tb.appendChild(tr);
    });
    t.appendChild(tb);
    wrapEl.innerHTML=''; wrapEl.appendChild(t);
  }
  render();
})();
})();
