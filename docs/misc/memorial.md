# 赛博老佛爷临幸纪念碑

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh; background: linear-gradient(180deg, #ff6b6b 0%, #feca57 50%, #ff9ff3 100%); border-radius: 12px; padding: 40px 20px; margin: 20px 0;">

  <!-- 顶部横幅 -->
  <div style="color: #fff; font-size: 1.5em; font-weight: bold; letter-spacing: 8px; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
    🎉 喜迎圣驾 🎉
  </div>

  <!-- 肖像框 -->
  <div style="position: relative; padding: 8px; background: linear-gradient(135deg, #ffd700, #ff6b6b); border-radius: 12px; box-shadow: 0 0 30px rgba(255, 215, 0, 0.6), 0 10px 40px rgba(0,0,0,0.3); animation: glow 2s ease-in-out infinite alternate;">
    <img src="../assets/images/001.png" alt="001" style="display: block; width: 200px; height: auto; border-radius: 8px;">
  </div>

  <!-- 标语 -->
  <div id="memorial-slogan" style="margin-top: 30px; color: #fff; font-size: 1.6em; font-weight: bold; letter-spacing: 4px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
    零零壹元年
  </div>

  <!-- 装饰 -->
  <div style="margin: 25px 0; display: flex; align-items: center; gap: 15px; font-size: 1.5em;">
    🎊 ✨ 🎆 ✨ 🎊
  </div>

  <!-- 底部文字 -->
  <div style="color: #fff; font-size: 1em; text-align: center; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
    普天同庆
  </div>

</div>

<style>
@keyframes glow {
  from { box-shadow: 0 0 30px rgba(255, 215, 0, 0.6), 0 10px 40px rgba(0,0,0,0.3); }
  to { box-shadow: 0 0 50px rgba(255, 107, 107, 0.8), 0 10px 40px rgba(0,0,0,0.3); }
}
</style>

<script>
(function() {
  var currentYear = new Date().getFullYear();
  var era = currentYear - 2022;
  var slogan = document.getElementById('memorial-slogan');
  if (slogan) {
    slogan.textContent = '零零壹元年' + era + '年';
  }
})();
</script>
