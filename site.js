function speak(text){
  if(!('speechSynthesis' in window)) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  const voices = speechSynthesis.getVoices();
  u.voice = voices.find(v => v.lang === 'en-GB') || voices.find(v => v.lang.startsWith('en')) || null;
  u.lang = 'en-GB';
  u.rate = 0.8;
  speechSynthesis.speak(u);
}

document.querySelectorAll('[data-say]').forEach(b => {
  b.addEventListener('click', () => speak(b.dataset.say));
});

document.querySelectorAll('.quiz').forEach(quiz => {
  const qs = quiz.querySelectorAll('.q');
  const score = quiz.querySelector('.score');
  let solved = 0;
  qs.forEach(q => {
    const result = q.querySelector('.result');
    q.querySelectorAll('.choice').forEach(c => {
      c.addEventListener('click', () => {
        if(q.dataset.done) return;
        if(c.dataset.ok !== undefined){
          c.classList.add('right');
          result.textContent = '✅ ' + q.dataset.answer;
          result.className = 'result ok';
          q.dataset.done = '1';
          solved++;
          speak(q.dataset.answer);
          if(score) score.textContent = solved === qs.length ? '🎉 Молодець! Усі ' + qs.length + ' правильно!' : 'Правильно: ' + solved + ' з ' + qs.length;
        } else {
          c.classList.add('wrong');
          result.textContent = 'Спробуй ще раз 🙂';
          result.className = 'result bad';
        }
      });
    });
  });
});
