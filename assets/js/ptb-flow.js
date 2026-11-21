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
    data.scenarios.forEach(function (s, i) {
      var o = document.createElement('option'); o.value = i; o.textContent = s.name; sel.appendChild(o);
    });
    function render() {
      var steps = data.scenarios[sc].steps;
      Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove('on'); });
      if (st < 0) {
        note.textContent = 'Bấm ▶ Bước tiếp để bắt đầu chạy sơ đồ.';
        vars.textContent = ''; out.textContent = '';
      } else {
        var s = steps[st];
        if (nodes[s.n]) nodes[s.n].classList.add('on');
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
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
