from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://demo.playwright.dev/todomvc")
        page.screenshot(path="playwright_screenshots/todomvc.png")
        assert "TodoMVC" in page.title()
        browser.close()