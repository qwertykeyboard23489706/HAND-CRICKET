from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8-sig')
a=s.index('function musicStart()');b=s.index('function musicStop()',a)
new=r'''function musicStart(){if(!S.musicOn||S.musicVolume<=0||!audio)return;try{ac??=new audio();if(ac.state!=='running'){ac.resume().catch(()=>{});return}}catch(e){return}if(S.musicNodes.length)return;try{const sr=ac.sampleRate,duration=8,length=Math.floor(sr*duration),buffer=ac.createBuffer(1,length,sr),data=buffer.getChannelData(0),chords=[[130.81,164.81,196],[110,130.81,164.81],[87.31,110,130.81],[98,123.47,146.83]],roots=[55,55,43.65,49];for(let i=0;i<length;i++){const t=i/sr,section=Math.floor(t/2)%4,within=t%2,x=Math.max(0,Math.min(1,(within-1.78)/.22)),blend=x*x*(3-2*x),next=(section+1)%4;let pad=0;for(let n=0;n<3;n++){const f=chords[section][n]*(1-blend)+chords[next][n]*blend;pad+=Math.sin(2*Math.PI*f*t)*(.035-n*.004)}const root=roots[section]*(1-blend)+roots[next]*blend,beatAge=t%0.5,kick=Math.sin(2*Math.PI*(48+65*Math.exp(-beatAge*24))*beatAge)*Math.exp(-beatAge*12)*.19;const beat=Math.floor(t/.5)%4,snareAge=(t%2);const snare=(beat===1||beat===3)?(Math.random()*2-1)*Math.exp(-snareAge*25)*.035:0;const hatAge=t%0.25,hat=(Math.random()*2-1)*Math.exp(-hatAge*38)*.012;const bass=Math.sin(2*Math.PI*root*t)*(.085+.025*Math.cos(2*Math.PI*2*t));const edge=Math.min(1,t/.025,(duration-t)/.025);data[i]=Math.max(-.8,Math.min(.8,(pad+bass+kick+snare+hat)*Math.max(0,edge)))}const bus=ac.createGain(),source=ac.createBufferSource();bus.gain.setValueAtTime(S.musicVolume*1.6,ac.currentTime);source.buffer=buffer;source.loop=true;source.connect(bus);bus.connect(ac.destination);source.start();S.musicGain=bus;S.musicNodes=[source,bus]}catch(e){S.musicNodes=[];console.warn('Background music could not start',e)}}'''
s=s[:a]+new+s[b:]
s=s.replace("S.musicVolume*.62", "S.musicVolume*1.6")
s=s.replace("b.textContent='♫ SOUND ON'", "b.textContent='♫ MUSIC ON'")
s=s.replace("bg.textContent='♫ SOUND ON'", "bg.textContent='♫ MUSIC ON'")
# Keep the original clear count in lockstep: beat 1, beat 2, reveal at 1.8 s.
# No changes to the startBall timing or count cue sounds.
p.write_text(s,encoding='utf-8')
