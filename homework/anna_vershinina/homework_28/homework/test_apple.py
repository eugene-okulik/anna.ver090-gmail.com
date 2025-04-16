import re
from playwright.sync_api import Page, expect, Route


def test_replace_iphone(page: Page):

    def handle_route(route: Route, new_text):
        response = route.fetch()
        body = response.text()
        modified = re.sub(
            r"iPhone\s?16\s?Pro",
            new_text,
            body
        )

        route.fulfill(
            response=response,
            body=modified
            )

    new_text = 'яблокофон 16 про'
    page.route(
        "**/shop/api/digital-mat?path=library/step0_iphone/digitalmat",
        lambda route: handle_route(route, new_text)
    )
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone_selector = page.locator(
        'h3:has-text("iPhone 16 Pro Max")'
    )
    iphone_selector.click()
    phone_name = page.locator(
        '[data-autom="DigitalMat-overlay-header-0-0"]'
    )
    expect(phone_name).to_have_text('яблокофон 16 про')
