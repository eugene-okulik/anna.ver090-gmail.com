from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_no_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = Select(driver.find_element(By.ID, 'id_choose_language'))
    options = dropdown.options[1:]
    rand_index = randint(1, len(options) - 1)
    dropdown.select_by_index(rand_index)
    selected_lang = dropdown.options[rand_index].text
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == selected_lang


def test_no_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    hello_world = WebDriverWait(driver, 7).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4'))
    )

    assert hello_world.text == 'Hello World!'
