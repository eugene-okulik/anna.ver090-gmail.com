import random

from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()


def test_fill_out_form(
    page: Page,
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    email=fake.email(),
    state_name="NCR",
    city_name="Noida",
    mobile=fake.msisdn(),
    date_of_birth=fake.date_of_birth(
        minimum_age=18, maximum_age=99).strftime("%d %b %Y"),
    subject="Maths",
    address=fake.address()
):

    page.goto("https://demoqa.com/automation-practice-form")
    page.evaluate(
        "document.querySelector('#fixedban')?.remove()"
    )

    first_name_field = page.get_by_role(
        "textbox",
        name="First Name"
    )
    first_name_field.fill(first_name)

    last_name_field = page.get_by_role(
        "textbox", name="Last Name"
    )
    last_name_field.fill(last_name)

    email_field = page.locator("#userEmail")
    email_field.fill(email)

    random_gender = random.choice(["Male", "Female", "Other"])
    page.get_by_text(random_gender, exact=True).click()

    page.locator("#userNumber").fill(mobile)

    date_of_birth_field = page.locator('#dateOfBirthInput')
    expect(date_of_birth_field).to_be_visible()
    page.evaluate(
        f"navigator.clipboard.writeText('{date_of_birth}')"
    )
    date_of_birth_field.click(click_count=3)
    page.keyboard.press("Meta+V")
    page.keyboard.press("Tab")

    page.locator(".subjects-auto-complete__control").click()
    page.keyboard.type(subject)
    option = page.locator(".subjects-auto-complete__option")
    expect(option.first).to_be_visible(timeout=5000)
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    page.keyboard.press("Space")

    address_field = page.locator("#currentAddress")
    address_field.click()
    address_field.type(address, delay=20)
    page.keyboard.press("Tab")

    page.get_by_text("Select State").click()
    page.get_by_text(state_name, exact=True).click()

    page.get_by_text("Select City").click()
    page.get_by_text(city_name, exact=True).click()

    page.locator("#submit").click()

    expect(page.locator(
        "#example-modal-sizes-title-lg"
    )).to_be_visible()
