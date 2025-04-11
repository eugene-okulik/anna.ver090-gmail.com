from time import sleep
from playwright.sync_api import Page


def test_fill_out_login_form(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    form_authentication_field = page.get_by_role(
        'link', name='Form Authentication'
    )
    form_authentication_field.click()

    username_field = page.get_by_role(
        'textbox', name='username'
    )
    username_field.fill('user1')
    password_filed = page.get_by_role(
        'textbox', name='password'
    )
    password_filed.fill('qwert1234')
    page.get_by_role(
        'button'
    ).click()
    sleep(3)
