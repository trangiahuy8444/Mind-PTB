/**
 * MINDX TECHNOLOGY SCHOOL - PYTHON PROGRAMMING (TT-C4K-PTB30)
 * UNIFIED JAVASCRIPT UTILITIES & ENGINES (common.js)
 */

document.addEventListener("DOMContentLoaded", function () {
  initTabs();
  initNavHighlight();
  initCopyButtons();
});

// ==============================================================================
// 1. TABS SWITCHER
// ==============================================================================
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const tabId = btn.getAttribute("data-tab");
      switchTab(tabId);
    });
  });
}

function switchTab(tabId) {
  if (!tabId) return;

  // Deactivate all tab buttons
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-tab") === tabId);
  });

  // Toggle tab panes
  document.querySelectorAll(".tab-pane").forEach(pane => {
    const paneId = pane.id.replace("pane-", "");
    if (paneId === tabId) {
      pane.hidden = false;
      pane.classList.add("active");
    } else {
      pane.hidden = true;
      pane.classList.remove("active");
    }
  });

  // Scroll to top of tab pane smoothly
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ==============================================================================
// 2. NAV HIGHLIGHTER
// ==============================================================================
function initNavHighlight() {
  const nav = document.querySelector(".course-quick-nav");
  if (!nav) return;
  if (nav.querySelector("a.active")) return;

  const currentPath = decodeURIComponent(window.location.pathname).replace(/\/$/, "");
  nav.querySelectorAll("a").forEach(link => {
    const href = link.getAttribute("href");
    if (!href) return;
    try {
      const linkPath = decodeURIComponent(new URL(href, window.location.href).pathname).replace(/\/$/, "");
      if (linkPath === currentPath) {
        link.classList.add("active");
      }
    } catch (e) {}
  });
}

// ==============================================================================
// 3. CODE COPY BUTTON
// ==============================================================================
function initCopyButtons() {
  document.querySelectorAll(".btn-copy").forEach(btn => {
    btn.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const targetElem = document.getElementById(targetId);
      if (!targetElem) return;

      const codeText = targetElem.value !== undefined ? targetElem.value : targetElem.innerText;
      navigator.clipboard.writeText(codeText).then(() => {
        const originalText = this.innerHTML;
        this.innerHTML = "✓ Đã sao chép!";
        this.style.background = "#10b981";
        this.style.color = "#ffffff";
        setTimeout(() => {
          this.innerHTML = originalText;
          this.style.background = "";
          this.style.color = "";
        }, 2000);
      });
    });
  });
}

// ==============================================================================
// 4. SKULPT IN-BROWSER PYTHON RUNNER
// ==============================================================================
function runPythonCode(editorId, outputId) {
  const outputEl = document.getElementById(outputId);
  if (!outputEl) return;

  if (typeof Sk === "undefined") {
    outputEl.innerHTML = '<span style="color:#ef4444;">⚠️ Lỗi: Trình biên dịch Skulpt Python chưa được tải. Vui lòng kiểm tra kết nối mạng và F5 lại trang!</span>';
    return;
  }

  const editor = document.getElementById(editorId);
  if (!editor) return;

  const prog = editor.value !== undefined ? editor.value : editor.innerText;
  outputEl.innerHTML = '<span style="color:#38bdf8;">⚡ Đang chạy chương trình...</span>\n';

  function outf(text) {
    // Append printed text
    outputEl.appendChild(document.createTextNode(text));
  }

  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined) {
      throw "File not found: '" + x + "'";
    }
    return Sk.builtinFiles["files"][x];
  }

  // Clear output on fresh run
  outputEl.innerHTML = '';

  Sk.pre = outputId;
  Sk.configure({
    output: outf,
    read: builtinRead,
    inputfun: function (promptMsg) {
      return window.prompt(promptMsg || "Nhập giá trị từ bàn phím:");
    },
    inputfunTakesPrompt: true,
    __future__: Sk.python3
  });

  const myPromise = Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody("<stdin>", false, prog, true);
  });

  myPromise.then(
    function (mod) {
      outputEl.innerHTML += '\n<span style="color:#10b981; font-weight:bold;">\n[Chương trình đã kết thúc thành công]</span>';
    },
    function (err) {
      outputEl.innerHTML += '\n<span style="color:#ef4444; font-weight:bold;">\n' + err.toString() + '</span>';
    }
  );
}

// ==============================================================================
// 5. INTERACTIVE QUIZ ENGINE
// ==============================================================================
const quizStats = {
  total: 0,
  answered: 0,
  correct: 0
};

function selectQuizOption(cardId, optionIndex, isCorrect, explanation) {
  const card = document.getElementById(cardId);
  if (!card) return;

  // Check if already answered
  if (card.dataset.answered === "true") return;
  card.dataset.answered = "true";

  const options = card.querySelectorAll(".quiz-option");
  const feedback = card.querySelector(".quiz-feedback");

  // Disable all radio buttons
  options.forEach((opt, idx) => {
    const radio = opt.querySelector('input[type="radio"]');
    if (radio) radio.disabled = true;

    if (idx === optionIndex) {
      opt.classList.add(isCorrect ? "correct" : "wrong");
    } else if (!isCorrect && opt.dataset.correct === "true") {
      // Highlight the correct answer in green
      opt.classList.add("correct");
    }
  });

  // Show feedback
  if (feedback) {
    feedback.classList.add("show");
    feedback.classList.add(isCorrect ? "success" : "error");
    feedback.innerHTML = `<strong>${isCorrect ? "✓ Chính xác!" : "✗ Chưa chính xác!"}</strong> ${explanation}`;
  }

  // Update card border
  card.classList.add(isCorrect ? "answered-correct" : "answered-wrong");

  // Update score
  if (!quizStats[cardId]) {
    quizStats[cardId] = true;
    quizStats.answered++;
    if (isCorrect) quizStats.correct++;
  }

  const scoreEl = document.getElementById("quiz-score-display");
  if (scoreEl) {
    scoreEl.innerText = `${quizStats.correct} / ${quizStats.answered}`;
  }
}
