import streamlit as st
import re

# --- Streamlit Config ---
st.set_page_config(page_title="Phishing & Fake Promotion Detector (Rule-Based AI)", layout="wide")

st.title("🧠 AI-Like Rule-Based Phishing & Fake Promotion Detector")
st.markdown("""
This **rule-based intelligent system** mimics how a trained ML model detects fake accounts and phishing posts.
It follows carefully tuned heuristics inspired by real social media behavior.
""")

# ===================================================================
# --- ACCOUNT DETECTION ---
# ===================================================================
st.header("👤 Phishing Account Detection")

col1, col2, col3 = st.columns(3)
with col1:
    followers_count = st.number_input("Followers Count", min_value=0, value=50, step=10)
    posts_count = st.number_input("Posts Count", min_value=0, value=10, step=1)
    is_verified = st.selectbox("Is Verified?", [False, True])

with col2:
    following_count = st.number_input("Following Count", min_value=0, value=500, step=10)
    account_age_days = st.number_input("Account Age (Days)", min_value=1, value=60, step=10)
    has_website = st.selectbox("Has Website Link?", [False, True])

with col3:
    profile_completeness = st.slider("Profile Completeness (0.0 to 1.0)", 0.0, 1.0, 0.5)
    has_bio = st.selectbox("Has Bio?", [False, True])

if st.button("Analyze Account"):
    risk_score = 0

    # --- Robust Rules ---
    if is_verified:
        risk_score = 0
        st.success("✅ Verified account detected — considered safe by rule.")
    else:
        # Ratio
        ratio = (following_count + 1) / (followers_count + 1)
        if followers_count < 50:
            risk_score += 20
        if ratio > 3:
            risk_score += 25
        if posts_count < 5:
            risk_score += 10
        if account_age_days < 60:
            risk_score += 20
        if not has_bio:
            risk_score += 10
        if not has_website:
            risk_score += 5
        if profile_completeness < 0.4:
            risk_score += 10
        if followers_count > 1000:
            risk_score -= 10
        if account_age_days > 180:
            risk_score -= 10

    # Normalize and clamp
    risk_score = min(max(risk_score, 0), 100)
    confidence = 1 - abs(0.5 - (risk_score / 100))

    # --- Decision ---
    if is_verified:
        decision = "LEGITIMATE"
        st.balloons()
        st.success(f"🟢 LEGITIMATE ACCOUNT (Verified) — Risk: 0/100 | Confidence: 100%")
    elif risk_score >= 60:
        decision = "FAKE"
        st.error(f"🔴 PHISHING/FAKE ACCOUNT DETECTED — Risk: {risk_score}/100 | Confidence: {confidence:.2f}")
        st.markdown("""
        **Reasons possibly indicating fake behavior:**
        - High following/follower ratio
        - Low followers or few posts
        - Recently created account
        """)
    else:
        decision = "LEGITIMATE"
        st.success(f"🟢 LEGITIMATE ACCOUNT — Risk: {risk_score}/100 | Confidence: {confidence:.2f}")
        st.markdown("""
        **Indicators of legitimacy:**
        - Good followers/following balance
        - Decent account age
        - Complete bio and website
        """)

st.markdown("---")

# ===================================================================
# --- POST DETECTION ---
# ===================================================================
st.header("💬 Fake Post/Promotion Detection")

post_input = st.text_area(
    "Enter Post Text:",
    placeholder="Example: 'Click here to claim your FREE reward now!!!'",
    height=150
)

if st.button("Analyze Post"):
    if not post_input.strip():
        st.warning("Please enter a post to analyze.")
    else:
        text = post_input.lower()

        # Suspicious keywords
        phishing_keywords = [
            'free', 'win', 'offer', 'click', 'verify', 'account', 'link', 'limited', 
            'money', 'prize', 'gift', 'urgent', 'bit.ly', 'tinyurl', 'login', 'bonus', 
            'giveaway', 'congratulations', 'lottery', 'reward', 'claim', 'cash','rich','faster'
        ]
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags
                               "]+", flags=re.UNICODE)

        suspicious_count = sum(word in text for word in phishing_keywords)
        exclamation_count = text.count("!")
        emoji_count = len(emoji_pattern.findall(text))
        all_caps_words = len(re.findall(r'\b[A-Z]{3,}\b', post_input))
        word_count = len(text.split())

        # Rule weights
        score = suspicious_count * 10 + exclamation_count * 2 + emoji_count * 2 + all_caps_words * 5

        # Adjust by length
        if word_count < 10:
            score += 10
        elif word_count > 50:
            score -= 5

        score = min(max(score, 0), 100)
        prob_fake = score / 100

        if prob_fake > 0.5:
            st.error(f"⚠️ Probability: {prob_fake:.2f})")
            st.markdown("""
            **Reasons possibly indicating phishing content:**
            - Contains suspicious keywords like "free", "click", "verify"
            - Overuse of punctuation or emojis
            - Very short or spammy message
            """)
        else:
            st.success(f"✅ Probability: {prob_fake:.2f})")
            st.markdown("""
            **Indicators of legitimate content:**
            - Natural writing style
            - No scam-related keywords
            - Balanced punctuation and tone
            """)

st.markdown("---")
st.caption("⚙️ This version uses deterministic rules but simulates AI-style reasoning for demonstration purposes.")
