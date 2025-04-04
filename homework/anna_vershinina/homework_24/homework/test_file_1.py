import platform
import pytest
from random import choice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='60%'")
    return driver


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')

    all_products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, 'a.hrefch')))

    selected_product = choice(all_products)
    selected_product_name = selected_product.text

    key = Keys.COMMAND if platform.system() == 'Darwin' else Keys.CONTROL

    (
        ActionChains(driver)
        .key_down(key)
        .click(selected_product)
        .key_up(key)
        .perform()
    )

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((
        By.LINK_TEXT, 'Add to cart'))).click()
    alert = Alert(driver)
    WebDriverWait(driver, 2).until(
        EC.alert_is_present()
    )
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()

    product_in_cart = (
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//a[contains(@onclick, "deleteItem")]/ancestor::tr/td[2]'
                )
            )
        )
    )
    assert product_in_cart.text == selected_product_name


def test_2(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    bag = driver.find_element(
        By.PARTIAL_LINK_TEXT,
        'Push It Messenger Bag'
    )
    selected_product_name = bag.text
    compare_button = driver.find_element(
            By.XPATH,
            f'//a[contains(text(), "{
                selected_product_name
                }")]/ancestor::li//a[@class="action tocompare"]'
    )
    actions = ActionChains(driver)
    actions.move_to_element(bag)
    actions.click(compare_button)
    actions.perform()

    product_to_compare = (
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH, '//*[@id="compare-items"]/li/strong/a'
                )
            )
        )
    )

    assert product_to_compare.text == selected_product_name
