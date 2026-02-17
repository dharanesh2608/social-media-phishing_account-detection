# 🛡️ Social Media Phishing Account & Fake Promotion Detection

## 📌 Overview

This project presents a hybrid Machine Learning system for detecting phishing social media accounts and fraudulent promotional posts.

The system combines:

🔹 Support Vector Machine (SVM) for account-level detection  
🔹 LSTM Deep Learning model for post-level text analysis  
🔹 Streamlit-based interactive web interface  

---

## 🎯 Problem Statement

Fake accounts and phishing promotions are major cybersecurity threats in social media platforms. These malicious actors:

- Impersonate legitimate users  
- Spread malware and scam links  
- Manipulate followers using fake promotions  

Manual moderation is inefficient and not scalable.

This project automates detection using AI techniques.

---

## 🧠 System Architecture

```
User Input
   ↓
Feature Extraction
   ↓
Account Model (SVM)
Post Model (LSTM)
   ↓
Risk Scoring
   ↓
Final Decision
   ↓
Streamlit Web Interface
```

---

## 🤖 Models Used

### 1️⃣ Account Detection

Algorithm: Support Vector Machine (SVM)

Features:

- Followers/Following Ratio  
- Account Age  
- Profile Completeness  
- Bio Presence  
- Website Link  

Output: Fake / Legitimate classification  

---

### 2️⃣ Post Detection

Algorithm: LSTM (Long Short-Term Memory Network)

Text Preprocessing:

- Tokenization  
- Sequence Padding  
- Keyword Analysis  

Detects:

- Scam keywords  
- Spam patterns  
- Emotional manipulation phrases  

---

## 📊 Technologies Used

- Python  
- Scikit-learn  
- TensorFlow / Keras  
- Pandas  
- NumPy  
- Streamlit  

---

## 🚀 How to Run

```bash
git clone https://github.com/dharanesh2608/social-media-phishing-detection.git
cd social-media-phishing-detection
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 🖥️ Application Screenshots

![Screenshot 1](/images/Screenshot%202026-02-17%20212242.png)

![Screenshot 2](/images/Screenshot%202026-02-17%20212322.png)

![Screenshot 3](/images/Screenshot%202026-02-17%20212558.png)

![Screenshot 4](/images/Screenshot%202026-02-17%20214338.png)



