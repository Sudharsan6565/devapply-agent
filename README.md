
# 💼 DevApply Agent

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LinkedIn Automation](https://img.shields.io/badge/LinkedIn-Bot-success?logo=linkedin)](https://www.linkedin.com/)
[![Built with Playwright](https://img.shields.io/badge/Built%20with-Playwright-green?logo=Playwright&logoColor=white)](https://playwright.dev/)

An automated **LinkedIn job search and outreach agent** built in just **6 hours** — using Python, Playwright, Tkinter GUI, and a sprinkle of Code Red energy.

> ✅ Private build. For personal job hunting use only. Not open-source.

---

## 🎥 Demo

👉 [Watch how this bot applied for a real job](https://loom.com/your-video-link-here)  
(*Loom link will go here once ready*)

---

## 🔧 ASCII Architecture

```
+-------------------+
|   Manual Login    | ←──────────────┐
+-------------------+                │
            │ Cookies saved          │
            ↓                        │
+-------------------+      +-------------------+
| Load Cookies and  |─────▶| Launch LinkedIn   |
| Create Browser    |      | Session with Bot  |
+-------------------+      +-------------------+
            │                        │
            ↓                        ↓
+-------------------+      +-----------------------+
| Search Jobs Based |─────▶| Scroll & Scrape Jobs |
| on Keywords       |      | (Easy Apply Filter)  |
+-------------------+      +-----------------------+
                                     │
                                     ↓
                          +-------------------------+
                          | Parse and Display Jobs |
                          +-------------------------+
```

---

## 🚀 What It Does

This GUI + CLI tool logs into your LinkedIn account using saved cookies and **automatically finds jobs** matching your criteria.

### Features:
- 🔐 Secure manual login (cookies stored)
- 🔍 LinkedIn job search by keyword + location
- ⚡ Easy Apply filter
- 🖥 Tkinter GUI to preview results
- ✅ Export jobs to CSV
- 🔗 Double-click any job to open the LinkedIn URL
- 🧠 Robust selectors to handle LinkedIn layout changes
- 🧪 Auto-scroll and debug tools

---

## 📂 Project Structure

```
devapply_agent/
├── core/
│   ├── job_search.py       # Job scraper logic
│   ├── session.py          # Manual login + cookie handling
│   ├── utils.py            # Scroll + HTML dump tools
├── cookies/                # Saved session
├── gui/                    # GUI script (optional alt)
├── ui.py                   # Tkinter interface
├── app.py                  # Launcher script
└── README.md
```

---

## 🛠️ How to Use

### One-Time Setup

```bash
git clone git@github.com:Sudharsan6565/devapply-agent.git
cd devapply_agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Login (First Time Only)

```bash
python app.py
```

- Choose manual login
- Login via browser
- Cookies saved automatically

### Daily Use (Auto Login)

```bash
python app.py
```

---

## ⚠️ License

**This project is for private/personal use only. No license is granted.**  
Do not fork, redistribute, or publish without permission.

---

## 💬 Author

Made with Code Red ☕ + Playwright by [Sudharsan](https://github.com/Sudharsan6565)  
→ Also check: [aws.sudharsan17.online][sudharsan17.online](https://aws.sudharsan17.online) – AWS Assistant on mobile.

---

> “I don’t just apply for jobs. I build the tool that finds them.”
