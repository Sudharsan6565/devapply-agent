import time

def scroll_full_page(page, steps=3, delay=2):
    print()
    for i in range(steps):
        print(f"🔄 Scrolling full page... ({i + 1}/{steps})")
        page.mouse.wheel(0, 10000)
        time.sleep(delay)

def dump_html(content, filename="debug.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Dumped full HTML to {filename}")

