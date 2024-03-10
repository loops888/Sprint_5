
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestPersonalAccount:
    """
    Проверка перехода по клику на «Личный кабинет».
    """
    def test_click_on_personal_account_personal_page_visible(self, login):
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.MAIN_PAGE)))
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_INFO_PAGE)))
        assert login.find_element(*Locators.PERSONAL_INFO_PAGE).is_displayed()

    """
    Проверка перехода из личного кабинета в конструктор по клику на «Конструктор».
    """
    def test_click_on_constructor_button_constructor_form_is_shown(self, login):
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.MAIN_PAGE)))
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_INFO_PAGE)))
        login.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert login.find_element(*Locators.CONSTRUCTOR_SECTION).is_displayed()

    """
    Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers.
    """
    def test_click_on_burger_logo_constructor_form_is_shown(self, login):
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.MAIN_PAGE)))
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_INFO_PAGE)))
        login.find_element(*Locators.BURGER_LOGO).click()
        assert login.find_element(*Locators.CONSTRUCTOR_SECTION).is_displayed()

    """
    Проверка выхода по кнопке «Выйти» в личном кабинете.
    """
    def test_click_on_exit_from_account_main_page_is_shown(self, login):
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.MAIN_PAGE)))
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 2).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_INFO_PAGE)))
        login.find_element(*Locators.EXIT_ACCOUNT_BUTTON).click()
        assert login.find_element(*Locators.LOGIN_WINDOW).is_displayed()
