/* Định dạng code kiểu Visual Studio Code (Dark+) cho toàn bộ code mẫu.
   - textarea trong .code-editor-area: giữ nguyên chức năng sửa/chạy, thêm tô màu + số dòng
   - <pre> tĩnh (câu hỏi trắc nghiệm, ví dụ): tô màu + số dòng
   - .trace-code (mô phỏng từng dòng): tô màu từng dòng khi mô phỏng vẽ lại */
(function () {
  var CONTROL = 'if elif else for while return import from break continue pass try except finally with raise yield assert del match case'.split(' ');
  var KW = 'def class and or not in is None True False global nonlocal as lambda'.split(' ');
  var TYPES = 'int float str bool list dict set tuple bytes complex object'.split(' ');
  var BUILTIN = 'print input len range sum min max abs round sorted reversed enumerate zip map filter type open ord chr isinstance format pow divmod any all id'.split(' ');
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function sp(c, t) { return '<span class="' + c + '">' + esc(t) + '</span>'; }
  function has(a, w) { return a.indexOf(w) !== -1; }

  var RE = /("""[\s\S]*?(?:"""|$)|'''[\s\S]*?(?:'''|$)|[fFrRbBuU]{0,2}"(?:[^"\\\n]|\\.)*"?|[fFrRbBuU]{0,2}'(?:[^'\\\n]|\\.)*'?)|(#[^\n]*)|(@[A-Za-z_][\w.]*)|(\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b)|([A-Za-z_À-ỹ][\w_À-ỹ]*)|(\s+)|([\s\S])/g;

  function str(t) {
    if (!/^[fF]|^[rR][fF]|^[fF][rR]/.test(t)) return sp('tk-str', t);
    var out = '', last = 0, m, r = /\{\{|\}\}|\{[^{}\n]*\}/g;
    while ((m = r.exec(t))) {
      out += sp('tk-str', t.slice(last, m.index));
      out += (m[0] === '{{' || m[0] === '}}') ? sp('tk-str', m[0]) : sp('tk-brace', '{') + highlight(m[0].slice(1, -1)) + sp('tk-brace', '}');
      last = r.lastIndex;
    }
    return out + sp('tk-str', t.slice(last));
  }

  function highlight(code) {
    var out = '', m, prev = '', prevWord = '', re = new RegExp(RE.source, 'g');
    while ((m = re.exec(code))) {
      if (m[1]) { out += str(m[1]); prev = 'str'; }
      else if (m[2]) { out += sp('tk-cm', m[2]); }
      else if (m[3]) { out += sp('tk-fn', m[3]); }
      else if (m[4]) { out += sp('tk-num', m[4]); prev = 'num'; }
      else if (m[5]) {
        var w = m[5], next = code.slice(re.lastIndex).match(/^\s*(.)/), isCall = next && next[1] === '(';
        var c;
        if (has(CONTROL, w)) c = 'tk-ctl';
        else if (has(KW, w)) c = 'tk-kw';
        else if (prevWord === 'def') c = 'tk-fn';
        else if (prevWord === 'class') c = 'tk-type';
        else if (w === 'self') c = 'tk-kw';
        else if (has(TYPES, w)) c = 'tk-type';
        else if (prev === '.') c = isCall ? 'tk-fn' : 'tk-prop';
        else if (has(BUILTIN, w) || isCall) c = 'tk-fn';
        else c = 'tk-var';
        out += sp(c, w); prev = 'w'; prevWord = w;
      }
      else if (m[6]) { out += esc(m[6]); }
      else { out += sp(/[=+\-*\/%<>!&|^~]/.test(m[7]) ? 'tk-op' : 'tk-pun', m[7]); prev = m[7]; if (m[7] !== '.') prevWord = ''; }
    }
    return out;
  }
  window.ptbHighlight = highlight;

  /* ---------- textarea -> trình soạn thảo ---------- */
  function lineNums(n) { var s = ''; for (var i = 1; i <= n; i++) s += i + '\n'; return s; }

  function enhanceTextarea(ta) {
    if (ta.dataset.ptbEd) return; ta.dataset.ptbEd = '1';
    var ed = document.createElement('div'); ed.className = 'ptb-ed' + (ta.readOnly ? ' is-ro' : '');
    var gut = document.createElement('div'); gut.className = 'ptb-gut'; gut.setAttribute('aria-hidden', 'true');
    var stack = document.createElement('div'); stack.className = 'ptb-stack';
    var pre = document.createElement('pre'); pre.className = 'ptb-hl'; pre.setAttribute('aria-hidden', 'true');
    ta.parentNode.insertBefore(ed, ta); ed.appendChild(gut); ed.appendChild(stack); stack.appendChild(pre); stack.appendChild(ta);
    ta.setAttribute('wrap', 'off'); ta.setAttribute('spellcheck', 'false'); ta.setAttribute('autocapitalize', 'off'); ta.setAttribute('autocomplete', 'off');
    ta.style.minHeight = ''; ta.style.height = ''; ta.classList.add('ptb-ta');
    function refresh() {
      var v = ta.value;
      pre.innerHTML = highlight(v) + (v.slice(-1) === '\n' ? ' ' : '');
      gut.textContent = lineNums(v.split('\n').length);
    }
    ta.addEventListener('input', refresh);
    var d = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value');
    Object.defineProperty(ta, 'value', { get: function () { return d.get.call(ta); }, set: function (x) { d.set.call(ta, x); refresh(); }, configurable: true });
    ta.addEventListener('keydown', function (e) {
      if (ta.readOnly) return;
      var s = ta.selectionStart, t = ta.selectionEnd, v = d.get.call(ta);
      if (e.key === 'Tab') {
        e.preventDefault(); ta.setRangeText('    ', s, t, 'end'); refresh();
      } else if (e.key === 'Enter' && s === t) {
        var ls = v.lastIndexOf('\n', s - 1) + 1, line = v.slice(ls, s), ind = line.match(/^ */)[0];
        if (/:\s*$/.test(line)) ind += '    ';
        e.preventDefault(); ta.setRangeText('\n' + ind, s, t, 'end'); refresh();
      }
    });
    refresh();
  }

  /* ---------- <pre> tĩnh ---------- */
  function enhancePre(pre) {
    if (pre.dataset.ptbPre || pre.classList.contains('ptb-out') || pre.classList.contains('ptb-hl') || pre.closest('.ptb-flow,.terminal-output')) return;
    pre.dataset.ptbPre = '1';
    var code = pre.textContent.replace(/\n$/, '');
    pre.removeAttribute('style'); pre.classList.add('ptb-code');
    pre.innerHTML = '<span class="ptb-gut" aria-hidden="true">' + lineNums(code.split('\n').length) + '</span><code>' + highlight(code) + '</code>';
  }

  /* ---------- mô phỏng từng dòng ---------- */
  function enhanceTrace(root) {
    root.querySelectorAll('.trace-line').forEach(function (row) {
      if (row.dataset.ptbTr) return; row.dataset.ptbTr = '1';
      var ln = row.querySelector('.ln'), text = '';
      Array.prototype.slice.call(row.childNodes).forEach(function (n) { if (n !== ln) { text += n.textContent; row.removeChild(n); } });
      var c = document.createElement('span'); c.className = 'ptb-tl-code'; c.innerHTML = highlight(text); row.appendChild(c);
    });
  }
  function watchTrace(el) {
    if (el.dataset.ptbWatch) return; el.dataset.ptbWatch = '1'; el.classList.add('ptb-trace');
    var busy = false;
    new MutationObserver(function () { if (busy) return; busy = true; enhanceTrace(el); busy = false; }).observe(el, { childList: true, subtree: true });
    enhanceTrace(el);
  }

  function init() {
    document.querySelectorAll('.code-editor-area textarea').forEach(enhanceTextarea);
    document.querySelectorAll('pre').forEach(enhancePre);
    document.querySelectorAll('.trace-code').forEach(watchTrace);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
