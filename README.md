Social Media Phishing & Fake Promotion Detection

This project presents a hybrid Machine Learning and Rule-Based system for detecting phishing social media accounts and fraudulent promotional posts.

The system combines:

- Support Vector Machine (SVM) for account-level detection
- LSTM Deep Learning model for post-level text analysis
- Streamlit-based interactive web interface

Problem Statement

Fake accounts and phishing promotions are major cybersecurity threats in social media platforms. These malicious actors:
Impersonate legitimate users
Spread malware and scam links
Manipulate followers using fake promotions

System architecture:

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


Models Used

1️)Account Detection
Algorithm: Support Vector Machine (SVM)
Features:
Followers/Following Ratio
Account Age
Profile Completeness
Bio Presence
Website Link
Output: Fake / Legitimate classification

 Post Detection
 Algorithm
Long Short-Term Memory (LSTM) Neural Network
 Text Preprocessing
- Tokenization
- Sequence Padding
- Keyword Pattern Analysis
 Detection Capabilities
- Scam-related keywords
- Spam posting patterns
- Emotional manipulation phrases
 Technologies Used
- Python
- Scikit-learn
- TensorFlow / Keras
- Pandas
- NumPy
- Streamlit

 How to Run
git clone https://github.com/yourusername/social-media-phishing-detection.git
cd social-media-phishing-detection
pip install -r requirements.txt
streamlit run app/app.py

