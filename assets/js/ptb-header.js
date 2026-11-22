/* Thanh đầu trang: chọn bài, bài trước/sau, đồng hồ tiết học, phóng chữ cho cả lớp xem. */
(function () {
  function ready(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }
  ready(function () {
    var root = document.documentElement;
    // Picker
    var btn = document.querySelector('.ptb-picker-btn'), menu = document.querySelector('.ptb-menu');
    if (btn && menu) {
      function close() { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
      btn.addEventListener('click', function (e) {
        e.stopPropagation(); var o = menu.classList.toggle('open'); btn.setAttribute('aria-expanded', o ? 'true' : 'false');
        if (o) { var a = menu.querySelector('a.active'); if (a) a.scrollIntoView({ block: 'nearest' }); }
      });
      document.addEventListener('click', function (e) { if (!menu.contains(e.target)) close(); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    }
    // Timer
    var tb = document.querySelector('.ptb-timer'), rb = document.querySelector('.ptb-timer-reset');
    if (tb) {
      var total = (parseInt(tb.getAttribute('data-min'), 10) || 120) * 60, left = total, h = null;
      function fmt(s) { var m = Math.floor(Math.abs(s) / 60), r = Math.abs(s) % 60; return (s < 0 ? '+' : '') + m + ':' + (r < 10 ? '0' : '') + r; }
      function draw() {
        tb.textContent = '⏱ ' + fmt(left);
        tb.classList.toggle('run', !!h); tb.classList.toggle('warn', left <= 300 && left > 0); tb.classList.toggle('over', left <= 0);
        tb.title = h ? 'Bấm để tạm dừng đồng hồ' : 'Bấm để bắt đầu đếm ngược tiết học';
      }
      tb.addEventListener('click', function () {
        if (h) { clearInterval(h); h = null; } else { h = setInterval(function () { left--; draw(); }, 1000); }
        draw();
      });
      if (rb) rb.addEventListener('click', function () { clearInterval(h); h = null; left = total; draw(); });
      draw();
    }
  });
})();
