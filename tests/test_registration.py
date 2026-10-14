from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from helpers import generate_user_data, register_user
from locators import Locators


class TestRegistration:
    def test_registration_valid_data_redirects_to_login(self, driver):
        user = generate_user_data()

        register_user(driver, user)

        assert driver.current_url == Urls.LOGIN

    def test_registration_short_password_shows_error(self, driver):
        user = generate_user_data()
        driver.get(Urls.REGISTER)
        driver.find_element(*Locators.NAME_INPUT).send_keys(user["name"])
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(
            TestData.INVALID_PASSWORD
        )
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.PASSWORD_ERROR
            )
        )

        assert error.text == TestData.PASSWORD_ERROR_TEXT

