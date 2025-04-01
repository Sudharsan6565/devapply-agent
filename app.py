# devapply_agent/app.py

from core.session import manual_login, launch_with_cookies, cookies_exist
from core.job_search import find_jobs
from ui import launch_ui

def main():
    if cookies_exist():
        print("🍪 Cookies found. Auto-launching job search...")

        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            from core.session import load_cookies
            load_cookies(context)
            page = context.new_page()

            page.goto("https://www.linkedin.com/feed/")
            print("🟢 Logged in with saved cookies.\n")

            jobs = find_jobs(page, "AWS Cloud Engineer", location="Remote", easy_apply_only=True)

            if jobs:
                print(f"\n✅ Found {len(jobs)} matching jobs:\n")
                for job in jobs:
                    print(f"💼 {job['title']} @ {job['company']} [{job['location']}] — {job['posted']}")
                    print(f"🔗 {job['url']}")
                    print(f"⚡ Easy Apply: {job['easy_apply']}\n")
                launch_ui(jobs)
            else:
                print("❌ No jobs found. Nothing to display.")

            browser.close()

    else:
        print("🔐 No cookies found. Launching manual login first...")
        manual_login()

if __name__ == "__main__":
    main()

