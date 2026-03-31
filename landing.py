import streamlit as st

st.set_page_config(page_title="Blood Results Checker", layout="centered")

# Custom CSS for a clean, professional look
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1a4a6f;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #2c5a7a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature {
        background-color: #f0f4f8;
        border-left: 4px solid #e67e22;
        padding: 1rem;
        margin: 1rem 0;
    }
    .pricing {
        background-color: #eef2fa;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 2rem 0;
    }
    .price {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1a4a6f;
    }
    .cta-button {
        background-color: #e67e22;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.8rem;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🩸 Blood Results Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Automate blood result review and Cliniko integration</div>', unsafe_allow_html=True)

st.markdown("""
### Save hours of admin time
- **Upload blood test PDF/DOCX** – instantly extract results.
- **Flag abnormal values** – based on reference ranges or custom rules.
- **Match patients automatically** – via NHS number or name/DOB.
- **Push plans directly to Cliniko** – as clinical notes.
- **Secure, GDPR‑compliant** – your data stays private.
""")

st.markdown("""
<div class="feature">
<strong>✅ Trusted by clinicians</strong><br>
“This tool cut my blood result review time from 30 minutes to 5 minutes per clinic.” – Karen G.
</div>
""", unsafe_allow_html=True)

# Pricing section
st.markdown("""
<div class="pricing">
    <div class="price">£30 / month</div>
    <div>per practice – unlimited uploads and Cliniko integration</div>
    <a href="https://buy.stripe.com/fZueVc35I5R28H7aJA0gw00" class="cta-button">Start 14‑day free trial →</a>
    <div style="margin-top: 1rem; font-size: 0.9rem;">No setup fee. Cancel anytime.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### How it works
1. **Upload** a blood test file (PDF or DOCX).
2. **Review** flagged results and add your plan.
3. **Click** “Push to Cliniko” – the plan appears in the patient’s timeline.
4. **Save time** and focus on patient care.

*Integrates with Cliniko via secure API. Works with any lab report format.*
""")

st.markdown("""
---
### Need a demo or custom setup?
Contact me directly:  
[LinkedIn](https://www.linkedin.com/in/george-shaker-a856b01b9/) | [Email](mailto:george@example.com)
""", unsafe_allow_html=False)

st.markdown('<div class="footer">© 2026 Blood Results Checker – Built for Cliniko users</div>', unsafe_allow_html=True)