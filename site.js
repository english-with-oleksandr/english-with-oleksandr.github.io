const AUDIO = new URL('audio/', document.currentScript.src);
const player = new Audio();

function slug(text){
  return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function speak(text){
  player.pause();
  player.src = new URL(slug(text) + '.mp3', AUDIO).href;
  player.currentTime = 0;
  player.play().catch(() => {});
}

document.querySelectorAll('[data-say]').forEach(b => {
  b.addEventListener('click', () => speak(b.dataset.say));
});

document.querySelectorAll('.peek').forEach(b => {
  b.addEventListener('click', () => {
    const hint = b.nextElementSibling;
    hint.hidden = !hint.hidden;
    b.textContent = hint.hidden ? '👀 Показати слова' : '🙈 Сховати';
  });
});

document.querySelectorAll('.quiz').forEach(quiz => {
  const qs = quiz.querySelectorAll('.q');
  const score = quiz.querySelector('.score');
  let done = 0, first = 0;
  qs.forEach(q => {
    const result = q.querySelector('.result');
    let missed = false;
    q.querySelectorAll('.choice').forEach(c => {
      c.addEventListener('click', () => {
        if(q.dataset.done) return;
        if(c.dataset.ok === undefined){
          missed = true;
          c.classList.add('wrong');
          result.textContent = 'Спробуй ще раз 🙂';
          result.className = 'result bad';
          return;
        }
        c.classList.add('right');
        q.dataset.done = '1';
        done++;
        if(!missed) first++;
        result.textContent = '✅ ' + q.dataset.answer;
        result.className = 'result ok';
        speak(q.dataset.answer);
        if(!score) return;
        score.textContent = done === qs.length
          ? '🎉 Готово! З першої спроби: ' + first + ' з ' + qs.length
          : 'Зроблено: ' + done + ' з ' + qs.length;
      });
    });
  });
});
