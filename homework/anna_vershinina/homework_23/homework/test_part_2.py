from random import randint, choice

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def test_fill_out_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script("document.body.style.zoom='60%'")

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.click()
    first_name.send_keys('John')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.click()
    last_name.send_keys('Doe')

    email = driver.find_element(By.ID, 'userEmail')
    email.click()
    email.send_keys('JohnDoe@gmail.com')

    gender = driver.find_element(
        By.CSS_SELECTOR,
        f'label[for="gender-radio-{randint(1, 3)}"]'
    )
    gender.click()

    phone_number = driver.find_element(By.ID, 'userNumber')
    phone_number.click()
    rand_num = ''.join(str(randint(0, 9)) for _ in range(10))
    phone_number.send_keys(rand_num)

    dob_form = driver.find_element(By.ID, 'dateOfBirthInput')
    dob_form.click()

    # selecting month
    month_selector = driver.find_element(
        By.CLASS_NAME, 'react-datepicker__month-select'
    )
    select_month = Select(month_selector)
    rand_month = randint(0, 1)
    select_month.select_by_index(rand_month)

    # selecting year
    year_selector = driver.find_element(
        By.CLASS_NAME, 'react-datepicker__year-select'
    )
    select_year = Select(year_selector)
    rand_year = str(randint(1910, 2008))
    select_year.select_by_value(rand_year)

    # selecting day
    day_selector = driver.find_elements(
        By.CSS_SELECTOR,
        'div.react-datepicker__day[aria-disabled="false"]'
    )
    rand_day = choice(day_selector)
    rand_day.click()

    subjects = driver.find_element(
        By.ID, 'subjectsInput'
    )
    subjects.click()
    subjects.send_keys('Math')
    subjects.send_keys(Keys.TAB)
    subjects.send_keys('Bio')
    subjects.send_keys(Keys.TAB)

    hobbies = driver.find_element(
        By.CSS_SELECTOR,
        f'label[for="hobbies-checkbox-{randint(1, 3)}"]'
    )
    hobbies.click()

    address = driver.find_element(
        By.ID, 'currentAddress'
    )
    address.click()
    address.send_keys('New York, 7th street')

    select_state = driver.find_element(
        By.XPATH,
        '//div[text()="Select State"]'
    )
    select_state.click()
    state = driver.find_element(By.XPATH, '//div[text()="Uttar Pradesh"]')
    # I was not able to perform random state & city select - how to do this?
    """states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    rand_state = choice(states)
    state.send_keys(rand_state)"""
    state.click()

    select_city = driver.find_element(
        By.XPATH,
        '//div[text()="Select City"]'
    )
    select_city.click()
    city = driver.find_element(
        By.XPATH,
        '//div[text()="Agra"]'
    )
    city.click()

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    table_text = {}
    rows = driver.find_elements(
        By.XPATH,
        '//table[contains(@class, "table-dark")]//tr'
    )

    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) >= 2:
            label = cells[0].text
            value = cells[1].text
            table_text[label] = value

    for label, value in table_text.items():
        print(f"{label}: {value}")
