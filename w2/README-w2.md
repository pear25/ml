# Week 2 — More math, NumPy, first model

> **Goal:** Finish linear algebra, start calculus, and train your first model (linear regression from scratch).
> **Time budget:** ~12 hours
> **Dates:** Mon May 18 – Sun May 24, 2026

---

## Days 1–3 (~5 hrs) — Finish linear algebra; start calculus

- [x] Watch [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) chapters 6–9 (determinants; inverses; rank; dot/cross products)
- [x] Watch chapters 10–14 (change of basis; eigenvectors; abstract vector spaces)
- [ ] Rewatch and understand chapters 10-14


- [x] Watch [3Blue1Brown — Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr), chapters 1–4 (derivatives, chain rule basics)
- [ ] Add notes to `learnings.md` capturing key intuitions (eigenvectors, determinants, derivatives)

## Days 4–5 (~4 hrs) — Linear regression from scratch

- [ ] Generate synthetic data: `y = 3x + 2 + Gaussian noise`
- [ ] Write the mean-squared-error loss function in NumPy
- [ ] Derive the gradient of MSE w.r.t. weight and bias on paper
- [ ] Implement gradient descent in pure NumPy (no scikit-learn)
- [ ] Plot the loss curve and the fitted line vs the true line
- [ ] Push the notebook to `w2/` with a README explaining gradient descent in your own words

## Days 6–7 (~3 hrs) — ML vocabulary

- [ ] Read [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) parts 1 and 2
- [ ] Read chapters 1–2 of Burkov's *The Hundred-Page Machine Learning Book*
- [ ] Add short glossary to `learnings.md` (features, labels, training/validation/test, overfitting, etc.)

---

## ✅ Checkpoint — Can you?

- [ ] Linear regression converges within 100 steps to within 1% of the true parameters
- [ ] Notebook is in the repo with a clear README
- [ ] You can explain (without notes) what gradient descent is doing geometrically

If yes to all three → move on to Week 3.
If not → don't push forward yet. Slow down, re-derive the MSE gradient on paper, and re-run the experiment until it converges.

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

*Part of the [6-Month AI / ML Learning Plan](../ml_learning_plan.md). Previous: [Week 1 — Setup and NumPy fluency](../w1/README-w1.md). Next: Week 3 — Calculus and logistic regression.*
