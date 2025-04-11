from playwright.sync_api import Page, expect


def test_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.once('dialog', lambda dialog: dialog.accept())
    page.get_by_role('link', name='Click').click()
    expect(page.locator('.result-text')).to_have_text('Ok')
