import streamlit as st
import requests

# Security headers to check
SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps prevent XSS attacks",
    "Strict-Transport-Security": "Enforces HTTPS",
    "X-Content-Type-Options": "Stops MIME type sniffing",
    "X-Frame-Options": "Mitigates clickjacking",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Restricts browser features"
}

def calculate_score(found_headers):
    total = len(SECURITY_HEADERS)
    found = len(found_headers)
    percentage = (found / total) * 100
    if percentage == 100:
        return "A+", percentage
    elif percentage >= 80:
        return "A", percentage
    elif percentage >= 60:
        return "B", percentage
    elif percentage >= 40:
        return "C", percentage
    elif percentage >= 20:
        return "D", percentage
    else:
        return "F", percentage

st.title("🔒 Website Security Header Analyzer")
url = st.text_input("Enter a website URL (e.g., https://example.com)")

if st.button("Analyze"):
    if not url.startswith("http"):
        st.error("Please include http:// or https:// in the URL")
    else:
        try:
            response = requests.get(url, timeout=10)
            headers = response.headers

            found = {h: headers[h] for h in SECURITY_HEADERS if h in headers}
            missing = {h: SECURITY_HEADERS[h] for h in SECURITY_HEADERS if h not in headers}

            grade, percent = calculate_score(found)

            st.subheader(f"🏆 Score: {grade} ({percent:.0f}%)")

            st.success("✅ Found Headers:")
            for k, v in found.items():
                st.write(f"- {k}: {v}")

            st.error("❌ Missing Headers:")
            for k, v in missing.items():
                st.write(f"- {k} → {v}")

        except Exception as e:
            st.error(f"Error fetching {url}: {e}")
