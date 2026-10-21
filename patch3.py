from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8')
s=s.replace("S.ballTimers=[];update();S.phase='count';", "S.ballTimers=[];S.phase='count';update();")
s=s.replace("// Landmark finger-state classifier. Uses one primary hand for 1–9; both hands together = 5, both open = 10.","// Landmark finger-state classifier. One hand only: open palm = 5 and closed fist = 10.")
s=s.replace("function nextMatch(){", "function editAnotherMatch(){replayMatch();$('#homeScreen').classList.remove('hidden')}function nextMatch(){")
s=s.replace("$('#anotherMatchBtn').onclick=replayMatch", "$('#anotherMatchBtn').onclick=editAnotherMatch")
p.write_text(s,encoding='utf-8')
