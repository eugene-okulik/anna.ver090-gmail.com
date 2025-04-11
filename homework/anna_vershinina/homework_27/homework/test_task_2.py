from playwright.sync_api import Page, expect, BrowserContext


def test_tabs(page: Page, context: BrowserContext):
    expected_text = 'I am a new page in a new tab'
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    new_tab_button = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        new_tab_button.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text(expected_text)
    new_page.close()
    expect(new_tab_button).to_be_enabled()
