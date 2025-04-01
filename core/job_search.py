from playwright.sync_api import sync_playwright
from time import sleep
from core.utils import scroll_full_page, dump_html

def find_jobs(page, keyword, location="Remote", easy_apply_only=False):
    print(f"\n🔍 Searching LinkedIn Jobs for: '{keyword}' in '{location}' (Easy Apply Only: {easy_apply_only})")

    # Build search URL
    query = keyword.replace(" ", "%20")
    loc = location.replace(" ", "%20")
    url = f"https://www.linkedin.com/jobs/search/?keywords={query}&location={loc}"
    if easy_apply_only:
        url += "&f_AL=true"

    # Visit search URL
    page.goto(url)
    print("⏳ Waiting for job cards to load...")
    try:
        page.wait_for_selector("div.job-card-container", timeout=15000)
        print("✅ Job cards loaded.")
    except:
        print("⚠️ Job cards not detected — page may be blank or slow.")


    dump_html(page.content(), "debug_jobs_page.html")
    scroll_full_page(page, steps=3)

    selectors = [
        "li.jobs-search-results__list-item",
        "div.job-card-container",
        "div.job-card-list__title"
    ]

    jobs_found = []

    for selector in selectors:
        try:
            job_cards = page.locator(selector)
            count = job_cards.count()
            print(f"🧪 Selector '{selector}' → Found {count} cards.")

            if count > 0:
                for i in range(count):
                    try:
                        card = job_cards.nth(i)
                        title = company = location = posted = "N/A"
                        url = "#"
                        easy_apply = False

                        title_el = card.locator(".job-card-container__link span[aria-hidden]")
                        if title_el.count() > 0:
                            title = title_el.first.inner_text(timeout=3000)

                        company_el = card.locator(".job-card-container__company-name")
                        if company_el.count() > 0:
                            company = company_el.first.inner_text(timeout=3000)

                        location_el = card.locator(".job-card-container__metadata-item")
                        if location_el.count() > 0:
                            location = location_el.first.inner_text(timeout=3000)

                        posted_el = card.locator("time")
                        if posted_el.count() > 0:
                            posted = posted_el.first.inner_text(timeout=3000)

                        url_el = card.locator("a")
                        if url_el.count() > 0:
                            raw_href = url_el.first.get_attribute("href")
                            if raw_href and raw_href.startswith("/jobs/view/"):
                                url = "https://www.linkedin.com" + raw_href
                            else:
                                url = raw_href or "#"

                        # Easy Apply detection (case-insensitive)
                        easy_apply = "easy apply" in card.inner_text(timeout=3000).lower()

                        # Append job
                        jobs_found.append({
                            "title": title.strip(),
                            "company": company.strip(),
                            "location": location.strip(),
                            "posted": posted.strip(),
                            "url": url,
                            "easy_apply": easy_apply
                        })

                    except Exception as e:
                        print(f"⚠️ Failed to parse job card {i+1} for '{selector}': {e}")
                break  # If this selector worked, skip others

        except Exception as e:
            print(f"❌ Error with selector {selector}: {e}")

    print(f"\n✅ Total jobs found: {len(jobs_found)}")
    return jobs_found

