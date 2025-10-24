from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct the absolute file path
        file_path = "file://" + os.path.abspath("index.html")
        page.goto(file_path)

        # Click the "Order Service" button to open the modal
        page.click(".hero-button")

        # Wait for the modal to be visible
        page.wait_for_selector(".modal-overlay.is-open")

        # Take a screenshot of the modal
        page.screenshot(path="jules-scratch/verification/modal-screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
