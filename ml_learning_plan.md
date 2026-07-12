# 6-Month AI / ML Learning Plan

A week-by-week roadmap from zero to capable practitioner

~12 hrs/week • 24 weeks • ~290 hours total

## How to use this plan

This plan assumes ~12 hrs/week for 24 weeks (~290 hours total). It is structured as an exploration arc: by the end of Month 3 you will have hit the three main tracks (ML engineering, applied AI, and research-flavored work) hard enough to choose one. Months 4–6 specialize and produce portfolio-quality work.

The plan is biased toward building over consuming. If you find yourself watching more than coding, course-correct. The point is not to complete every resource — it is to push code to GitHub every week and accumulate real understanding through implementation.

### Operating principles

**Code more than you read.**
For every hour of video, write at least 30 minutes of code. If you are not implementing, you are not learning.

**Math on demand, not upfront.**
You do not need to finish linear algebra before touching neural networks. Math is woven into the schedule to support what you are building each week.

**Public learning journal.**
Push everything to a GitHub repo called ml-journey (or similar). Add a README to each week explaining what you built and what confused you. By month 6, this is your portfolio.

**Use AI tools while learning AI.**
Have Claude or ChatGPT explain confusing ideas, derive math, debug your code. The skill is asking good questions and verifying answers, not memorizing.

**Hardware reality check.**
CPU is fine for the first 2 months. After that, Google Colab's free tier handles most exercises. Colab Pro ($10/mo) or runpod.io ($0.30–$2/hr) is enough for serious work later.

**Tooling: use uv, not legacy pip/conda.**
Install uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`). Pin Python 3.12 (`uv python pin 3.12`). Use `uv add` for dependencies, `uv run` for execution, `uv sync` to reproduce environments. Commit `pyproject.toml` and `uv.lock`; gitignore `.venv/`.

### How to track progress

Each task in this plan starts with an empty checkbox: ☐

When you complete a task, replace ☐ with ☑ (or just type X over the box). Check in with yourself at the end of each week — celebrate finished checkboxes, and decide whether to roll uncompleted ones forward or drop them.

At the end of each month there is a CHECKPOINT — a concrete thing you should be able to demonstrate. If you can't, slow down rather than push forward.

---

## Month 1 — Foundations

Get tooling sharp, math back, and your first neural network trained. By end of week 4 you will have written backpropagation by hand in NumPy.

### Week 1: Setup and NumPy fluency

*Time budget: ~12 hours*

**Day 1 (~2 hrs) — Environment & repo**
- ☐ Install uv with the official one-liner (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- ☐ Create the ml-journey directory, run `uv init` and `uv python pin 3.12`
- ☐ `uv add numpy pandas matplotlib jupyter ipykernel`
- ☐ Initialize a git repo, push to GitHub as ml-journey
- ☐ Install VS Code with Python and Jupyter extensions (or set up JupyterLab)
- ☐ Make first commit: a README.md describing the goal of the repo

**Days 2–4 (~6 hrs) — NumPy fluency**
- ☐ Work through the official NumPy 'absolute beginners' guide
- ☐ Work through 'NumPy: the absolute basics for beginners'
- ☐ Complete exercises 1–50 of the '100 NumPy exercises' GitHub repo
- ☐ Write a notebook summarizing the operations you learned (broadcasting, indexing, reshaping)

**Days 5–7 (~4 hrs) — Linear algebra refresh**
- ☐ Watch 3Blue1Brown 'Essence of Linear Algebra', chapters 1–2 (vectors; linear combinations and span)
- ☐ Watch chapter 3 (linear transformations and matrices)
- ☐ Watch chapter 4 (matrix multiplication as composition)
- ☐ Watch chapter 5 (three-dimensional linear transformations)
- ☐ Pause and re-derive examples on paper as you watch

> **CHECKPOINT:** Without looking it up, write NumPy code to multiply two matrices, transpose, and take a dot product. Explain in your own words what a matrix multiplication does to a vector geometrically.

### Week 2: More math, NumPy, first model

*Time budget: ~12 hours*

**Days 1–3 (~5 hrs) — Finish linear algebra; start calculus**
- ☐ Watch 3Blue1Brown linear algebra chapters 6–9 (determinants; inverses; rank; dot/cross products)
- ☐ Watch chapters 10–14 (change of basis; eigenvectors; abstract vector spaces)
- ☐ Watch 3Blue1Brown 'Essence of Calculus', chapters 1–4 (derivatives, chain rule basics)

**Days 4–5 (~4 hrs) — Linear regression from scratch**
- ☐ Generate synthetic data: y = 3x + 2 + Gaussian noise
- ☐ Write the mean-squared-error loss function in NumPy
- ☐ Derive the gradient of MSE with respect to weight and bias on paper
- ☐ Implement gradient descent in pure NumPy (no scikit-learn)
- ☐ Plot the loss curve and the fitted line vs the true line
- ☐ Push the notebook to your repo with a README explaining gradient descent in your own words

**Days 6–7 (~3 hrs) — ML vocabulary**
- ☐ Read 'A Visual Introduction to Machine Learning' parts 1 and 2 (r2d3.us)
- ☐ Read chapters 1–2 of Burkov's 'The Hundred-Page Machine Learning Book'

> **CHECKPOINT:** Your linear regression converges within 100 steps to within 1% of the true parameters. Notebook is in the repo with a clear README.

### Week 3: Calculus and logistic regression

*Time budget: ~12 hours*

**Days 1–2 (~4 hrs) — Chain rule mastery**
- ☐ Finish 3Blue1Brown 'Essence of Calculus' (chapters 5–11) completed (done)
- ☐ Drill the chain rule on paper: if f(g(x)), then df/dx = f'(g(x)) · g'(x)
- ☐ Compute derivatives of nested functions until automatic (sigmoid, log, polynomials) (done)

**Days 3–5 (~5 hrs) — Logistic regression from scratch**
- ☐ Implement the sigmoid function in NumPy (done)
- ☐ Implement the binary cross-entropy loss in NumPy
- ☐ Derive the gradient of binary cross-entropy with respect to weights on paper
- ☐ Train logistic regression on the Iris dataset (or sklearn's make_blobs)
- ☐ Plot the decision boundary
- ☐ Add L2 regularization and observe the effect on the boundary

**Days 6–7 (~3 hrs) — Probability refresh**
- ☐ Watch StatQuest 'Statistics Fundamentals' first 6 videos (probability vs likelihood)
- ☐ Watch StatQuest videos on the normal distribution and expected value
- ☐ Watch a StatQuest video on Bayes' theorem
- ☐ Take notes on these in your repo

> **CHECKPOINT:** On paper, no peeking, derive the gradient of L = -y·log(σ(wx+b)) - (1-y)·log(1-σ(wx+b)) with respect to w. Push your logistic regression notebook.

### Week 4: A neural network from scratch (the Karpathy week)

*Time budget: ~12 hours*

**Days 1–2 (~3 hrs) — Watch micrograd**
- ☐ Watch Karpathy's 'The spelled-out intro to neural networks and backpropagation: building micrograd' (YouTube, ~2.5 hrs)
- ☐ Pause to code along with the early sections
- ☐ Take written notes on the autograd graph idea

**Days 3–5 (~6 hrs) — Re-implement micrograd from scratch**
- ☐ Without looking at the source, build a Value class with `__add__`, `__mul__`, and a `backward()` method
- ☐ Add tanh and exp; verify gradients match torch.autograd on a small example
- ☐ Build a simple MLP using your Value class
- ☐ Train it on a tiny binary classification problem
- ☐ Where you got stuck, write notes in the README

**Days 6–7 (~3 hrs) — Apply to a real task**
- ☐ Use `sklearn.datasets.make_moons` to generate a non-linear dataset
- ☐ Train a 2-layer NN (with your micrograd or fresh NumPy) until it learns the boundary
- ☐ Plot the decision boundary; observe how it bends
- ☐ Write a reflection: what does backprop actually do? How is it the chain rule?

> **CHECKPOINT:** MONTH 1 COMPLETE. Repo contains: linear regression, logistic regression, micrograd, NN on moons. You can explain backprop as the chain rule applied recursively through a computation graph.

---

## Month 2 — Real frameworks and classical ML

Graduate from NumPy to PyTorch. Fill in the classical ML knowledge everyone in the field assumes you have. Continue the Karpathy series.

### Week 5: PyTorch fundamentals

*Time budget: ~12 hours*

**Days 1–2 (~4 hrs) — PyTorch basics**
- ☐ Complete PyTorch's official 'Learn the Basics' tutorial, all 8 sections
- ☐ Complete 'Deep Learning with PyTorch: A 60 Minute Blitz'
- ☐ `uv add torch torchvision` (use the official PyTorch install command for your platform)

**Days 3–5 (~5 hrs) — Re-implement and train**
- ☐ Re-implement your week-4 neural network using `nn.Module` and `torch.optim`
- ☐ Notice that `loss.backward()` does what took you days to write by hand
- ☐ Train an MLP on MNIST
- ☐ Aim for >97% test accuracy
- ☐ Try different optimizers (SGD, Adam) and learning rates

**Days 6–7 (~3 hrs) — Core PyTorch objects**
- ☐ Read PyTorch docs on `nn.Module`
- ☐ Read on `DataLoader` and `Dataset`
- ☐ Read on optimizers (SGD, Adam) and learning rate schedulers
- ☐ Write a one-page summary of these four objects in your repo

> **CHECKPOINT:** MNIST classifier hits >97% test accuracy. You can describe what `nn.Module`, `DataLoader`, optimizer, and scheduler each do.

### Week 6: Convolutional networks and computer vision

*Time budget: ~12 hours*

**Days 1–3 (~5 hrs) — CNN theory**
- ☐ Read CS231n notes on convolutional networks (Stanford)
- ☐ Watch the corresponding CS231n lecture if you prefer video
- ☐ Sketch by hand how a 3x3 convolution slides over a 5x5 input
- ☐ Understand pooling, stride, padding intuitively

**Days 4–6 (~5 hrs) — Build a CNN**
- ☐ Build a small CNN for CIFAR-10 in PyTorch
- ☐ Aim for >75% test accuracy
- ☐ Add data augmentation (random crops, flips); measure improvement
- ☐ Add batch normalization; measure improvement
- ☐ Add dropout; measure improvement

**Day 7 (~2 hrs) — Read the AlexNet paper**
- ☐ Read 'ImageNet Classification with Deep Convolutional Neural Networks' (Krizhevsky et al., 2012)
- ☐ Note the key architectural choices and why they mattered historically
- ☐ Add a one-paragraph summary to your repo

> **CHECKPOINT:** CIFAR-10 CNN at >75% test accuracy with augmentation. You can describe what each layer of a CNN does.

### Week 7: Classical ML you actually need to know

*Time budget: ~12 hours*

**Days 1–3 (~5 hrs) — Scikit-learn**
- ☐ Work through scikit-learn's official tutorial
- ☐ Understand train/test split and cross-validation
- ☐ Train a decision tree, random forest, and gradient boosting model on a tabular dataset
- ☐ Try k-means clustering and PCA on a real dataset

**Days 4–5 (~4 hrs) — Kaggle starter**
- ☐ Pick a 'Getting Started' Kaggle competition (Titanic or House Prices)
- ☐ Do EDA: plot distributions, missing values, correlations
- ☐ Engineer features
- ☐ Train an XGBoost model and submit
- ☐ Iterate at least twice based on validation score

**Days 6–7 (~3 hrs) — Theory of generalization**
- ☐ Read about the bias-variance tradeoff
- ☐ Understand why ensembling works (variance reduction)
- ☐ Read Burkov's chapters on regularization and model selection

> **CHECKPOINT:** At least one Kaggle submission. You can explain bias-variance and why XGBoost is so dominant on tabular data.

### Week 8: Karpathy series, part 1

*Time budget: ~12 hours*

**Throughout the week (~12 hrs) — Karpathy 'Zero to Hero' videos 2–4**
- ☐ Watch and code along with 'The spelled-out intro to language modeling: building makemore'
- ☐ Watch 'Building makemore Part 2: MLP'
- ☐ Watch 'Building makemore Part 3: Activations & Gradients, BatchNorm'
- ☐ Implement each from scratch; do not just copy-paste
- ☐ Push each implementation to your repo with notes

> **CHECKPOINT:** MONTH 2 COMPLETE. You can build, train, and evaluate models in PyTorch; you've trained a CNN, an MLP language model, and classical models; you've made a Kaggle submission.

---

## Month 3 — Transformers and LLMs (the inflection point)

Build a transformer from scratch, then fine-tune a real LLM. After this you'll know whether the modern AI stack feels like home.

### Week 9: Karpathy series, part 2 — build a GPT

*Time budget: ~12 hours*

**Throughout the week (~12 hrs) — Backprop ninja and 'Let's build GPT'**
- ☐ Watch and complete 'Building makemore Part 4: Becoming a Backprop Ninja'
- ☐ Watch 'Let's build GPT: from scratch, in code, spelled out' (~2 hrs video, expect ~8 hrs of implementation)
- ☐ Implement the model fully — tokenizer, attention block, training loop
- ☐ Train on the Tiny Shakespeare dataset and generate samples
- ☐ Push the working GPT to your repo

> **CHECKPOINT:** Your from-scratch GPT generates Shakespeare-flavored text. You can describe what each component (embedding, attention, MLP block, layernorm) does.

### Week 10: Attention and the Transformer paper

*Time budget: ~12 hours*

**Days 1–3 (~5 hrs) — Conceptual deep-dive**
- ☐ Read 'The Illustrated Transformer' by Jay Alammar
- ☐ Read 'The Annotated Transformer' (Harvard NLP)
- ☐ Sketch on paper how Q, K, V are computed and how attention scores are formed

**Days 4–5 (~4 hrs) — Original paper**
- ☐ Read 'Attention Is All You Need' (Vaswani et al., 2017) cover to cover
- ☐ Understand every figure
- ☐ Internalize: queries/keys/values, multi-head attention, positional encodings, encoder vs decoder

**Days 6–7 (~3 hrs) — Extend your GPT**
- ☐ Add multi-head attention if your week-9 GPT used single-head
- ☐ Train on a different dataset (Tiny Stories, or a different Shakespeare-scale corpus)
- ☐ Compare sample quality and loss curves

> **CHECKPOINT:** You can read the Transformer paper without confusion. Your extended GPT runs on at least two datasets.

### Week 11: The Hugging Face ecosystem

*Time budget: ~12 hours*

**Days 1–2 (~3 hrs) — HF NLP Course**
- ☐ Complete chapters 1–3 of the Hugging Face NLP Course (free)

**Days 3–5 (~5 hrs) — Use pretrained models**
- ☐ `uv add transformers datasets accelerate`
- ☐ Load a pretrained model (try distilbert-base-uncased or Qwen2.5-0.5B)
- ☐ Run inference on sample text
- ☐ Inspect the tokenizer: encode, decode, examine special tokens
- ☐ Print the model architecture and identify the attention/MLP blocks

**Days 6–7 (~4 hrs) — First fine-tune**
- ☐ Fine-tune a small pretrained model on IMDB sentiment or AG News
- ☐ Use Hugging Face's Trainer class
- ☐ Compare with training the same model from scratch — note how much faster fine-tuning converges

> **CHECKPOINT:** You can load and run any model from Hugging Face Hub. You have one fine-tuned classifier in your repo.

### Week 12: Fine-tuning, LoRA, and a RAG app

*Time budget: ~12 hours*

**Days 1–3 (~5 hrs) — Parameter-efficient fine-tuning**
- ☐ Read the LoRA paper (Hu et al., 2021)
- ☐ `uv add peft bitsandbytes`
- ☐ LoRA-fine-tune a small open-source LLM (Qwen2.5-0.5B or Llama-3.2-1B) on an instruction dataset (e.g., Alpaca)
- ☐ Use Colab free tier if no local GPU
- ☐ Generate responses before and after fine-tuning; observe the difference

**Days 4–7 (~7 hrs) — Build a RAG application**
- ☐ Pick a small corpus you find interesting (your notes, a book, blog posts)
- ☐ Embed documents using a sentence-transformer model
- ☐ Store embeddings in Chroma or FAISS
- ☐ Retrieve top-k relevant chunks for a query
- ☐ Pass them as context to an LLM (Claude API, OpenAI, or local) and answer questions
- ☐ Push the working app to your repo with a README

> **CHECKPOINT:** MONTH 3 COMPLETE. You've built a transformer from scratch, fine-tuned a real LLM with LoRA, and built a working RAG app. By now you should have a sense of which track excites you. Be honest with yourself.

---

## Month 4 — Taste all three tracks, then commit

One week each on ML engineering, applied AI, and research. Reflect at the end of the month and choose where to go deep.

### Week 13: Track taste — ML engineering

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Train, track, deploy**
- ☐ Train a model with proper experiment tracking using Weights & Biases
- ☐ Run a real hyperparameter sweep (random or grid search)
- ☐ Wrap your best model behind a FastAPI endpoint
- ☐ Containerize it with Docker
- ☐ Read about distributed training: DDP and FSDP (no need to actually run multi-GPU)
- ☐ Note in your journal: did this energize you or drain you?

> **CHECKPOINT:** A trained model served behind a Docker + FastAPI endpoint. W&B dashboard linked from your repo.

### Week 14: Track taste — applied AI

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Ship something real**
- ☐ Pick a small product you'd actually use (notes assistant, code reviewer, study tool)
- ☐ Build it end-to-end with the Claude or OpenAI API
- ☐ Use function calling and structured outputs
- ☐ Write at least 5 evals (test cases) and run them
- ☐ Deploy it somewhere accessible (Vercel, Streamlit Community Cloud, etc.)
- ☐ Note in your journal: did this energize you or drain you?

> **CHECKPOINT:** A deployed app you'd show a friend. README with screenshots.

### Week 15: Track taste — research

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Reproduce a paper**
- ☐ Browse arxiv-sanity-lite and pick a recent paper with a narrow, reproducible core experiment
- ☐ Read the paper carefully; understand the claim
- ☐ Reproduce the core experiment in your repo
- ☐ Write a blog-style README explaining what you did and what you found
- ☐ Note in your journal: did this energize you or drain you?

> **CHECKPOINT:** A reproduced experiment with results pushed to your repo, plus a written explanation.

### Week 16: Reflect and commit to a track

*Time budget: ~12 hours*

**Days 1–3 (~6 hrs) — Honest reflection**
- ☐ Write a journal entry comparing the three previous weeks
- ☐ Which one had you losing track of time?
- ☐ Which one made you procrastinate?
- ☐ Where do you have the most natural curiosity?
- ☐ Pick a track. Write down why.

**Days 4–7 (~6 hrs) — Plan month 5 project**
- ☐ Define a substantial project for your chosen track (see month-5 details)
- ☐ Write a one-page project spec: goal, scope, deliverables, weekly milestones
- ☐ Identify the resources you'll need (compute, datasets, tools)
- ☐ Push the spec to your repo

> **CHECKPOINT:** MONTH 4 COMPLETE. Track chosen. Project spec written and committed.

---

## Month 5 — One substantial project in your chosen track

Four weeks on a single project that becomes the centerpiece of your portfolio. The shape depends on your track.

### Week 17: Project week 1 — scaffold and baseline

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Get something working end-to-end, even if poorly**
- ☐ Set up the project repo and environment
- ☐ Get a minimal end-to-end version running (the 'hello world' of your project)
- ☐ Establish a baseline metric (accuracy, latency, user feedback, whatever applies)
- ☐ Write the README with the project goal and current state

> **CHECKPOINT:** End-to-end pipeline working, even if results are bad. Baseline metric recorded.

### Week 18: Project week 2 — first real iteration

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Improve based on what's broken**
- ☐ Identify the top 2 weaknesses of your baseline
- ☐ Address them (better data, better model, better UX, better tests)
- ☐ Measure: did the metric move?
- ☐ Document what you tried and what worked

> **CHECKPOINT:** Measurable improvement over baseline. Notes on what worked and what didn't.

### Week 19: Project week 3 — push for quality

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Polish the rough edges**
- ☐ Get user feedback (real or simulated): what's confusing, what's slow, what's wrong?
- ☐ Fix the top 3 issues
- ☐ Write tests for the parts most likely to break
- ☐ Add monitoring/logging if it makes sense for your project

> **CHECKPOINT:** Project is genuinely usable. Tests in place.

### Week 20: Project week 4 — ship and write up

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Make it visible**
- ☐ Deploy or finalize the project for real use
- ☐ Write a substantial README: motivation, approach, architecture, results, limitations
- ☐ Record a 2–3 minute demo video (Loom or similar)
- ☐ Write a blog post explaining what you built and learned
- ☐ Share it: post on Twitter/X, LinkedIn, or a relevant subreddit

> **CHECKPOINT:** MONTH 5 COMPLETE. Project shipped. Demo video and write-up published.

---

## Month 6 — Polish, papers, and what comes next

Build a paper-reading habit, polish your portfolio, contribute to open source, plug into the community.

### Week 21: Paper reading habit, week 1

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Read with depth**
- ☐ Read one paper relevant to your chosen track this week
- ☐ Take structured notes: claim, method, results, what's surprising, what's questionable
- ☐ Push the notes to a /papers folder in your repo
- ☐ Pick the next paper for week 22

> **CHECKPOINT:** First paper note in your repo with a clear structure you can reuse.

### Week 22: Portfolio polish

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Make it good enough to share with strangers**
- ☐ Pick your top 3 projects from the past 5 months
- ☐ Rewrite each README to be excellent: motivation, approach, results, what you learned
- ☐ Add screenshots, GIFs, or diagrams where useful
- ☐ Pin them on your GitHub profile
- ☐ Update LinkedIn / personal site
- ☐ Read another paper and take notes

> **CHECKPOINT:** Three polished projects pinned. Profile reads as someone serious about ML.

### Week 23: Open-source contribution

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Get a PR merged**
- ☐ Find an open issue in a major ML project (PyTorch, transformers, datasets, etc.)
- ☐ Start with a 'good first issue' label or a small docs fix
- ☐ Read the contributor guide carefully
- ☐ Submit the PR
- ☐ Iterate on review feedback until merged
- ☐ Read another paper and take notes

> **CHECKPOINT:** PR opened (ideally merged) on a major project.

### Week 24: Community and what's next

*Time budget: ~12 hours*

**Across the week (~12 hrs) — Plug in for the long term**
- ☐ Follow 20–30 active ML practitioners on Twitter/X
- ☐ Subscribe to 2–3 newsletters (Import AI, The Batch, etc.)
- ☐ Join one Discord or Slack community in your track
- ☐ Write a retrospective blog post: what you built in 6 months, what you'd do differently
- ☐ Define the next 3-month goal: a job, a research project, a startup, a deeper specialization
- ☐ Read another paper and take notes

> **CHECKPOINT:** MONTH 6 COMPLETE. You are now a competent practitioner with a portfolio, paper-reading habit, OSS contribution, and a clear next direction.

---

## Appendix — Curated resources

These are the resources referenced throughout the plan. Bookmark this page.

### Math
- 3Blue1Brown — Essence of Linear Algebra (YouTube)
- 3Blue1Brown — Essence of Calculus (YouTube)
- StatQuest with Josh Starmer — Statistics Fundamentals (YouTube)

### Foundational ML
- Andrew Burkov — The Hundred-Page Machine Learning Book
- scikit-learn official tutorial (scikit-learn.org)
- Trevor Hastie et al. — The Elements of Statistical Learning (reference)
- r2d3.us — A Visual Introduction to Machine Learning

### Deep learning
- Andrej Karpathy — Neural Networks: Zero to Hero (YouTube series)
- PyTorch official tutorials (pytorch.org/tutorials)
- CS231n notes (Stanford, cs231n.github.io)
- Jay Alammar — The Illustrated Transformer
- Harvard NLP — The Annotated Transformer

### LLMs and applied AI
- Hugging Face — NLP Course (huggingface.co/learn)
- Hugging Face — transformers and peft documentation
- LangChain or LlamaIndex docs (for RAG patterns)
- Anthropic and OpenAI API docs

### Papers (read in order across weeks 6–24)
- Krizhevsky et al., 2012 — ImageNet Classification with Deep CNNs (AlexNet)
- Vaswani et al., 2017 — Attention Is All You Need
- Devlin et al., 2018 — BERT
- Radford et al., 2018–2020 — GPT series
- Hu et al., 2021 — LoRA
- Hoffmann et al., 2022 — Chinchilla scaling laws
- Ouyang et al., 2022 — InstructGPT (RLHF)

### Tooling
- uv — Python package and env manager (astral.sh/uv)
- Weights & Biases — experiment tracking (wandb.ai)
- Hugging Face Hub — model and dataset registry
- Google Colab — free GPU notebooks
- RunPod, Lambda Labs — rentable GPUs

---

## Final note

This is enough. You don't need a master's degree, you don't need to read every paper, you don't need to be the smartest person in any room. You need to build things consistently for 6 months. If you do that, you'll be more capable than the median person who calls themselves an 'AI engineer' today.

*Good luck.*
