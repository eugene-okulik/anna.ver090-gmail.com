import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_submit_form(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Submit me"]'
    )
    send_text = 'Phone'
    text_string.send_keys(send_text)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == send_text
