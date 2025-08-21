# 🔒 Website Security Header Analyzer

A simple web-based tool to analyze HTTP security headers of any website and provide a **scorecard (A–F)** like SSL Labs.  

This project helps security learners and professionals quickly check if websites implement important headers like:

- **Content-Security-Policy (CSP)** – Prevents XSS  
- **Strict-Transport-Security (HSTS)** – Enforces HTTPS  
- **X-Frame-Options** – Protects against clickjacking  
- **X-Content-Type-Options** – Stops MIME sniffing  
- **Referrer-Policy** – Controls referrer data  
- **Permissions-Policy** – Restricts browser features  

---

## 🚀 Features
- Input any website URL.  
- Fetch and analyze security headers.  
- Display **found** vs **missing** headers.  
- Generate a **score (A–F)** based on coverage.  
- Can be run **locally** or deployed via **Streamlit Cloud / GitHub Pages (with Streamlit sharing)**.  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Streamlit** (UI)  
- **Requests** (fetch headers)  

---

## 📦 Project Access
You can view and try the project here:
https://website-security-header-analyzer.streamlit.app/
Github Repository
https://github.com/Nivas-Kanniah/Website-Security-Header-Analyzer

