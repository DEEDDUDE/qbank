// qbank study site — vanilla JS, hash routing, tap-to-reveal.
// No framework, no build step for this file itself; site/build.py only
// produces data.json and copies this file as-is into dist/.

let DATA = null;

// In-memory only, per CLAUDE.md ("no accounts, no backend") — resets on reload.
const pickedByQid = {};
const revealedQids = new Set();

const STATUS_LABEL = {
  verified: "Verified",
  conflict: "Conflict",
  external: "External",
  "not-in-source": "Not in source",
  "needs-eye": "Needs a look",
};

function el(tag, attrs = {}, children = []) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") node.className = v;
    else if (k === "html") node.innerHTML = v;
    else node.setAttribute(k, v);
  }
  for (const child of [].concat(children)) {
    if (child == null) continue;
    node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
  }
  return node;
}

function statusBadge(status) {
  return el("span", { class: `badge badge-${status}` }, STATUS_LABEL[status] || status);
}

function link(hash, text, extraClass) {
  return el("a", { href: `#${hash}`, class: extraClass || "" }, text);
}

async function init() {
  const res = await fetch("data.json");
  DATA = await res.json();
  window.addEventListener("hashchange", render);
  render();
}

function parseHash() {
  return location.hash
    .replace(/^#\/?/, "")
    .split("/")
    .filter(Boolean)
    .map(decodeURIComponent);
}

function render() {
  const app = document.getElementById("app");
  app.innerHTML = "";
  const parts = parseHash();

  if (parts.length === 0) return renderCourseList(app);

  const course = DATA.courses.find((c) => c.id === parts[0]);
  if (!course) return renderNotFound(app, "course", parts[0]);
  if (parts.length === 1) return renderTabList(app, course);

  const tab = course.tabs.find((t) => t.id === parts[1]);
  if (!tab) return renderNotFound(app, "tab", parts[1]);
  if (parts.length === 2) return renderQuestionList(app, course, tab);

  const q = tab.questions.find((q) => q.id === parts[2]);
  if (!q) return renderNotFound(app, "question", parts[2]);
  renderQuestion(app, course, tab, q);
}

function renderNotFound(app, kind, id) {
  app.appendChild(el("p", {}, `No such ${kind}: ${id}`));
  app.appendChild(link("/", "Back to courses"));
}

function renderCourseList(app) {
  app.appendChild(el("h1", {}, "qbank"));
  const list = el("ul", { class: "list" });
  for (const course of DATA.courses) {
    const totalQ = course.tabs.reduce((n, t) => n + t.questions.length, 0);
    list.appendChild(
      el("li", {}, link(`/${course.id}`, `${course.id} — ${totalQ} questions`))
    );
  }
  app.appendChild(list);
}

function countsLine(counts) {
  const order = ["verified", "conflict", "external", "not-in-source", "needs-eye"];
  return order
    .filter((k) => counts[k])
    .map((k) => `${STATUS_LABEL[k]} ${counts[k]}`)
    .join(" · ");
}

function renderTabList(app, course) {
  app.appendChild(el("p", {}, link("/", "← courses")));
  app.appendChild(el("h1", {}, course.id));
  const list = el("ul", { class: "list" });
  for (const tab of course.tabs) {
    const item = el("li", {}, [
      link(`/${course.id}/${tab.id}`, `${tab.id} — ${tab.questions.length} questions`),
      el("div", { class: "meta" }, countsLine(tab.counts)),
    ]);
    if (!tab.complete) {
      item.appendChild(el("div", { class: "note-inline" }, `Partial batch. ${tab.covers}`));
    }
    list.appendChild(item);
  }
  app.appendChild(list);
}

function renderQuestionList(app, course, tab) {
  app.appendChild(el("p", {}, link(`/${course.id}`, `← ${course.id}`)));
  app.appendChild(el("h1", {}, `${course.id} / ${tab.id}`));
  if (!tab.complete) {
    app.appendChild(
      el("p", { class: "note-inline" }, `This tab is a partial batch. ${tab.covers}`)
    );
  }
  app.appendChild(el("p", { class: "meta" }, countsLine(tab.counts)));

  const list = el("ul", { class: "list" });
  for (const q of tab.questions) {
    const preview = q.stem.split("\n")[0].slice(0, 80);
    list.appendChild(
      el("li", {}, [
        statusBadge(q.status),
        " ",
        link(`/${course.id}/${tab.id}/${q.id}`, `${q.id} — ${preview}`),
      ])
    );
  }
  app.appendChild(list);
}

function answerLetters(answerField) {
  if (!answerField) return [];
  return answerField
    .split(",")
    .map((s) => s.trim().toLowerCase())
    .filter((s) => /^[a-z]$/.test(s));
}

function renderOptions(container, q, onPick) {
  const list = el("ol", { class: "options" });
  for (const opt of q.options) {
    const item = el(
      "li",
      { class: "option", "data-letter": opt.letter },
      `${opt.letter}) ${opt.text}`
    );
    item.addEventListener("click", () => onPick(opt.letter));
    list.appendChild(item);
  }
  container.appendChild(list);
}

function markOptions(container, q, pickedLetter) {
  const correct = new Set(
    q.status === "not-in-source" || q.status === "needs-eye" ? [] : answerLetters(q.answer)
  );
  const claimed = q.status === "conflict" ? new Set(answerLetters(q.claimed)) : new Set();
  container.querySelectorAll(".option").forEach((node) => {
    const letter = node.getAttribute("data-letter");
    if (correct.has(letter)) node.classList.add("correct");
    if (claimed.has(letter) && !correct.has(letter)) node.classList.add("claimed-wrong");
    if (letter === pickedLetter) node.classList.add("picked");
  });
}

function renderImages(container, images) {
  if (!images.length) return;
  const wrap = el("div", { class: "images" });
  for (const src of images) {
    wrap.appendChild(el("img", { src, alt: "source crop", loading: "lazy" }));
  }
  container.appendChild(wrap);
}

function renderResolution(container, q) {
  const box = el("div", { class: `resolution resolution-${q.status}` });
  box.appendChild(statusBadge(q.status));

  if (q.status === "verified") {
    box.appendChild(el("p", { class: "answer-line" }, formatAnswerLine(q, q.answer)));
    if (q.basis) box.appendChild(el("p", { class: "basis" }, q.basis));
    if (q.evidence) box.appendChild(el("blockquote", { class: "evidence" }, q.evidence));
  } else if (q.status === "conflict") {
    box.appendChild(
      el("p", { class: "answer-line source-wins" }, `Source: ${formatAnswerLine(q, q.answer)}`)
    );
    box.appendChild(
      el("p", { class: "answer-line claimed-line" }, `Circulating file claimed: ${formatAnswerLine(q, q.claimed)}`)
    );
    if (q.basis) box.appendChild(el("p", { class: "basis" }, q.basis));
    if (q.evidence) box.appendChild(el("blockquote", { class: "evidence" }, q.evidence));
  } else if (q.status === "external") {
    box.appendChild(
      el(
        "p",
        { class: "warning" },
        "Not from your lecturer's material — settled outside knowledge, included because your exam may still test it."
      )
    );
    box.appendChild(el("p", { class: "answer-line" }, formatAnswerLine(q, q.answer)));
    if (q.evidence) box.appendChild(el("blockquote", { class: "evidence" }, q.evidence));
  } else if (q.status === "not-in-source") {
    box.appendChild(
      el("p", { class: "warning" }, "Not answerable from your course material — a real gap, not a failure.")
    );
  } else if (q.status === "needs-eye") {
    box.appendChild(
      el("p", { class: "warning" }, "Unresolved — this one needs a human look at the source image.")
    );
  }

  if (q.note) box.appendChild(el("p", { class: "note-inline" }, q.note));
  renderImages(box, q.images);

  if (q.seen || q.noteJobA) {
    const details = el("details", { class: "provenance" });
    details.appendChild(el("summary", {}, "Provenance"));
    if (q.seen) details.appendChild(el("p", {}, `Seen in: ${q.seen}`));
    if (q.noteJobA) details.appendChild(el("p", {}, q.noteJobA));
    box.appendChild(details);
  }

  container.appendChild(box);
}

function formatAnswerLine(q, field) {
  if (!field) return "(no answer recorded)";
  if (q.form !== "mcq") return field;
  const letters = answerLetters(field);
  if (!letters.length) return field;
  const parts = letters.map((l) => {
    const opt = q.options.find((o) => o.letter === l);
    return opt ? `${l}) ${opt.text}` : l;
  });
  return parts.join("; ");
}

function renderQuestion(app, course, tab, q) {
  app.appendChild(el("p", {}, link(`/${course.id}/${tab.id}`, `← ${course.id} / ${tab.id}`)));
  app.appendChild(el("h1", {}, q.id));
  app.appendChild(el("p", { class: "stem" }, q.stem));

  const alreadyRevealed = revealedQids.has(q.id);

  if (q.form === "mcq" && q.options.length) {
    renderOptions(app, q, (letter) => reveal(letter));
  }

  let revealBtn = null;
  if (!alreadyRevealed) {
    revealBtn = el("button", { class: "reveal-btn" }, "Reveal answer");
    revealBtn.addEventListener("click", () => reveal(null));
    app.appendChild(revealBtn);
  }

  const resolutionHost = el("div");
  app.appendChild(resolutionHost);

  function reveal(pickedLetter) {
    if (revealedQids.has(q.id)) return;
    revealedQids.add(q.id);
    pickedByQid[q.id] = pickedLetter || null;
    if (q.form === "mcq") markOptions(app, q, pickedLetter);
    renderResolution(resolutionHost, q);
    if (revealBtn) revealBtn.remove();
  }

  // Re-render already-revealed state on back/forward nav within a session.
  if (alreadyRevealed) {
    if (q.form === "mcq") markOptions(app, q, pickedByQid[q.id]);
    renderResolution(resolutionHost, q);
  }
}

init();
