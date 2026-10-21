from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8-sig')
s=s.replace("if(b){b.textContent='♫ SOUND ON';b.setAttribute('aria-pressed','true')}}catch(e)","if(b){b.textContent='♫ SOUND ON';b.setAttribute('aria-pressed','true')}const bg=$('#audioUnlockGame');if(bg){bg.textContent='♫ SOUND ON';bg.setAttribute('aria-pressed','true')}}catch(e)")
s=s.replace('.focus-mode .topright .pill,.focus-mode #pauseBtn', '.focus-mode .topright .pill,.focus-mode #audioUnlockGame,.focus-mode #pauseBtn')
p.write_text(s,encoding='utf-8')
