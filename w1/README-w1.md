# Week 1 — Setup and NumPy fluency

> **Goal:** Get tooling sharp, environment ready, and start the linear-algebra refresh.
> **Time budget:** ~12 hours
> **Dates:** Mon May 11 – Sun May 17, 2026

---

## Day 1 (~2 hrs) — Environment & repo

- [x] Install `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [x] Create `ml-journey` directory and `cd` into it
- [x] Run `uv init` and `uv python pin 3.12`
- [x] Install core deps: `uv add numpy pandas matplotlib jupyter ipykernel`
- [x] Initialize git repo and push to GitHub as `ml-journey`
- [x] Add `.venv/` to `.gitignore`; commit `pyproject.toml` and `uv.lock`
- [x] Install VS Code with Python + Jupyter extensions (or set up JupyterLab)
- [x] First commit: a `README.md` describing the goal of the repo

## Days 2–4 (~6 hrs) — NumPy fluency

- [x] Work through the official NumPy "absolute beginners" guide
- [x] Work through "NumPy: the absolute basics for beginners"
- [x] Complete exercises 1–50 of the [100 NumPy exercises](https://github.com/rougier/numpy-100) repo
- [x] Write a notebook summarizing the operations you learned (broadcasting, indexing, reshaping)
- [x] Commit notebook to repo under `week-01/`

## Days 5–7 (~4 hrs) — Linear algebra refresh

- [x] Watch [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), chapters 1–2 (vectors; linear combinations and span)
- [x] Watch chapter 3 (linear transformations and matrices)
- [x] Watch chapter 4 (matrix multiplication as composition)
- [x] Watch chapter 5 (three-dimensional linear transformations)
- [x] Pause and re-derive examples on paper as you watch
- [x] Add a `notes.md` to `week-01/` capturing the key intuitions

---

## ✅ Checkpoint — Can you?

- [x] Without looking it up, write NumPy code to multiply two matrices
- [x] Without looking it up, transpose a matrix and take a dot product
- [x] Explain in your own words what a matrix multiplication does to a vector geometrically

If yes to all three → move on to Week 2.
If not → don't push forward yet. Re-watch the relevant 3B1B chapter and re-do the NumPy exercise that failed. Speed kills more often than slowness in this plan.

---

## 📓 Reflection (fill in at end of week)

**What clicked:**
<!-- e.g. "x finally made sense" -->

**What's still fuzzy:**
<!-- e.g. "still shaky on what x actually mean" -->

**Time actually spent:** ___ hrs (target: 12)

**Carry-over to next week:**
<!-- anything you didn't finish or want to revisit -->

---

*Part of the [6-Month AI / ML Learning Plan](./ml_learning_plan.docx). Next: [Week 2 — More math, NumPy, first model](./week-02-checkpoint.md)*