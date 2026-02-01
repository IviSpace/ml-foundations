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


### Day 00 - Concepts of Audio Processing
**Key Learning**
This is an experiment to get in to introduction of interperatation of audio data
Special terms like 
            - Frequncy
            - Intersity(Amplitude)
            - Sample Rate
            - Spectrogram
            - Mel-Spectrogram 
            


### Day 02 — IMDB Sentiment Baseline
- Model: TF-IDF + Logistic Regression
- Accuracy: 86.4%
- ROC–AUC: 0.94

This notebook demonstrates a complete NLP pipeline:
preprocessing → vectorisation → classification → evaluation.

### DAY 03 - Plan
1.Imports
2.Folder setup
3.Real audio creation
4.Spoof audio generation
5.Feature extraction (next)
6.Classifier + EER (next)

### Day 03 — Audio Spoofing Baseline (Log-Mel + EER)

This experiment validates a minimal audio deepfake detection pipeline.

**Approach**
- Loaded real (bona fide) and spoofed speech samples
- Extracted log-mel spectrograms from audio signals
- Applied temporal mean pooling to obtain fixed-length feature vectors
- Trained a lightweight Logistic Regression classifier

**Evaluation**
- Performance evaluated using Equal Error Rate (EER), which is commonly used in spoofing detection
- Visualised score distributions for real vs spoofed speech to inspect class separation

**Key Learning**
This experiment demonstrates that audio deepfake detection follows the same core ML pipeline as NLP tasks:
feature extraction → classification → evaluation, with modality-specific representations.
