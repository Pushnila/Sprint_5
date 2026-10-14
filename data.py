class Urls:
    BASE = "https://stellarburgers.education-services.ru/"
    LOGIN = f"{BASE}login"
    REGISTER = f"{BASE}register"
    FORGOT_PASSWORD = f"{BASE}forgot-password"
    PROFILE = f"{BASE}account/profile"


class TestData:
    USER_NAME = "Владислав"
    USER_EMAIL = "vlad_maximof_49_315@yandex.ru"
    USER_PASSWORD = "Stellar315"
    INVALID_PASSWORD = "12345"
    PASSWORD_ERROR_TEXT = "Некорректный пароль"
    WAIT_TIMEOUT = 15
