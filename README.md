# 🩺 Chronic Kidney Disease (CKD) Detection Project

## 📌 Overview
This project aims to detect and classify Chronic Kidney Disease (CKD) stages using machine learning and deep learning techniques. It involves exploratory data analysis (EDA), preprocessing, modeling, evaluation, and model persistence for real-world usage.

---

## 📁 Dataset Information

This project uses three datasets:

- `imputed data.csv`
- `CKD_dataset_AbuDhabi.csv`
- `40K_dataset.csv`

Each dataset contains clinical and laboratory features with a corresponding target column (`stage`, `ckd_stage`, or `CKD_stage`) representing the CKD stage.

---

## 🧼 Data Preprocessing

Key preprocessing steps:

- **Missing Value Analysis**: Percentage of missing values computed for each file.
- **Feature Exploration**:
  - Unique value count
  - Data type checking (categorical vs numerical)
- **Feature Visualization**:
  - Histograms, bar plots, pie charts for understanding distribution
- **Data Balancing**: Used `SMOTE` to handle class imbalance
- **Standardization**: Applied `StandardScaler` for numeric features

---

## 🧪 Exploratory Data Analysis (EDA)

The notebook explores:

- Class distributions
- Missing data patterns
- Value distributions across all features
- Frequency of categories in categorical features

---

## 🧮 Machine Learning – K-Nearest Neighbors (KNN)

- **Model**: `KNeighborsClassifier`
- **Hyperparameter Tuning**: `RandomizedSearchCV`
- **Evaluation Metrics**:
  - Accuracy
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-Score)

---

## 🧠 Deep Learning – PyTorch Neural Network

- **Framework**: PyTorch
- **Architecture**: Fully Connected Feedforward Network
- **DataLoader**: Batch processing using PyTorch `TensorDataset`
- **Loss Function**: `CrossEntropyLoss`
- **Optimizer**: `Adam`
- **Evaluation**:
  - ROC Curve
  - Precision-Recall Curve
  - AUC Score

---

## 📊 Performance Evaluation

- **Permutation Importance**: To analyze feature impact
- **Learning Curves**: Training performance over time
- **Validation Curves**: Model behavior over hyperparameter changes
- **Visual Aids**:
  - ROC & PR curves
  - Confusion matrix plots
  - Feature importance bar plots

---

## 💾 Model Persistence

Models were saved using:

- `joblib`
- `pickle`

This enables reloading without retraining, ready for deployment.

---

## ✅ Results & Conclusion

- The model successfully detects CKD and classifies it into stages.
- Both classical ML (KNN) and deep learning (PyTorch) approaches are tested.
- Balanced datasets improve fairness across all CKD stages.
- Visualization tools support transparency and explainability.

---

## 🚀 Future Work

- Add more diverse datasets
- Implement Transformer-based models for tabular data
- Deploy as a web or mobile app using Flask or FastAPI
