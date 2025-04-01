
# 💼 DevApply Agent

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LinkedIn Automation](https://img.shields.io/badge/LinkedIn-Bot-success?logo=linkedin)](https://www.linkedin.com/)
[![Built with Playwright](https://img.shields.io/badge/Built%20with-Playwright-green?logo=Playwright&logoColor=white)](https://playwright.dev/)

An automated **LinkedIn job search and outreach bot** built using **Playwright**, **Python**, and a sprinkle of chaos.

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

This CLI tool logs into your LinkedIn account using saved cookies and **automatically searches** for jobs matching your query.

### ✅ Features So Far

- 🔐 Manual login → saved cookies (no login every time)
- 🔍 Job scraping via Playwright
- ⚡ Easy Apply filter
- 📄 Auto-scroll and HTML dump for inspection
- 🧪 Multi-selector parsing (robust against UI changes)
- ✅ Works with headless or full browser
- 🧠 Uses intelligent fallback selectors

## 📦 Project Structure

```
devapply_agent/
│
├── core/
│   ├── job_search.py       # Job scraper logic
│   ├── session.py          # Manual login + cookie handling
│   ├── utils.py            # Scroll + HTML dump tools
│
├── .venv/                  # Local Python environment (ignored)
├── cookies/                # Session cookies saved here (ignored)
├── debug_jobs_page.html    # HTML dump of the job page
├── app.py                  # Main launcher script
└── README.md
```

## 🛠️ How To Use

### 1. First-Time Login

```bash
python app.py
```

Choose manual login, sign in via LinkedIn browser popup, hit Enter, and cookies get saved for future runs.

### 2. Auto Launch with Saved Session

```bash
python app.py
```

It auto-detects cookies, logs in, scrapes jobs with filters, and dumps the HTML.

## 📌 TODO (Coming Soon)

- ✅ Auto Easy Apply for matching jobs  
- 🧠 Recruiter post sentiment analysis  
- ✉️ Auto-DM recruiter after connecting  
- 📊 Job filtering by recent activity  
- 💬 CLI UI with Tkinter GUI mode  
- 🔁 Cron job automation  
- 🤖 ML ranking system ("Recruiter Bait Score")

## 🧠 Dev Philosophy

> "Apply smart. Not hard."

You’ve already seen how painful manual job hunting is. Let this agent hunt jobs while you focus on leveling up.

## 🤝 Contributing

Wanna help? Fork, star, and open a PR. Or just tell your recruiter friends this bot exists.

---

Made with ❤️ by [@Sudharsan6565](https://github.com/Sudharsan6565)
