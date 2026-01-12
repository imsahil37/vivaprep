
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly since it's static
        file_path = os.path.abspath("src/index.html")
        page.goto(f"file://{file_path}")

        # Scroll to the simulator section
        simulator = page.locator("#simulator-section")
        simulator.scroll_into_view_if_needed()

        # Wait a bit for any transitions
        page.wait_for_timeout(500)

        # Take a screenshot
        page.screenshot(path="verification/viva_simulator.png")
        print("Screenshot saved to verification/viva_simulator.png")

        # Verify elements are present
        assert page.locator("#apiKey").is_visible()
        assert page.locator("#generateBtn").is_visible()
        assert page.locator("#questionContainer").is_hidden()

        browser.close()

if __name__ == "__main__":
    run()
