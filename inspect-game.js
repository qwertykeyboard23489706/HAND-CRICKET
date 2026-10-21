const fs=require('fs'),s=fs.readFileSync('outputs/handcricket.html','utf8');
for(const [a,b] of [['<div class="home-matchup"','<div class="home-ctas"'],['<section class="arena"','</section>'],['function startMatch','function showPractice'],['function classify','function startCamera']]){let i=s.indexOf(a),j=s.indexOf(b,i);console.log('\n--- '+a+' ---\n'+s.slice(i,j>i?j:i+4000))}
