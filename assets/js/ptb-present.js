/* Chế độ TRÌNH CHIẾU cho tivi/máy chiếu:
   - mỗi phần nội dung (một "slide") chiếm trọn chiều cao màn hình, nội dung căn giữa
   - chữ tự phóng theo độ rộng màn hình (tivi 1920px: khoảng gấp 1,8 lần)
   - chuyển phần: phím ← → / PageUp PageDown / bút bấm slide, hoặc nút ◀ ▶ ở góc phải dưới
   - phím + và - chỉnh cỡ chữ; nút 📺 trên thanh đầu để bật/tắt chế độ
   Chỉ bật khi màn hình rộng từ 1100px; điện thoại/máy tính bảng giữ giao diện thường. */
(function () {
  var root = document.documentElement, LAYOUT_W = 1080, MIN_W = 1100;
  var mode = 'tv', adj = 1;
  try { mode = localStorage.getItem('ptbMode') || 'tv'; adj = parseFloat(localStorage.getItem('ptbAdj') || '1') || 1; } catch (e) {}
  function save() { try { localStorage.setItem('ptbMode', mode); localStorage.setItem('ptbAdj', String(adj)); } catch (e) {} }
  function isEl(n) { return n.nodeType === 1 && !/^(SCRIPT|STYLE)$/.test(n.tagName); }
  function has(el, c) { return el.classList && el.classList.contains(c); }

  /* ---- gom nội dung thành các slide ---- */
  function wrapSlides(container) {
    var kids = Array.prototype.filter.call(container.children, isEl), i = 0;
    while (i < kids.length) {
      var el = kids[i], group = [el];
      if (has(el, 'ptb-slide')) { i++; continue; }
      if (has(el, 'ptb-goals') && kids[i + 1] && has(kids[i + 1], 'ptb-roadmap')) group.push(kids[i + 1]);
      else if (has(el, 'section-title')) { var j = i + 1; while (kids[j] && !has(kids[j], 'section-title')) { group.push(kids[j]); j++; } }
      else if ((has(el, 'alert') || has(el, 'quiz-score-banner')) && kids[i + 1]) group.push(kids[i + 1]);
      var w = document.createElement('div'); w.className = 'ptb-slide';
      container.insertBefore(w, group[0]); group.forEach(function (g) { w.appendChild(g); });
      i += group.length;
    }
  }
  function build() {
    document.querySelectorAll('main .tab-pane').forEach(function (p) {
      wrapSlides(p.id === 'pane-quiz' && p.querySelector('.quiz-container') ? p.querySelector('.quiz-container') : p);
    });
  }

  /* ---- tách phần dài hơn một màn hình thành nhiều slide ---- */
  var splits = [];
  function zoomNow() { return parseFloat(getComputedStyle(root).getPropertyValue('--ptb-z')) || 1; }
  function hdrReal() { var h = header(); return h ? h.getBoundingClientRect().height : 48; }
  function unsplit() {
    for (var i = splits.length - 1; i >= 0; i--) {
      var r = splits[i];
      for (var j = r.moved.length - 1; j >= 0; j--) { var m = r.moved[j]; m.parent.insertBefore(m.node, m.parent.childNodes[m.idx] || null); }
      r.made.forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
    }
    splits = [];
    document.querySelectorAll('.ptb-slide[data-ptbfit]').forEach(function (e) { e.style.zoom = ''; e.removeAttribute('data-ptbfit'); });
  }
  function stripIds(n) { if (n.removeAttribute) n.removeAttribute('id'); n.querySelectorAll && n.querySelectorAll('[id]').forEach(function (e) { e.removeAttribute('id'); }); return n; }
  function splitSlide(slide) {
    var z = zoomNow(), cap = window.innerHeight - hdrReal() - 40 * z, gap = 14 * z;
    var kids = Array.prototype.filter.call(slide.children, isEl);
    var natural = kids.reduce(function (a, k) { return a + k.getBoundingClientRect().height + gap; }, -gap);   /* chiều cao nội dung thật, không tính min-height */
    if (natural <= cap) return;
    /* hơi dài hơn màn hình (≤ 1,35 lần): thu nhỏ vừa đủ để cả phần nằm trọn một màn hình, không tách đôi */
    if (natural <= cap * 1.35) { slide.style.zoom = (cap / natural).toFixed(3); slide.setAttribute('data-ptbfit', ''); return; }
    var card = (kids.length === 1 && /(^|\s)(card|exercise-box)(\s|$)/.test(kids[0].className)) ? kids[0] : null;
    var host = card || slide;
    var top = Array.prototype.filter.call(host.children, isEl);
    var head = (card && top[0] && has(top[0], 'card-header')) ? top[0] : null;
    var overhead = Math.max(0, host.getBoundingClientRect().height - top.reduce(function (a, b) { return a + b.getBoundingClientRect().height; }, 0));
    var room = cap - overhead;
    /* danh sách khối; khối nào dài quá một màn hình mà có nhiều khối con thì tách xuống khối con */
    var items = [];
    (function add(list, depth) {
      list.forEach(function (b) {
        var h = b.getBoundingClientRect().height, sub = Array.prototype.filter.call(b.children, isEl);
        if (h > room && depth < 2 && sub.length >= 2 && !/^(TABLE|UL|OL|PRE|svg)$/i.test(b.tagName) && !has(b, 'ptb-flow') && !has(b, 'code-box')) add(sub, depth + 1);
        else items.push({ node: b, h: h + gap });
      });
    })(top, 0);
    if (items.length < 2) return;
    var headH = head ? head.getBoundingClientRect().height + gap : 0;
    var limit = room * 1.1;   /* lấp đầy từng slide, cho phép vượt nhẹ 10% thay vì để slide thưa */
    var chunks = [[]], used = 0;
    items.forEach(function (it) {
      var cur = chunks[chunks.length - 1];
      if (cur.length && used + it.h > limit && !(used < room * 0.5 && used + it.h <= room * 1.5)) {   /* slide đang quá thưa thì nhận thêm khối kế tiếp */
        chunks.push([]); cur = chunks[chunks.length - 1]; used = headH; }
      cur.push(it); used += it.h;
    });
    /* tiêu đề mục không được bị bỏ lại cuối slide: chuyển sang slide sau cùng với nội dung của nó */
    for (var ci = 0; ci < chunks.length - 1; ci++) {
      var cc = chunks[ci];
      while (cc.length > 1 && /^H[1-6]$/.test(cc[cc.length - 1].node.tagName)) chunks[ci + 1].unshift(cc.pop());
    }
    if (chunks.length < 2) return;
    var rec = { moved: [], made: [] }, anchor = slide;
    chunks.slice(1).forEach(function (ch) {
      var ns = document.createElement('div'); ns.className = 'ptb-slide ptb-split';
      var box = ns;
      if (card) { box = card.cloneNode(false); stripIds(box); ns.appendChild(box);
        if (head) { var hc = stripIds(head.cloneNode(true)); var t = hc.querySelector('.card-title') || hc; t.appendChild(document.createTextNode(' (tiếp)')); box.appendChild(hc); } }
      ch.forEach(function (it) {
        var par = it.node.parentNode; rec.moved.push({ node: it.node, parent: par, idx: Array.prototype.indexOf.call(par.childNodes, it.node) });
        box.appendChild(it.node);
      });
      anchor.parentNode.insertBefore(ns, anchor.nextSibling); anchor = ns; rec.made.push(ns);
    });
    splits.push(rec);
  }
  function resplit() {
    if (!active()) return;
    unsplit();
    slides().forEach(splitSlide);
  }

  /* ---- bật/tắt + tính cỡ chữ ---- */
  function active() { return mode === 'tv' && window.innerWidth >= MIN_W; }
  function header() { return document.querySelector('header.ptb-bar') || document.querySelector('header'); }
  function apply() {
    var on = active();
    if (on) {
      var z = Math.max(1, Math.min(2.6, window.innerWidth / LAYOUT_W)) * adj; z = Math.max(0.9, z);
      root.style.setProperty('--ptb-z', z.toFixed(3)); root.setAttribute('data-ptbtv', '');
      var h = header(), hh = h ? h.getBoundingClientRect().height / z : 48;
      root.style.setProperty('--ptb-hh', hh.toFixed(1) + 'px');
      root.style.setProperty('--ptb-sh', Math.max(300, window.innerHeight / z - hh).toFixed(1) + 'px');
    } else { unsplit(); root.removeAttribute('data-ptbtv'); }
    var b = document.querySelector('.ptb-zoom');
    if (b) { b.textContent = active() ? '📺 TV' : (mode === 'tv' ? '📺 TV (cần màn rộng)' : '🖥 Thường'); b.title = 'Bật/tắt chế độ trình chiếu tivi: mỗi phần chiếm trọn màn hình, chữ lớn. Phím ← → chuyển phần, + − chỉnh cỡ chữ.'; }
    hud();
    if (on) { clearTimeout(apply.t); apply.t = setTimeout(function () { resplit(); update(); }, 60); } else update();
  }

  /* ---- điều hướng giữa các slide ---- */
  function slides() {
    return Array.prototype.filter.call(document.querySelectorAll('main .ptb-slide'), function (s) { return s.offsetParent !== null; });
  }
  function current(list) {
    var line = hdrReal() + window.innerHeight * 0.3, idx = 0;
    list.forEach(function (s, i) { if (s.getBoundingClientRect().top <= line) idx = i; });
    return idx;
  }
  function go(dir) {
    var list = slides(); if (!list.length) return;
    var i = current(list), cur = list[i], r = cur.getBoundingClientRect(), view = window.innerHeight - hdrReal();
    if (dir > 0 && r.bottom > window.innerHeight + 40) { window.scrollBy({ top: view * 0.85, behavior: 'smooth' }); return; }
    if (dir < 0 && r.top < hdrReal() - 40) { window.scrollBy({ top: -view * 0.85, behavior: 'smooth' }); return; }
    var t = list[Math.max(0, Math.min(list.length - 1, i + dir))];
    if (t === cur && dir > 0) { var pg = document.querySelector('.lesson-pager'); if (pg) pg.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
    t.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function goEdge(end) { var l = slides(); if (l.length) (end ? l[l.length - 1] : l[0]).scrollIntoView({ behavior: 'smooth', block: 'start' }); }

  /* ---- bảng điều khiển nhỏ góc phải dưới ---- */
  var box, label, raf = 0;
  function hud() {
    if (!box) {
      box = document.createElement('div'); box.className = 'ptb-hud'; box.setAttribute('aria-label', 'Điều khiển trình chiếu');
      box.innerHTML = '<button type="button" data-a="dec" title="Giảm cỡ chữ (-)">A−</button><button type="button" data-a="inc" title="Tăng cỡ chữ (+)">A+</button><span class="sep"></span>' +
        '<button type="button" data-a="prev" title="Phần trước (←)">◀</button><span class="ptb-hud-n">1 / 1</span><button type="button" data-a="next" title="Phần sau (→)">▶</button>';
      document.body.appendChild(box); label = box.querySelector('.ptb-hud-n');
      box.addEventListener('click', function (e) {
        var a = e.target.getAttribute && e.target.getAttribute('data-a'); if (!a) return;
        if (a === 'next') go(1); else if (a === 'prev') go(-1);
        else { adj = Math.max(0.6, Math.min(1.8, adj + (a === 'inc' ? 0.1 : -0.1))); save(); apply(); }
      });
    }
    box.style.display = active() ? 'flex' : 'none';
  }
  function update() {
    if (!label || !active()) return;
    var l = slides(); label.textContent = l.length ? (current(l) + 1) + ' / ' + l.length : '–';
  }
  function schedule() { if (raf) return; raf = requestAnimationFrame(function () { raf = 0; update(); }); }

  document.addEventListener('keydown', function (e) {
    if (!active() || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target; if (t && (/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName) || t.isContentEditable)) return;
    var k = e.key;
    if (k === 'ArrowRight' || k === 'PageDown') { e.preventDefault(); go(1); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); go(-1); }
    else if (k === 'Home') { e.preventDefault(); goEdge(false); }
    else if (k === 'End') { e.preventDefault(); goEdge(true); }
    else if (k === '+' || k === '=') { adj = Math.min(1.8, adj + 0.1); save(); apply(); }
    else if (k === '-' || k === '_') { adj = Math.max(0.6, adj - 0.1); save(); apply(); }
  });
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', function () { apply(); });

  function ready(fn) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn); else fn(); }
  ready(function () {
    build();
    var zb = document.querySelector('.ptb-zoom');
    if (zb) zb.addEventListener('click', function () { mode = (mode === 'tv') ? 'normal' : 'tv'; save(); apply(); });
    document.querySelectorAll('.tab-btn').forEach(function (b) { b.addEventListener('click', function () { setTimeout(function () { resplit(); update(); }, 120); }); });
    apply();
    window.addEventListener('load', apply);
  });
})();
