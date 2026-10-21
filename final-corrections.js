const fs=require('fs');const p='outputs/handcricket.html';let s=fs.readFileSync(p,'utf8');
s=s.replace("sound:saved.sound!==false,effectsVolume:saved.effectsVolume??.65,musicVolume:saved.musicVolume??.12,musicOn:saved.musicOn!==false", "sound:true,effectsVolume:saved.effectsVolume||.8,musicVolume:saved.musicVolume||.32,musicOn:true");
s=s.replace("$('#playerLabel').textContent=(S.playerName||'PLAYER').toUpperCase();$('#playerStatus')", "$('#playerLabel').textContent=(S.playerName||'PLAYER').toUpperCase();$('#playerHomeName').textContent=S.playerName?S.playerName.toUpperCase():'YOUR NAME';$('#playerStatus')");
s=s.replace("if(step%8===0)kick(now,.42*v);if(step%16===8)kick(now,.27*v);if(step%16===4||step%16===12)drumNoise(now,.16,.25*v,900);", "if(step%4===0)kick(now,.42*v);if(step%8===6)kick(now,.2*v);if(step%8===4)drumNoise(now,.16,.25*v,900);");
s=s.replace('const now=ac.currentTime,v=S.musicVolume;', 'const now=ac.currentTime,v=Math.min(.8,S.musicVolume*2);');
s=s.replace('Computer won the toss!', 'AI Battle Bot won the toss!').replace('Computer is choosing its opening innings…','AI Battle Bot is choosing its opening innings…').replace('Computer is batting','AI Battle Bot is batting').replace('Computer wins','AI Battle Bot wins').replace('Computer takes it.','AI Battle Bot takes it.');
s=s.replace('Pip is batting', 'AI Battle Bot is batting').replace('Pip are out', 'AI Battle Bot is out');
fs.writeFileSync(p,s);
