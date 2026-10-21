from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8')
s=s.replace('</div>\n<div class="arena"><div class="field">','</div>\n<div class="number-display" aria-label="Last play numbers"><div><small>YOUR NUMBER</small><b id="playerNumberDisplay">—</b></div><div><small>AI BATTLE BOT</small><b id="opponentNumberDisplay">—</b></div><div><small>RUNS THIS BALL</small><b id="runsDisplay">—</b></div><div><small>RESULT</small><b id="ballResultDisplay">READY</b></div></div><div class="arena"><div class="field">',1)
s=s.replace("`<div class=\"modal-actions\"><button class=\"btn\" onclick=\"location.reload()\">PLAY AGAIN</button></div>`)","`<div class=\"modal-actions\"><button class=\"btn secondary\" id=\"replayMatchBtn\">REPLAY SERIES</button><button class=\"btn\" id=\"anotherMatchBtn\">PLAY ANOTHER · EDIT SETUP</button></div>`);$('#replayMatchBtn').onclick=replayMatch;$('#anotherMatchBtn').onclick=replayMatch")
s=s.replace("if(hands.length!==1)return null;const lm=hands[0]", "if(hands.length!==1)return null;const lm=hands[0]")
p.write_text(s,encoding='utf-8')
