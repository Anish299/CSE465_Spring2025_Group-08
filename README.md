# CSE465_Spring2025_Group-08
# 🩺 Chronic Kidney Disease Detection using Neural Networks

This project detects **Chronic Kidney Disease (CKD)** using a 5-layer Artificial Neural Network (ANN) trained on an **augmented medical dataset**. It classifies whether a patient has CKD based on various clinical indicators.

---

## 🚀 Project Overview

- **Objective**: Predict the presence of CKD from clinical numeric data.
- **Methodology**: Train a deep neural network with 5-fold cross-validation.
- **Tools & Libraries**: Python, TensorFlow/Keras (or PyTorch), Pandas, NumPy, Scikit-learn, Google Colab.

---

## 📁 Dataset

- The dataset is augmented to improve model robustness and generalization.
- Augmented files are located in the `augmented_dataset/` directory.
- Each entry includes features such as:
  - Blood pressure
  - Blood glucose levels
  - Serum creatinine
  - Hemoglobin
  - Packed cell volume
  - and more...

---

## 🧠 Model Architecture

- 5-layer fully connected ANN.
- **Activation Functions**:
  - ReLU (hidden layers)
  - Sigmoid or Softmax (output)
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy

---

## 📊 Training Configuration

- **Validation**: 5-Fold Cross Validation
- **Metrics**: Accuracy, Precision, Recall, Loss
- Training logs and graphs are included in the notebook.

---

## 📂 Project Structure


