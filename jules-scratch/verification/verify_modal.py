from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct the absolute path to the HTML file
        html_file_path = os.path.abspath('index.html')

        page.goto(f'file://{html_file_path}')

        # Click the button to open the modal
        page.click('button.hero-button')

        # Wait for the modal to be visible
        page.wait_for_selector('.modal-overlay.is-open')

        # Take a screenshot of the modal
        modal = page.query_selector('.modal')
        if modal:
            modal.screenshot(path='jules-scratch/verification/screenshot.png')
        else:
            print("Modal not found")

        browser.close()

if __name__ == '__main__':
    run()
