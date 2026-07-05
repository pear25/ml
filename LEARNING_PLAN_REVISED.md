# ML Learning Plan — Revised

> **Updated:** 14 June 2026 · **Status:** Week 2 (finishing) · **Repo:** `ml-journey`

A recalibration of the original 6-month plan. The curriculum content and sequence are unchanged; what changed is the **cadence and structure**, to fix an accountability problem (three weeks stalled at W2 on a schedule that assumed twice the available hours).

---

## What changed and why

The original plan targeted **12 hrs/week across six slots**, four of them weeknight evenings starting at 8pm. Evidence said that didn't get executed — deep cognitive work after a workday is where it stalled. Three structural fixes:

1. **Lower the bar to one that gets cleared.** 12 → **6.5 hrs/week**. Raise it only after three consecutive 100% weeks.
2. **Firewall deep work to the weekend.** Two coding-first weekend blocks carry the load, when you're fresh. No deep work on weeknights.
3. **Batch by mode, not just topic.** One theme per week. Coding in the morning blocks; all reading/journaling/README writing herded into one low-load slot.

Because the pace halved, the original 24 content-weeks now stretch in calendar time. **Week numbers below track the content sequence (W2–W24), not calendar weeks.** Expect roughly 1.5–2 calendar weeks per content-week at 6.5 hrs.

---

## Weekly cadence — 6.5 hrs, four sessions

| When | Type | Length | What happens |
|---|---|---|---|
| **Tue 8:00–8:30pm** | Light review | 0.5h | Keep material warm. No new code. Re-read notes / one d2l passage / flag fuzzy bits. |
| **Sat 10:00am–12:30pm** | Deep work | 2.5h | Primary block. ≥30 min coding before any video. |
| **Sun 10:00am–12:00pm** | Deep work | 2.0h | Second block. Continue Saturday's thread. |
| **Sun 9:00–10:30pm** | Review + journal | 1.5h | Reading, journal entry, README, end-of-week check. |

**The accountability gate:** a deep-work session counts only if it ends in a **git push to `ml-journey`**. No push = no progress. (Tuesday review is exempt — a one-line journal note counts.)

**If you defend only one slot, defend Saturday morning.** It's the single biggest predictor of whether this sticks.

---

## Operating principles (unchanged)

- **Code more than you read** — ≥30 min coding per 1 hr of video.
- **Math on demand** — introduce prerequisites when the task needs them, not upfront.
- **Learn in public** — push the journal every session.
- **Break things deliberately** — set `lr` too high to watch divergence; vary noise and sample size. Beats passively running provided code.
- **Use AI as a study aid** — ask good questions, restate concepts, verify answers.

**Tooling:** `uv` (not pip/conda), Python 3.12 pinned, `uv add`/`uv run`/`uv sync`. Commit `pyproject.toml` + `uv.lock`; gitignore `.venv/`.
**Hardware:** CPU for the first two months, then Google Colab free tier; optionally Colab Pro or RunPod when GPU is needed.

---

## End-of-week check (Sunday journal)

- Did each deep-work session end in a push?
- Hours actually spent vs target (6.5)?
- What clicked / what's still fuzzy?
- What rolls over to next week?

---

# Month 1 — Foundations (current)

## Week 2 (finishing) — Linear regression from scratch
**Theme:** Close out the W2 implementation you're mid-way through.

- Finish the pure-NumPy linear regression: synthetic data (`y = 3x + 2 + Gaussian noise`), `predict`, MSE loss, gradient computation (chain rule), gradient-descent update loop.
- Track dimensions explicitly; understand the matrix form `ŷ = Xw + b` and the `@` operator.
- **Break it on purpose:** set `lr=1.5` to watch divergence; increase noise σ; increase sample size; observe each effect.
- Plot the fitted line over the data and the loss curve over iterations.
- Finish reading **d2l.ai §3.1**.

**Push-gate deliverable:** plots + a README explaining the model, loss, and what the experiments showed → committed to `ml-journey`.
**Resources:** d2l.ai §3.1 · StatQuest (gradient descent) · Karpathy micrograd (for the gradient concept) · r2d3.us visual intro · Burkov ch 1–2.

## Week 3 — Calculus + logistic regression from scratch
**Theme:** The math you need for classification, then a second from-scratch model.

- **3B1B Essence of Calculus ch 5–11** (multi-variable intuition, partial derivatives properly named, the chain rule you've been using implicitly).
- Chain-rule drills — a small notebook of worked derivatives.
- Implement **logistic regression from scratch**: sigmoid + binary cross-entropy (BCE) loss, gradient descent, on the **Iris** dataset, with **L2 regularization**.
- StatQuest probability for the BCE/MLE intuition.

**Push-gate deliverable:** derivative-drill notebook + working logistic-regression classifier + README → committed.
**Resources:** 3B1B Calculus ch 5–11 · StatQuest (probability, logistic regression) · CS229 notes (logistic regression derivation).

## Week 4 — Micrograd + a real neural net
**Theme:** Backprop from first principles, then your first multi-layer net.

- Work through **Karpathy's micrograd** video; reimplement the autograd engine yourself (a `Value` class with backward).
- Verify your gradients against analytic ones; make the tests pass.
- Build a small **neural net on `make_moons`** (non-linear decision boundary).
- Plot the decision boundary.

**Push-gate deliverable:** `micrograd` reimplemented with passing tests + trained net + decision-boundary plot → committed.
**Resources:** Karpathy "The spelled-out intro to neural networks and backpropagation: building micrograd."

> **Milestone (lighthouse, ~Sep 13):** Foundations + early frameworks solid — regression from scratch, micrograd, a neural net, plus PyTorch & classical ML below.

---

# Month 2 — Frameworks + classical ML

## Week 5 — PyTorch basics
**Theme:** Move off raw NumPy onto a real framework.

- **PyTorch:** "Learn the Basics" + the 60-Minute Blitz.
- Re-implement the **W4 neural net** in `nn.Module` + `torch.optim` — same model, framework idioms.
- Build an **MNIST MLP**, target **>97%** test accuracy.
- Be able to describe `nn.Module`, `DataLoader`, optimizer, scheduler.

**Push-gate deliverable:** MNIST MLP >97% + README describing the PyTorch building blocks → committed.

## Week 6 — CNNs and computer vision
**Theme:** Convolutions and the tricks that make them train.

- CNN theory from **CS231n**.
- **CNN on CIFAR-10**, target **>75%** test accuracy with **data augmentation + batchnorm + dropout**.
- Read the **AlexNet** paper (Krizhevsky 2012).

**Push-gate deliverable:** CIFAR-10 CNN >75% with augmentation + AlexNet paper note → committed.

## Week 7 — Classical ML
**Theme:** The non-deep-learning toolbox that still wins on tabular data.

- **scikit-learn** tutorial; implement/apply decision tree, random forest, GBM, k-means, PCA.
- Make a **Kaggle submission** (Titanic or House Prices) using **XGBoost**.
- Understand the **bias–variance tradeoff** and why gradient boosting dominates tabular.

**Push-gate deliverable:** ≥1 Kaggle submission + a short bias–variance writeup → committed.

## Week 8 — makemore (language modeling on-ramp)
**Theme:** Bridge from MLPs toward sequence models.

- **Karpathy makemore parts 1–3** (intro / MLP / activations + BatchNorm).
- Build the character-level model; understand the training dynamics parts 2–3 dig into.

**Push-gate deliverable:** makemore reimplemented through part 3 + notes on what activations/BN fixed → committed.

> **Checkpoint:** You've built a CNN, an MLP language model, and classical models, and made a Kaggle submission. Review and patch gaps before transformer weeks.

---

# Month 3 — Transformers + LLMs

## Week 9 — Build a GPT from scratch
**Theme:** The single most important build in the plan.

- **Karpathy "Backprop Ninja"** (manual backprop mastery) + **"Let's build GPT"**.
- Train your from-scratch GPT on **Tiny Shakespeare**; it should generate Shakespeare-flavored text.

**Push-gate deliverable:** from-scratch GPT generating text + README → committed.

## Week 10 — The Attention paper
**Theme:** Read the founding paper without hand-holding.

- **The Illustrated Transformer** (Alammar) + **The Annotated Transformer** (Harvard NLP).
- Read **"Attention Is All You Need"** (Vaswani 2017) — aim to read it without confusion.
- Extend your GPT: add **multi-head attention**; run on a second dataset.

**Push-gate deliverable:** multi-head GPT running on 2 datasets + a paper note → committed.

## Week 11 — Hugging Face ecosystem
**Theme:** Use pretrained models like a practitioner.

- **Hugging Face NLP Course ch 1–3.**
- First **fine-tune**: DistilBERT or Qwen2.5-0.5B on IMDB or AG News, via the `Trainer` API.

**Push-gate deliverable:** one fine-tuned classifier in the repo + loaded-HF-model notes → committed.

## Week 12 — LoRA + RAG
**Theme:** Efficient fine-tuning and retrieval — the two techniques you'll actually reach for.

- Read the **LoRA paper** (Hu 2021).
- **LoRA fine-tune** on Alpaca via `peft` + `bitsandbytes`.
- Build a **RAG app**: embeddings + a vector store (Chroma or FAISS) + an LLM API (Claude or OpenAI).

**Push-gate deliverable:** LoRA fine-tune + working RAG app + README → committed.

> **Inflection point:** M3 is where you decide which track to lean toward. M4 makes you taste all three before committing.

---

# Month 4 — Taste three tracks, then commit

## Week 13 — Track taste: ML engineering
- **Weights & Biases** experiment tracking; run a hyperparameter sweep.
- Put a trained model behind a **FastAPI + Docker** endpoint.
- Read about **DDP / FSDP** (distributed training).
- **Ask honestly:** did this energize you?

**Push-gate deliverable:** model behind a Docker + FastAPI endpoint, W&B dashboard linked → committed.

## Week 14 — Track taste: applied AI
- Build a **deployable LLM-API app** with function calling and structured outputs.
- Write **5+ evals** for it.
- **Ask honestly:** did this energize you?

**Push-gate deliverable:** deployed app you'd show a friend, README with screenshots → committed.

## Week 15 — Track taste: research
- **Reproduce an arXiv paper** — pick something small and self-contained.
- Write up the result and where your numbers matched or diverged.
- **Ask honestly:** did this energize you?

**Push-gate deliverable:** reproduced experiment with results + written explanation → committed.

## Week 16 — Reflect and commit
- Compare the three weeks honestly against energy, not just competence.
- **Commit to one track.**
- Write the **Month-5 project spec** (scope it to the hours you actually have).

**Push-gate deliverable:** track decision + project spec → committed.

> **Milestone (lighthouse, ~Dec 13):** Track chosen, Month-5 project spec written and committed.

---

# Month 5 — One substantial project

## Week 17 — Scaffold + baseline
- Stand up the **end-to-end pipeline**, even if results are bad.
- Record a **baseline metric**.

**Push-gate deliverable:** working pipeline + baseline recorded → committed.

## Week 18 — First iteration
- Make a **measurable improvement** over baseline.
- Notes on what worked and what didn't.

**Push-gate deliverable:** improvement over baseline + iteration notes → committed.

## Week 19 — Push for quality
- Get the project **genuinely usable**.
- Put **tests** in place.

**Push-gate deliverable:** usable project + test suite → committed.

## Week 20 — Ship + demo + writeup
- Ship it. Write a **demo** and a **writeup** explaining the approach and results.

**Push-gate deliverable:** shipped project + demo + writeup → committed.

---

# Month 6 — Consolidate and go public

## Week 21 — Paper-reading habit
- Establish a repeatable paper note structure: **claim · method · results · surprises · doubts**.
- First paper note in the repo.

**Push-gate deliverable:** first structured paper note → committed.

## Week 22 — Portfolio polish
- Pick your **top 3 projects**; polish READMEs, pin them to your GitHub profile.
- Update LinkedIn.

**Push-gate deliverable:** 3 polished, pinned projects → committed.

## Week 23 — Open-source contribution
- Open a **PR** (ideally merged) on a major ML project.

**Push-gate deliverable:** PR opened on a real project → linked in journal.

## Week 24 — Community + what's next
- Engage with the community (write up a learning, answer questions, join a group).
- Decide the next 6-month arc from where you've landed.

**Push-gate deliverable:** a public writeup of the journey + a next-arc sketch → committed.

---

## A note on the timeline

At 6.5 hrs/week, this is roughly a **9–10 month** calendar journey, not 6. That's the honest cost of a plan you'll actually execute versus one you abandon. The milestone dates are lighthouses — if you're ahead or behind, adjust them, don't abandon them. The only number that truly matters each week is whether you pushed.
