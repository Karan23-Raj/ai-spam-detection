import streamlit as st

spam_keywords = [
    "win", "winner", "lottery", "jackpot", "prize", "reward", "gift",
    "cash prize", "lucky draw", "congratulations", "selected winner",

    "free money", "easy money", "earn money", "instant cash",
    "double your money", "cash reward", "claim money",

    "bank details", "bank account", "account blocked", "account suspended",
    "account frozen", "verify account", "bank verification",
    "update bank account", "credit card blocked", "debit card blocked",

    "otp", "share otp", "provide otp", "verification code",
    "security code", "one time password",

    "upi", "upi pin", "google pay", "phonepe", "paytm",
    "payment request", "collect request", "receive payment",
    "scan qr code", "wallet update",

    "kyc", "complete kyc", "update kyc", "re-kyc",
    "kyc expired", "kyc verification required",

    "urgent", "immediately", "act now", "limited time",
    "within 24 hours", "final warning", "last chance",
    "avoid suspension",

    "click here", "tap here", "visit link", "open link",
    "verify now", "login now", "update now",

    "unauthorized login", "suspicious login", "login attempt",
    "security alert", "password expired", "reset password",
    "account recovery", "verify identity",

    "income tax refund", "gst refund", "government subsidy",
    "pm yojana", "aadhaar update", "pan verification",

    "parcel pending", "package held", "delivery failed",
    "courier issue", "tracking update",

    "work from home", "part time job", "online job",
    "earn daily", "registration fee", "joining fee",

    "crypto investment", "bitcoin profit", "guaranteed return",
    "investment plan", "trading profit", "100% return",

    "exclusive offer", "special offer", "free gift",
    "bonus reward", "customer care", "helpline number",
    "confidential", "sensitive information",

    "account will be closed", "service suspended",
    "legal action", "penalty", "fine payment",
    "court notice"
]
st.title("AI Spam & Fraud Detection Assistant")

message = st.text_area("Enter Message")

if st.button("Analyze"):
    score = 0
    reasons = []

    for keyword in spam_keywords:
        if keyword.lower() in message.lower():
            score += 10
            reasons.append(keyword)

    result = "Spam/Fraud" if score >= 30 else "Safe"

    st.write("Result:", result)
    st.write("Risk Score:", score, "%")

    if reasons:
        st.write("Reasons:")
        for r in reasons:
            st.write("-", r)
