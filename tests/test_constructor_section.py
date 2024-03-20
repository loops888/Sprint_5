from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestConstructorSection:
    """
    Проверка, что работает переход к разделу «Булки».
    """

    def test_transition_to_rolls_selector_show_rolls(self, driver):
        driver.find_element(*Locators.SAUCES_SELECTOR).click()
        driver.find_element(*Locators.ROLLS_SELECTOR).click()
        assert WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((Locators.ROLLS_SECTION)))

    """
    Проверка, что работает переход к разделу «Соусы».
    """

    def test_transition_to_sauces_selector_show_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_SELECTOR).click()
        assert WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((Locators.SAUCES_SECTION)))

    """
    Проверка, что работает переход к разделу «Начинки».
    """

    def test_transition_to_fillings_selector_show_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_SELECTOR).click()
        assert WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((Locators.FILLINGS_SECTION)))
