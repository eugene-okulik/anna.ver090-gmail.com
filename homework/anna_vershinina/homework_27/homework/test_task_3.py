from playwright.sync_api import Page, expect


def test_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.get_by_role('button', name='Color Change')
    expect(button).to_have_css("color", "rgb(220, 53, 69)")
    button.click()
