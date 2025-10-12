# Legal Case Outcome Classification using Legal-BERT and SVM

This project predicts the **outcome of legal case citations** (e.g., *cited*, *applied*, *followed*, *affirmed*, etc.) using **Legal-BERT embeddings** and a **Support Vector Machine (SVM)** classifier.

The workflow combines **domain-specific text embeddings** from Legal-BERT with classical machine learning to achieve interpretable, high-performing legal text classification.

Data Source: https://www.kaggle.com/datasets/amohankumar/legal-text-classification-dataset

---

## Project Overview

### Goal
Classify legal case citations into one of several **semantic outcome categories**, such as:
- **Positive citation** – *cited*, *applied*, *followed*
- **Neutral citation** – *considered*, *discussed*
- **Negative citation** – *distinguished*
- **Approval** – *affirmed*, *approved*, *related*

### Approach
1. **Data preprocessing**
   - Combine `Case_Title` and `Case_Text`
   - Clean, tokenize, and lemmatize text
   - Group similar outcomes into four semantic categories
2. **Text representation**
   - Generate embeddings using [`nlpaueb/legal-bert-base-uncased`](https://huggingface.co/nlpaueb/legal-bert-base-uncased)
3. **Classification**
   - Train a `LinearSVC` model (`scikit-learn`)
   - Use `class_weight='balanced'` for imbalance handling
4. **Evaluation**
   - Macro F1-score for balanced multi-class evaluation
   - Confusion matrix and per-class performance metrics

---

## Project Structure
Model/
│
├── Legal_case_classification_development.ipynb # Model training & analysis
├── legal_case_classification.py # Inference script
├── test_legal_case_classification.py # Unit tests
├── legal_case_classifier.pkl/ # Saved model 


---

## Setup Instructions

1). Activate your virtual environment
    .\venv\Scripts\activate
2). Install requirements
    pip install -r requirements.txt
3). Navigate to the Model folder
4). Run the script
    python legal_case_classification.py

---
## Testing
pytest test_legal_case_classification.py

--

## Results Summary

| Dataset    | Macro F1 | Accuracy |
| ---------- | -------- | -------- |
| Train      | 0.55     | 0.80     |
| Validation | 0.43     | 0.76     |
| Test       | 0.42     | 0.77     |

Legal-BERT embeddings improved F1 by ~25% compared to TF-IDF and MiniLM embeddings.