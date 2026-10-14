from selenium.webdriver.common.by import By


class Locators:
    # Поле «Имя» в форме регистрации
    NAME_INPUT = (
        By.XPATH,
        "//label[text()='Имя']/following-sibling::input",
    )

    # Поле Email в формах регистрации и входа
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input",
    )

    # Поле «Пароль» в формах регистрации и входа
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка отправки формы регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Сообщение об ошибке короткого пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

    # Кнопка отправки формы входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка «Войти» в формах регистрации и восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Ссылка «Личный Кабинет» в шапке
    PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//a[.//p[text()='Личный Кабинет']]",
    )

    # Ссылка «Конструктор» в шапке
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[.//p[text()='Конструктор']]",
    )

    # Логотип Stellar Burgers в шапке
    LOGO_LINK = (
        By.XPATH,
        "//div[contains(@class, 'header__logo')]//a",
    )

    # Кнопка выхода в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Заголовок конструктора на главной странице
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Вкладка раздела «Булки»
    BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab')]//span[text()='Булки']/parent::div",
    )

    # Вкладка раздела «Соусы»
    SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab')]//span[text()='Соусы']/parent::div",
    )

    # Вкладка раздела «Начинки»
    FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab')]//span[text()='Начинки']/parent::div",
    )

    # Активная вкладка конструктора
    ACTIVE_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_type_current')]//span",
    )

