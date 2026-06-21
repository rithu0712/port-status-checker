import re

def analyze_email(email):
    risk_score = 0
    reasons = []

    suspicious_keywords = [
        "urgent", "verify", "password", "bank account",
        "click here", "login now", "limited time",
        "update account", "confirm identity"
    ]

    for keyword in suspicious_keywords:
        if keyword.lower() in email.lower():
            risk_score += 1
            reasons.append(f"Suspicious keyword found: '{keyword}'")

    urls = re.findall(r'https?://\S+|www\.\S+', email)
    if urls:
        risk_score += 1
        reasons.append("Contains external link(s)")

    sensitive_words = [
        "otp", "credit card", "debit card",
        "cvv", "pin", "password"
    ]

    for word in sensitive_words:
        if word.lower() in email.lower():
            risk_score += 1
            reasons.append(f"Sensitive information request: '{word}'")

    print("\n----- EMAIL ANALYSIS REPORT -----")

    if risk_score >= 3:
        print("⚠️ HIGH RISK EMAIL")
    elif risk_score >= 1:
        print("⚠️ MEDIUM RISK EMAIL")
    else:
        print("✅ SAFE EMAIL")

    print("\nReasons:")
    if reasons:
        for reason in reasons:
            print("-", reason)
    else:
        print("No suspicious content detected.")

email_text = input("Paste Email Content:\n")
analyze_email(email_text)