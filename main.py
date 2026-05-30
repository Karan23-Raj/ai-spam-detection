import streamlit as st

spam_keywords = [
    "win", "lottery", "free money", "bank details",
    "otp", "urgent", "click here", "reward",
    "kyc", "upi", "prize", "gift"
]

st.title("AI Spam & Fraud Detection Assistant")

message = st.text_area("Enter Message")

if st.button("Analyze"):
    score = 0
    reasons = []

    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            score += 25
            reasons.append(keyword)

    result = "Spam/Fraud" if score >= 20 else "Safe"

    st.write("Result:", result)
    st.write("Risk Score:", score, "%")

    if reasons:
        st.write("Reasons:")
        for r in reasons:
            st.write("-", r)
