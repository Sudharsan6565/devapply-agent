# devapply_agent/core/scraper.py

from playwright.sync_api import sync_playwright
from core.session import launch_with_cookies
import time
import re

TARGET_KEYWORDS = [
    "hiring", "we are hiring", "looking for", "open position",
    "send your resume", "join our team", "we're hiring", "cloud engineer"
]

RECRUITER_TITLES = ["recruiter", "talent", "hr", "hiring", "people ops"]

def match_keywords(text):
    text = text.lower()
    return [kw for kw in TARGET_KEYWORDS if kw in text]

def is_recent(text):
    return any(k in text.lower() for k in ["h", "hour", "1d", "day", "minutes", "now"])

def is_probable_recruiter(author_name, title_text):
    if title_text:
        return any(role in title_text.lower() for role in RECRUITER_TITLES)
    return any(role in author_name.lower() for role in RECRUITER_TITLES)

def scrape_posts_by_hashtag(hashtag, scroll_count=5):
    browser, context, page = launch_with_cookies()
    if not page:
        return []

    tag_url = f"https://www.linkedin.com/feed/hashtag/{hashtag.strip('#')}/"
    print(f"🔍 Searching for posts: {tag_url}")
    page.goto(tag_url)
    time.sleep(5)

    posts = []

    for i in range(scroll_count):
        print(f"🔃 Scrolling... {i+1}/{scroll_count}")
        page.mouse.wheel(0, 5000)
        time.sleep(3)

    post_elements = page.locator("div.feed-shared-update-v2")
    count = post_elements.count()
    print(f"📦 Found {count} posts")

    for i in range(count):
        try:
            post = post_elements.nth(i)
            post_text = post.inner_text(timeout=5000)
            if not post_text.strip():
                continue

            matched = match_keywords(post_text)
            if not matched:
                continue

            timestamp = post.locator("span.feed-shared-actor__sub-description").inner_text(timeout=3000)
            if not is_recent(timestamp):
                continue

            author_elem = post.locator("span.feed-shared-actor__name")
            author = author_elem.inner_text(timeout=3000)
            profile_url = author_elem.locator("a").get_attribute("href")

            recruiter_title = post.locator("span.feed-shared-actor__description").inner_text(timeout=3000)
            recruiter_guess = is_probable_recruiter(author, recruiter_title)

            posts.append({
                "author": author,
                "profile_url": f"https://www.linkedin.com{profile_url}",
                "post_text": post_text[:500],  # limit
                "timestamp": timestamp,
                "is_recent": True,
                "matched_keywords": matched,
                "is_recruiter": recruiter_guess
            })

        except Exception as e:
            print(f"⚠️ Error scraping post {i}: {e}")
            continue

    browser.close()
    return posts

