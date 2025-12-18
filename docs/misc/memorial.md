# 赛博老佛爷临幸纪念碑

<div id="memorial-container" style="position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 80vh; background: linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%); border-radius: 12px; padding: 40px 20px; margin: 20px 0; overflow: hidden;">

  <!-- 浮动emoji背景 -->
  <div id="floating-emojis" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: hidden;"></div>

  <!-- 五彩纸屑容器 -->
  <div id="confetti-container" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: hidden;"></div>

  <!-- 顶部横幅 -->
  <div id="banner" style="color: #fff; font-size: 1.8em; font-weight: bold; letter-spacing: 8px; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); z-index: 10; animation: bounce 2s ease infinite;">
    🎉 喜迎圣驾 🎉
  </div>

  <!-- 肖像框 -->
  <div id="portrait-frame" onclick="triggerCelebration()" style="position: relative; padding: 8px; background: linear-gradient(135deg, #ffd700, #ff6b6b, #ffd700); background-size: 200% 200%; border-radius: 12px; cursor: pointer; z-index: 10; animation: borderGlow 3s ease infinite, float 3s ease-in-out infinite;">
    <!-- 星星环绕 -->
    <div class="star star1">⭐</div>
    <div class="star star2">✨</div>
    <div class="star star3">⭐</div>
    <div class="star star4">✨</div>
    <img src="../assets/images/001.png" alt="001" style="display: block; width: 200px; height: auto; border-radius: 8px; transition: transform 0.3s ease;">
  </div>
  <div style="color: rgba(255,255,255,0.7); font-size: 0.8em; margin-top: 8px; z-index: 10;">👆 点击有惊喜</div>

  <!-- 标语 -->
  <div id="memorial-slogan" style="margin-top: 25px; font-size: 1.8em; font-weight: bold; letter-spacing: 4px; z-index: 10; background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #8b00ff, #ff0000); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: rainbow 3s linear infinite;">
    零零壹元年
  </div>

  <!-- 年份显示 -->
  <div id="year-display" style="margin-top: 10px; color: #fff; font-size: 3em; font-weight: bold; text-shadow: 0 0 20px rgba(255,215,0,0.8); z-index: 10;">
    <span id="year-counter">0</span>年
  </div>

  <!-- 装饰 -->
  <div style="margin: 20px 0; display: flex; align-items: center; gap: 15px; font-size: 2em; z-index: 10; animation: pulse 1.5s ease infinite;">
    🎊 🎆 🎇 🎆 🎊
  </div>

  <!-- 底部文字 -->
  <div style="color: #fff; font-size: 1.2em; text-align: center; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); z-index: 10; animation: glow 2s ease-in-out infinite alternate;">
    ✨ 普天同庆 ✨
  </div>

</div>

<style>
/* 弹跳动画 */
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(-15px); }
  60% { transform: translateY(-8px); }
}

/* 浮动动画 */
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-10px) rotate(2deg); }
}

/* 边框渐变发光 */
@keyframes borderGlow {
  0% { background-position: 0% 50%; box-shadow: 0 0 30px rgba(255, 215, 0, 0.6); }
  50% { background-position: 100% 50%; box-shadow: 0 0 50px rgba(255, 107, 107, 0.8); }
  100% { background-position: 0% 50%; box-shadow: 0 0 30px rgba(255, 215, 0, 0.6); }
}

/* 彩虹文字 */
@keyframes rainbow {
  0% { background-position: 0% center; }
  100% { background-position: 200% center; }
}

/* 脉冲动画 */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

/* 发光动画 */
@keyframes glow {
  from { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #ff00de; }
  to { text-shadow: 0 0 20px #fff, 0 0 30px #ff00de, 0 0 40px #ff00de; }
}

/* 星星环绕 */
.star {
  position: absolute;
  font-size: 1.2em;
  animation: orbit 4s linear infinite;
}
.star1 { top: -10px; left: 50%; animation-delay: 0s; }
.star2 { top: 50%; right: -15px; animation-delay: 1s; }
.star3 { bottom: -10px; left: 50%; animation-delay: 2s; }
.star4 { top: 50%; left: -15px; animation-delay: 3s; }

@keyframes orbit {
  0% { transform: rotate(0deg) translateX(10px) rotate(0deg) scale(1); opacity: 1; }
  50% { transform: rotate(180deg) translateX(10px) rotate(-180deg) scale(1.3); opacity: 0.7; }
  100% { transform: rotate(360deg) translateX(10px) rotate(-360deg) scale(1); opacity: 1; }
}

/* 浮动emoji */
@keyframes floatUp {
  0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
}

/* 纸屑飘落 */
@keyframes confettiFall {
  0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
  100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
}

/* 肖像悬停效果 */
#portrait-frame:hover img {
  transform: scale(1.1) rotate(5deg);
}
#portrait-frame:hover {
  animation: shake 0.5s ease;
}

@keyframes shake {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-5deg); }
  75% { transform: rotate(5deg); }
}
</style>

<script>
(function() {
  // 计算年份
  var currentYear = new Date().getFullYear();
  var era = currentYear - 2022;

  // 数字滚动动画
  var counter = document.getElementById('year-counter');
  var target = era;
  var current = 0;
  var duration = 2000;
  var stepTime = duration / target;

  function updateCounter() {
    if (current < target) {
      current++;
      counter.textContent = current;
      setTimeout(updateCounter, stepTime);
    }
  }
  setTimeout(updateCounter, 500);

  // 创建浮动emoji
  var emojis = ['🎉', '🎊', '🎈', '⭐', '✨', '🎆', '🎇', '💫', '🌟', '🥳'];
  var container = document.getElementById('floating-emojis');

  function createFloatingEmoji() {
    var emoji = document.createElement('div');
    emoji.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    emoji.style.cssText =
      'position: absolute;' +
      'font-size: ' + (Math.random() * 20 + 15) + 'px;' +
      'left: ' + Math.random() * 100 + '%;' +
      'bottom: 0;' +
      'animation: floatUp ' + (Math.random() * 5 + 5) + 's linear forwards;';
    container.appendChild(emoji);
    setTimeout(function() { emoji.remove(); }, 10000);
  }

  // 每隔一段时间创建新emoji
  setInterval(createFloatingEmoji, 800);
  // 初始创建几个
  for (var i = 0; i < 5; i++) {
    setTimeout(createFloatingEmoji, i * 200);
  }

  // 初始纸屑
  setTimeout(function() { triggerCelebration(); }, 1000);
})();

// 点击触发庆祝效果
function triggerCelebration() {
  var colors = ['#ff0000', '#ff7f00', '#ffff00', '#00ff00', '#0000ff', '#8b00ff', '#ff69b4', '#ffd700'];
  var container = document.getElementById('confetti-container');

  for (var i = 0; i < 50; i++) {
    (function(index) {
      setTimeout(function() {
        var confetti = document.createElement('div');
        confetti.style.cssText =
          'position: absolute;' +
          'width: ' + (Math.random() * 10 + 5) + 'px;' +
          'height: ' + (Math.random() * 10 + 5) + 'px;' +
          'background: ' + colors[Math.floor(Math.random() * colors.length)] + ';' +
          'left: ' + Math.random() * 100 + '%;' +
          'top: -10px;' +
          'border-radius: ' + (Math.random() > 0.5 ? '50%' : '0') + ';' +
          'animation: confettiFall ' + (Math.random() * 3 + 2) + 's linear forwards;';
        container.appendChild(confetti);
        setTimeout(function() { confetti.remove(); }, 5000);
      }, index * 30);
    })(i);
  }
}
</script>
