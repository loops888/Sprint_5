from selenium.webdriver.common.by import By


class Locators:
    # Ссылка на вход в "Личный Кабинет".
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]")
    # Ссылка "Зарегистрироваться".
    REG_LINK = (By.LINK_TEXT, 'Зарегистрироваться')
    # Ссылка "Восстановить пароль".
    PASSWORD_RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    # Главная страница сайта.
    MAIN_PAGE = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]")
    # Окно для авторизации пользователей.
    LOGIN_WINDOW = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]")
    # Информация о пользователе из его личного кабинета.
    PERSONAL_INFO_PAGE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/nav[1]/ul[1]")
    # Конструктор "Соберите бургер".
    CONSTRUCTOR_SECTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]")
    # Кнопка "Войти в  аккаунт" в главном окне.
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка "Войти" в окне авторизации.
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка "Выход" из личного кабинета пользователя.
    EXIT_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка "Зарегистрироваться" из формы Регистрации.
    REGISTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]")
    # Ссылка "Войти" из окна регистрации.
    LOGIN_LINK = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]")
    # Ссылка "Восстановить пароль" из окна авторизации.
    ENTER_FROM_RECOVERY = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[2]/a[1]")
    # Поле для ввода Имени из окна регистрации.
    NAME_FIELD_REG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    # Поле для ввода Почты из окна регистрации.
    EMAIL_FIELD_REG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    # Поле для ввода Пароля из окна регистрации.
    PASSWORD_FIELD_REG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]")
    # Поле для ввода Почты из окна авторизации.
    EMAIL_FIELD_LOG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    # Поле для ввода Пароля из окна авторизации.
    PASSWORD_FIELD_LOG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    # Сообщение о некорректном пароле.
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]")
    # Кнопка "Конструктор".
    CONSTRUCTOR_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[1]/a[1]/p[1]")
    # Логотип Stellar Burgers.
    BURGER_LOGO = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")
    # Выбор раздела "Бургер".
    ROLLS_SELECTOR = (By.XPATH, "//span[contains(text(),'Булки')]")
    # Выбор раздела "Соусы".
    SAUCES_SELECTOR = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # Выбор раздела "Начинки".
    FILLINGS_SELECTOR = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Раздел с булками.
    ROLLS_SECTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[1]")
    # Раздел с соусами.
    SAUCES_SECTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[2]")
    # Раздел с начинками.
    FILLINGS_SECTION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[2]/ul[3]")
