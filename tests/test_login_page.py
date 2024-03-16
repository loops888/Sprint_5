
from locators import Locators
from constants import Constants


class TestLogin:
    """
    Вход по кнопке «Войти в аккаунт» на главной.
    """
    def test_login_from_login_button_authorized_transition_to_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASS_CORRECT)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    """
    Вход через кнопку «Личный кабинет».
    """
    def test_login_from_personal_account_authorized_transition_to_main_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASS_CORRECT)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    """
    Вход через кнопку в форме регистрации.
    """
    def test_login_from_registration_form_authorized_transition_to_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASS_CORRECT)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()

    """
    Вход через кнопку в форме восстановления пароля.
    """
    def test_login_from_recovery_page_authorized_transition_to_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASS_CORRECT)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert driver.find_element(*Locators.MAIN_PAGE).is_displayed()
