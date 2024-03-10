
from locators import Locators


class TestConstructorSection:
    """
    Проверка, что работает переход к разделу «Булки».
    """
    def test_transition_to_rolls_selector_show_rolls(self, driver):
        driver.find_element(*Locators.SAUCES_SELECTOR).click()
        driver.find_element(*Locators.ROLLS_SELECTOR).click()
        assert driver.find_element(*Locators.ROLLS_SECTION).is_displayed()

    """
    Проверка, что работает переход к разделу «Соусы».
    """
    def test_transition_to_sauces_selector_show_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_SELECTOR).click()
        assert driver.find_element(*Locators.SAUCES_SECTION).is_displayed()

    """
    Проверка, что работает переход к разделу «Начинки».
    """
    def test_transition_to_fillings_selector_show_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_SELECTOR).click()
        assert driver.find_element(*Locators.FILLINGS_SECTION).is_displayed()
