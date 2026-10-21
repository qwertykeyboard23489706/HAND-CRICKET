from pathlib import Path
p=Path('outputs/handcricket.html')
s=p.read_text(encoding='utf-8')
repls={
"function update(){const bs=S.scores[S.batting]??0;":"function update(){const bs=S.scores[S.batting]??0;$('#replayBall').classList.toggle('hidden',!S.lastBallSnapshot||S.phase!=='ready');",
"function startBall(){if(S.phase!=='ready')return;S.ballTimers=[];":"function startBall(){if(S.phase!=='ready')return;S.ballTimers=[];update();",
"function commit(playerNum){if(S.phase!=='reveal'||S.committed)return;S.committed=true;":"function commit(playerNum){if(S.phase!=='reveal'||S.committed)return;S.lastBallSnapshot={scores:{...S.scores},wickets:S.wickets,balls:S.balls,superBalls:S.superBalls,feed:[...S.feed],batting:S.batting};S.committed=true;",
"const cpuNum=S.cpuChoice||1+Math.floor(Math.random()*10);const batterNum=":"const cpuNum=S.cpuChoice||1+Math.floor(Math.random()*10);$('#playerNumberDisplay').textContent=playerNum;$('#opponentNumberDisplay').textContent=cpuNum;$('#runsDisplay').textContent='0';$('#ballResultDisplay').textContent='PLAYING';const batterNum=",
"if(out){S.wickets++;eventLog(label,'WICKET');":"if(out){$('#ballResultDisplay').textContent='WICKET';S.wickets++;eventLog(label,'WICKET');",
"}else{eventLog(label,`+${runs} RUN${runs===1?'':'S'}`);":"}else{$('#runsDisplay').textContent=String(runs);$('#ballResultDisplay').textContent=runs===0?'DOT BALL':runs>=4?'BOUNDARY':'RUNS';eventLog(label,`+${runs} RUN${runs===1?'':'S'}`);",
"$('#mainAction').disabled=true;$('#mainAction').textContent='WATCH THE BEAT';":"$('#mainAction').disabled=true;$('#mainAction').textContent='WATCH THE BEAT';$('#playerNumberDisplay').textContent='—';$('#opponentNumberDisplay').textContent='—';$('#runsDisplay').textContent='—';$('#ballResultDisplay').textContent='WAITING';",
"$('#rulesBtn').onclick=":"$('#focusToggle').onclick=()=>{const on=document.body.classList.toggle('focus-mode');$('#focusToggle').setAttribute('aria-pressed',String(on));$('#focusToggle').textContent=on?'× EXIT FOCUS':'⊡ FOCUS'};$('#rulesBtn').onclick=",
"function nextMatch(){":"function replayLastBall(){const x=S.lastBallSnapshot;if(!x)return;S.scores={...x.scores};S.wickets=x.wickets;S.balls=x.balls;S.superBalls=x.superBalls;S.feed=[...x.feed];S.batting=x.batting;$('#feed').innerHTML=S.feed.map(v=>`<div class=\"feedrow\"><strong>${v.text}</strong><span>${v.result}</span></div>`).join('');S.phase='ready';S.committed=false;update();startBall()}$('#replayBall').onclick=replayLastBall;function replayMatch(){closeModal();S.scores={you:0,cpu:0};S.wickets=0;S.balls=0;S.superBalls=0;S.super=false;S.secondInnings=false;S.target=null;S.lastBallSnapshot=null;S.feed=[];S.phase='setup';S.match=1;S.playerWins=0;S.cpuWins=0;$('#tossBtn').disabled=false;$('#tossBtn').textContent='FLIP THE COIN';$('#tossTitle').textContent='Waiting for toss';$('#tossText').textContent='Win the toss to choose whether to bat or bowl first.';$('#coin').textContent='?';$('#feed').innerHTML='<div class=\"feedrow\"><strong>Awaiting first ball</strong><span>—</span></div>';setMessage('NEW MATCH SETUP','Edit the settings if you like, then flip the toss.');$('#homeScreen').classList.add('hidden');update()}function nextMatch(){"
}
for a,b in repls.items():
    if a not in s: print('MISSING',a[:75])
    else: s=s.replace(a,b,1)
p.write_text(s,encoding='utf-8')
