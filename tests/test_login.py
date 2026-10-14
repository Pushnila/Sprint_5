from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from helpers import submit_login_form
from locators import Locators


class TestLogin:
    def test_login_from_main_page_success(self, driver):
        driver.get(Urls.BASE)
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.LOGIN)
        )

        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )

        assert driver.current_url == Urls.BASE

    def test_login_from_personal_account_success(self, driver):
        driver.get(Urls.BASE)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.LOGIN)
        )

        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )

        assert driver.current_url == Urls.BASE

    def test_login_from_registration_form_success(self, driver):
        driver.get(Urls.REGISTER)
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.LOGIN)
        )

        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )

        assert driver.current_url == Urls.BASE

    def test_login_from_password_recovery_form_success(self, driver):
        driver.get(Urls.FORGOT_PASSWORD)
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.LOGIN)
        )

        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )

        assert driver.current_url == Urls.BASE
