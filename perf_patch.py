from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8-sig')
# Replace high cost camera drawing/detection path with a throttled 15fps loop and cached canvas geometry.
s=s.replace("S={playerName:","S={lastDetectAt:0,lastDrawAt:0,playerName:",1)
old="function drawHands(lms){const c=$('#draw'),ctx=c.getContext('2d');c.width=c.clientWidth*devicePixelRatio;c.height=c.clientHeight*devicePixelRatio;ctx.scale(devicePixelRatio,devicePixelRatio);ctx.clearRect(0,0,c.clientWidth,c.clientHeight);if(!lms)return;"
new="function drawHands(lms){const c=$('#draw'),ctx=c.getContext('2d');const w=c.clientWidth,h=c.clientHeight,dpr=Math.min(1.5,devicePixelRatio||1);if(c.width!==Math.round(w*dpr)||c.height!==Math.round(h*dpr)){c.width=Math.round(w*dpr);c.height=Math.round(h*dpr)}ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,w,h);if(!lms)return;"
s=s.replace(old,new)
s=s.replace("function onResults(r){if(S.paused)return;const found=r.multiHandLandmarks||[];drawHands(found);", "function onResults(r){if(S.paused)return;const found=r.multiHandLandmarks||[];const now=performance.now();if(now-S.lastDrawAt>140){drawHands(found);S.lastDrawAt=now}")
s=s.replace("if(performance.now()-S.stableAt>115&&S.stableFrames>=3&&!S.committed)commit(n)","if(performance.now()-S.stableAt>55&&S.stableFrames>=2&&!S.committed)commit(n)")
s=s.replace("video:{facingMode:'user',width:{ideal:640},height:{ideal:480}}", "video:{facingMode:'user',width:{ideal:480,max:640},height:{ideal:360,max:480},frameRate:{ideal:24,max:30}}")
s=s.replace("numHands:2,minHandDetectionConfidence:.72,minHandPresenceConfidence:.68,minTrackingConfidence:.65", "numHands:2,minHandDetectionConfidence:.58,minHandPresenceConfidence:.55,minTrackingConfidence:.55")
s=s.replace("const detectFrame=()=>{if(!S.cam)return;if(v.readyState>=2&&v.currentTime!==S.lastVideoTime){const result=S.landmarker.detectForVideo(v,performance.now());S.lastVideoTime=v.currentTime;onResults({multiHandLandmarks:result.landmarks})}S.raf=requestAnimationFrame(detectFrame)}", "const detectFrame=()=>{if(!S.cam)return;const now=performance.now();if(document.visibilityState==='visible'&&now-S.lastDetectAt>=66&&v.readyState>=2&&v.currentTime!==S.lastVideoTime){S.lastDetectAt=now;S.lastVideoTime=v.currentTime;try{const result=S.landmarker.detectForVideo(v,now);onResults({multiHandLandmarks:result.landmarks})}catch(err){console.warn('Hand tracking frame skipped',err)}}S.raf=requestAnimationFrame(detectFrame)}")
# Explicitly label and announce the current innings score, while keeping both team totals.
s=s.replace('<b id="targetText">VS</b><small id="scoreCaption">MATCH <span>01</span></small>', '<b id="targetText">VS</b><small id="inningsContext">CURRENT INNINGS</small><small id="scoreCaption">MATCH <span>01</span></small>')
s=s.replace('<strong id="leftScore">0</strong>', '<strong id="leftScore" aria-live="polite" aria-atomic="true">0</strong>').replace('<strong id="rightScore">0</strong>', '<strong id="rightScore" aria-live="polite" aria-atomic="true">0</strong>')
s=s.replace("$('#targetText').textContent=S.target===null?'VS':`${bs} / ${S.target}`;", "$('#targetText').textContent=S.target===null?String(bs):`${bs} / ${S.target}`;$('#inningsContext').textContent=S.target===null?`${S.batting==='you'?(S.playerName||'YOU'):'AI BATTLE BOT'} · INNINGS SCORE`:'SCORE / TARGET';")
# Put a clear sound unlock control in the in-game header and strengthen default levels.
s=s.replace('<button class="navbtn" id="focusToggle" aria-pressed="false">⊡ FOCUS</button>', '<button class="navbtn" id="audioUnlockGame" type="button" aria-label="Enable game music and sound">♫ SOUND</button><button class="navbtn" id="focusToggle" aria-pressed="false">⊡ FOCUS</button>')
s=s.replace("$('#audioUnlock').onclick=unlockAudio;document.addEventListener", "$('#audioUnlock').onclick=unlockAudio;$('#audioUnlockGame').onclick=unlockAudio;document.addEventListener")
s=s.replace("const v=Math.min(.35,S.musicVolume*.72);", "const v=Math.min(.8,S.musicVolume*1.8);")
s=s.replace("if(beat%4===0)kick(now,.18*v);", "if(beat%4===0)kick(now,.42*v);")
s=s.replace("g.gain.linearRampToValueAtTime(.11*v,now+.045);", "g.gain.linearRampToValueAtTime(.22*v,now+.045);")
s=s.replace("pg.gain.linearRampToValueAtTime(.022*v,now+.2);", "pg.gain.linearRampToValueAtTime(.045*v,now+.2);")
# Remove stale single unused landmark and obsolete helper noise generation.
s=s.replace("const wrist=hands[0][0];","")
# Accessibility overrides: larger targets, visible focus, high contrast and clearer scores.
css="""
/* Readability and keyboard access */
:focus-visible{outline:3px solid #fff!important;outline-offset:3px!important}.btn,.navbtn,.cam-status,.pep{min-height:40px}.btn.small{min-height:42px;padding:10px 14px;font-size:11px}.scoreboard{background:#0d1712;border-color:#78877b}.team,.score-mid small{color:#d2ddd5}.team strong{font-size:clamp(34px,4vw,48px)}.score-mid b{font-size:clamp(36px,4vw,48px);color:#fff}.score-mid small{font-size:10px;line-height:1.4}.number-display>div{background:#111c15;border-color:#65766a}.number-display small{color:#d4ded7;font-size:10px}.number-display b{font-size:28px}.capture-hint{color:#c0cbc3;font-size:11px}.field-label2,.mode-note,.message,.phase-label{font-size:12px}.read-num{font-size:32px}.high-contrast .number-display>div{border-color:#d4ded7}.high-contrast .number-display small,.high-contrast .capture-hint,.high-contrast .cam-status{color:#fff}@media(max-width:640px){.team{font-size:11px}.team strong{font-size:31px}.score-mid{min-width:78px}.score-mid b{font-size:31px}.score-mid small{font-size:9px}.number-display small{font-size:9px}.number-display b{font-size:25px}}
"""
s=s.replace('</style>',css+'</style>',1)
p.write_text(s,encoding='utf-8')
