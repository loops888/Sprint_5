
from locators import Locators
from constants import Constants


class TestRegistration:
    """
    Проверим успешную регистрацию пользователя с допустимым минимальным паролем — шесть символов.
    После завершения регистрации появится окна для логина.
    """
    def test_registration_with_correct_user_info_login_form_is_displayed(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(Constants.TEST_NAME)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(Constants.TEST_PASS_CORRECT)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.LOGIN_WINDOW).is_displayed()


    """
    Проверим ошибку регистрации пользователя при вводе пароля, длина которого меньше допустимого.
    В результате отобразится ошибка о некорректном пароле.
    """
    def test_registration_incorrect_password_incorrect_pasword_message(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(Constants.TEST_NAME)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(Constants.TEST_MAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(Constants.TEST_PASS_SHORT)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.find_element(*Locators.INCORRECT_PASSWORD_MESSAGE).is_displayed()
