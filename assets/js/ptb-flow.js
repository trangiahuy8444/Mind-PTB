/* Bộ mô phỏng sơ đồ khối chạy từng bước. Dữ liệu nằm trong <script type="application/json"> của mỗi .ptb-flow */
(function () {
  function init(root) {
    var holder = root.querySelector('script[type="application/json"]');
    if (!holder) return;
    var data = JSON.parse(holder.textContent);
    var sel = root.querySelector('.ptb-sc'), bNext = root.querySelector('.go'),
        bPrev = root.querySelector('.prev'), bReset = root.querySelector('.reset'),
        lab = root.querySelector('.ptb-step'), note = root.querySelector('.ptb-note'),
        vars = root.querySelector('.ptb-vars'), out = root.querySelector('.ptb-out');
    var nodes = {};
    root.querySelectorAll('[data-node]').forEach(function (g) { nodes[g.getAttribute('data-node')] = g; });
    var sc = 0, st = -1;
    var cv = root.querySelector('.ptb-codeview'), rows = [];
    function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
    if (cv && data.code) {
      data.code.split('\n').forEach(function (ln, i) {
        var r = document.createElement('div'); r.className = 'ptb-cl';
        r.innerHTML = '<span class="ptb-cn">' + (i + 1) + '</span><span class="ptb-ct">' + (window.ptbHighlight ? window.ptbHighlight(ln) : esc(ln)) + '</span>';
        cv.appendChild(r); rows.push(r);
      });
    } else if (cv) { var h = cv.previousElementSibling; if (h) h.style.display = 'none'; cv.style.display = 'none'; }
    function mark(s) {
      rows.forEach(function (r) { r.classList.remove('on'); });
      if (!s || !rows.length) return;
      var l = s.l !== undefined ? s.l : (data.map ? data.map[s.n] : null);
      if (l == null) return;
      var a = Array.isArray(l) ? l[0] : l, b = Array.isArray(l) ? l[1] : l;
      for (var i = a; i <= b; i++) if (rows[i - 1]) rows[i - 1].classList.add('on');
      var f = rows[a - 1];
      if (f && cv.scrollHeight > cv.clientHeight) {
        var top = f.offsetTop, bot = rows[Math.min(b, rows.length) - 1].offsetTop + f.offsetHeight;
        if (top < cv.scrollTop + 8) cv.scrollTop = Math.max(0, top - 8);
        else if (bot > cv.scrollTop + cv.clientHeight - 8) cv.scrollTop = bot - cv.clientHeight + 8;
      }
    }
    data.scenarios.forEach(function (s, i) {
      var o = document.createElement('option'); o.value = i; o.textContent = s.name; sel.appendChild(o);
    });
    function render() {
      var steps = data.scenarios[sc].steps;
      Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove('on'); });
      if (st < 0) {
        note.textContent = 'Bấm ▶ Bước tiếp để bắt đầu chạy sơ đồ.';
        vars.textContent = ''; out.textContent = ''; mark(null);
      } else {
        var s = steps[st];
        if (nodes[s.n]) nodes[s.n].classList.add('on');
        mark(s);
        note.textContent = s.t;
        vars.textContent = s.v || '';
        var lines = [];
        for (var i = 0; i <= st; i++) if (steps[i].o != null) lines.push(steps[i].o);
        out.textContent = lines.join('\n');
      }
      lab.textContent = 'Bước ' + (st + 1) + '/' + steps.length;
      bPrev.disabled = st < 0; bNext.disabled = st >= steps.length - 1;
    }
    sel.addEventListener('change', function () { sc = +sel.value; st = -1; render(); });
    bNext.addEventListener('click', function () { if (st < data.scenarios[sc].steps.length - 1) { st++; render(); } });
    bPrev.addEventListener('click', function () { if (st >= 0) { st--; render(); } });
    bReset.addEventListener('click', function () { st = -1; render(); });
    render();
  }
  function boot() { document.querySelectorAll('.ptb-flow').forEach(init); }
  /* chờ DOMContentLoaded để ptb-code.js (tô màu cú pháp) đã sẵn sàng */
  if (document.readyState === 'complete') boot(); else document.addEventListener('DOMContentLoaded', boot);
})();
