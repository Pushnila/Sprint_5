from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from helpers import submit_login_form
from locators import Locators


class TestLogout:
    def test_logout_from_personal_account_redirects_to_login(self, driver):
        driver.get(Urls.LOGIN)
        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.PROFILE)
        )

        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.LOGIN)
        )

        assert driver.current_url == Urls.LOGIN
