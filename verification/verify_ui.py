
from playwright.sync_api import sync_playwright
import os

def run():
    # Because this is a static file, we can just point to it.
    # However, to simulate "server" behavior or at least ensure file protocol works:
    file_path = os.path.abspath("src/index.html")
    url = f"file://{file_path}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate
        page.goto(url)

        # Verify Dark Mode is applied (check body background color)
        # slate-900 is rgb(15, 23, 42) or hex #0f172a
        body_bg = page.evaluate("window.getComputedStyle(document.body).backgroundColor")
        print(f"Body Background: {body_bg}")

        # Navigate to Methodology Tab
        page.click("button[onclick=\"switchTab('methodology')\"]")
        page.wait_for_timeout(500) # Wait for fade

        # Navigate to Viva Tab
        page.click("button[onclick=\"switchTab('viva')\"]")
        page.wait_for_timeout(500)

        # Verify Viva Section is visible
        viva_section = page.locator("#viva")
        if viva_section.is_visible():
            print("Viva Section is visible")

        # Screenshot
        page.screenshot(path="verification/viva_page.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
