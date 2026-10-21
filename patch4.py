from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8')
s=s.replace('.focus-mode .topright .pill,.focus-mode #settingsBtn,.focus-mode #homeBtn{display:none}', '.focus-mode .top .brand,.focus-mode .topright .pill,.focus-mode #pauseBtn,.focus-mode #settingsBtn,.focus-mode #homeBtn,.focus-mode .game-info .phase-label,.focus-mode .game-info .message,.focus-mode .game-info .balls,.focus-mode #replayBall{display:none}')
s=s.replace("$('#coin').textContent='?';$('#feed').innerHTML", "$('#coin').textContent='?';$('#tossChoices').classList.add('hidden');$('#feed').innerHTML",1)
p.write_text(s,encoding='utf-8')
