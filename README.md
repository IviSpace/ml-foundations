# ML Foundations (NLP + Audio Track)

This repository documents my foundations in applied machine learning using Python, with a focus on skills needed for NLP and speech/audio ML projects.

## What’s inside
- Clean, structured notebooks (learning + experiments)
- Reproducible ML workflows (data → model → evaluation)
- Practical utilities (metrics, plots, helpers)

## Tech stack
- Python
- NumPy, Pandas
- Scikit-learn
- PyTorch (basics)

## Repository structure
- `notebooks/` – numbered notebooks for each topic
- `src/` – reusable helper functions (metrics, utilities)
- `data/` – kept empty in git (local only)
- `reports/` – saved plots/figures (optional)

## How to run
1. Create a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


### Day 02 — IMDB Sentiment Baseline
- Model: TF-IDF + Logistic Regression
- Accuracy: 86.4%
- ROC–AUC: 0.94

This notebook demonstrates a complete NLP pipeline:
preprocessing → vectorisation → classification → evaluation.