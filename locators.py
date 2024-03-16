from selenium.webdriver.common.by import By


class Locators:
    # Ссылка на вход в "Личный Кабинет".
    PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")
    # Ссылка "Зарегистрироваться".
    REG_LINK = (By.LINK_TEXT, 'Зарегистрироваться')
    # Ссылка "Восстановить пароль".
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    # Главная страница сайта.
    MAIN_PAGE = (By.CLASS_NAME, "App_App__aOmNj")
    # Окно для авторизации пользователей.
    LOGIN_WINDOW = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Информация о пользователе из его личного кабинета.
    PERSONAL_INFO = (By.CLASS_NAME, "Account_contentBox__2CPm3")
    # Конструктор "Соберите бургер".
    CONSTRUCTOR_SECTION = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
    # Кнопка "Войти в  аккаунт" в главном окне.
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка "Войти" в окне авторизации.
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка "Выход" из личного кабинета пользователя.
    EXIT_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка "Зарегистрироваться" из формы Регистрации.
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Ссылка "Войти" из окна регистрации.
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    # Ссылка "Восстановить пароль" из окна авторизации.
    ENTER_FROM_RECOVERY = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    # Поле для ввода Имени из окна регистрации.
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@type='text']")
    # Поле для ввода Почты из окна регистрации.
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    # Поле для ввода Пароля из окна регистрации.
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']")
    # Надпись "Некорректный пароль".
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    # Кнопка "Конструктор".
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    # Логотип Stellar Burgers.
    BURGER_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    # Выбор раздела "Бургер".
    ROLLS_SELECTOR = (By.XPATH, "//span[contains(text(),'Булки')]")
    # Выбор раздела "Соусы".
    SAUCES_SELECTOR = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # Выбор раздела "Начинки".
    FILLINGS_SELECTOR = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Раздел с булками.
    ROLLS_SECTION = (By.XPATH, ".//span[text()='Булки']/ancestor::div[1]")
    # Раздел с соусами.
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/ancestor::div[1]")
    # Раздел с начинками.
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/ancestor::div[1]")
