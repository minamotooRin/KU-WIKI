# 赛博老佛爷临幸纪念碑

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh; background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%); border-radius: 12px; padding: 40px 20px; margin: 20px 0;">

  <!-- 顶部横幅 -->
  <div style="color: #ffd700; font-size: 1.5em; font-weight: bold; letter-spacing: 8px; margin-bottom: 30px; text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);">
    奠
  </div>

  <!-- 肖像框 -->
  <div style="position: relative; padding: 8px; background: linear-gradient(135deg, #ffd700, #b8860b); border-radius: 8px; box-shadow: 0 0 30px rgba(255, 215, 0, 0.4), 0 10px 40px rgba(0,0,0,0.5);">
    <img src="assets/images/001.png" alt="001" style="display: block; width: 200px; height: auto; border-radius: 4px;">
  </div>

  <!-- 标语 -->
  <div id="memorial-slogan" style="margin-top: 30px; color: #fff; font-size: 1.4em; font-weight: bold; letter-spacing: 4px;">
    001元年
  </div>

  <!-- 装饰分隔线 -->
  <div style="margin: 25px 0; display: flex; align-items: center; gap: 15px;">
    <span style="font-size: 1.5em;">🕯️</span>
    <div style="width: 100px; height: 2px; background: linear-gradient(90deg, transparent, #ffd700, transparent);"></div>
    <span style="font-size: 1.5em;">🕯️</span>
  </div>

  <!-- 底部文字 -->
  <div style="color: #888; font-size: 0.9em; text-align: center;">
    永垂不朽
  </div>

</div>

<script>
(function() {
  var currentYear = new Date().getFullYear();
  var era = currentYear - 2022;
  var slogan = document.getElementById('memorial-slogan');
  if (slogan) {
    slogan.textContent = '001元年' + era + '年';
  }
})();
</script>
