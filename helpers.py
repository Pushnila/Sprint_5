import random
import string

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from locators import Locators


_generated_email_numbers = set()


def generate_email():
    """Генерирует email формата vlad_maximof_49_XXX@yandex.ru."""
    available_numbers = list(
        set(range(100, 1000)) - _generated_email_numbers
    )
    random_number = random.choice(available_numbers)
    _generated_email_numbers.add(random_number)
    return f"vlad_maximof_49_{random_number}@yandex.ru"


def generate_password(length=10):
    """Генерирует пароль длиннее минимально допустимых шести символов."""
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def generate_user_data():
    """Возвращает независимый набор данных для регистрации."""
    return {
        "name": TestData.USER_NAME,
        "email": generate_email(),
        "password": generate_password(),
    }


def register_user(driver, user):
    """Регистрирует нового пользователя через интерфейс приложения."""
    wait = WebDriverWait(driver, TestData.WAIT_TIMEOUT)
    driver.get(Urls.REGISTER)
    wait.until(
        expected_conditions.visibility_of_element_located(
            Locators.NAME_INPUT
        )
    )
    driver.find_element(*Locators.NAME_INPUT).send_keys(user["name"])
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
        user["password"]
    )
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    wait.until(expected_conditions.url_to_be(Urls.LOGIN))


def submit_login_form(driver, email, password):
    """Заполняет открытую форму входа и ждёт главную страницу."""
    wait = WebDriverWait(driver, TestData.WAIT_TIMEOUT)
    wait.until(
        expected_conditions.visibility_of_element_located(
            Locators.EMAIL_INPUT
        )
    )
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    wait.until(expected_conditions.url_to_be(Urls.BASE))
    wait.until(
        expected_conditions.visibility_of_element_located(
            Locators.CONSTRUCTOR_TITLE
        )
    )
