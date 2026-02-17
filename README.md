# 🛡️ Social Media Phishing Account Detection using Machine Learning

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

Social media platforms are increasingly targeted by **phishing and fake accounts** that impersonate genuine users. These malicious accounts are used to spread malware, scams, spam campaigns, and misinformation.

Manual detection methods are inefficient, time-consuming, and not scalable.  
This project proposes a **Machine Learning–based automated detection system** to classify social media accounts as legitimate or phishing.

---

## 🎯 Problem Statement

- Fake accounts impersonate real users.
- They spread malware, phishing links, and scams.
- They damage user trust and platform integrity.
- Manual moderation is slow and expensive.
- Need for an automated, scalable detection system.

---

## 🧠 Proposed Solution

This system uses supervised machine learning to detect phishing accounts based on profile-level features.

### 🔹 Step 1: Data Collection
- Publicly available social media profile datasets
- Labeled accounts (Legitimate / Phishing)

### 🔹 Step 2: Feature Engineering
Extracted meaningful features such as:

- Number of followers
- Number of followings
- Followers-to-following ratio
- Bio length
- Presence of URL in bio
- Account age
- Number of posts
- Profile completeness indicators

### 🔹 Step 3: Model Training
- Data split into training and testing sets
- Multiple models trained and compared
- Hyperparameter tuning applied

### 🔹 Step 4: Prediction System
- Final model deployed using **Streamlit**
- Users can input profile data
- Model predicts: **Legitimate or Phishing**

---

## 🏗️ System Architecture

```
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Deployment (Streamlit Web App)
```

---

## 📊 Machine Learning Models Used

The following models were evaluated:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

### ✅ Final Model Selected: Random Forest

**Why Random Forest?**
- Handles nonlinear patterns well
- Robust to overfitting
- Performs well on tabular data
- Provides feature importance insights

---

## 📈 Model Performance

| Metric        | Score  |
|--------------|--------|
| **Accuracy**  | 94.2% |
| **Precision** | 92%   |
| **Recall**    | 95%   |
| **F1-Score**  | 93%   |

### 📌 Interpretation

- **High Recall (95%)** → Effectively detects phishing accounts  
- **High Precision (92%)** → Low false positives  
- **Balanced F1-score (93%)** → Strong overall performance  

---

## 🔎 Confusion Matrix

> Add your confusion matrix image inside the repository and link it below:

```markdown
![Confusion Matrix](images/confusion_matrix.png)
```

---

## ⚙️ Tech Stack

### 🧠 Backend & ML
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### 📊 Visualization
- Matplotlib
- Seaborn

### 🌐 Deployment
- Streamlit

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
```

### 2️⃣ Navigate to project folder

```bash
cd social-media-phishing-detection
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app/app.py
```

---

## 📁 Project Structure

```
social-media-phishing-detection/
│
├── data/
├── models/
├── notebooks/
├── app/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

- Deep learning-based detection
- Real-time API integration
- Browser extension integration
- Automated feature extraction pipeline
- Continuous learning system

---

## 📜 License

This project is developed for academic and research purposes.

---

## 👨‍💻 Author

**Alex**  
Machine Learning Enthusiast | AI Developer  

---

⭐ If you found this project useful, consider giving it a star!
