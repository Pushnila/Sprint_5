import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from helpers import submit_login_form
from locators import Locators


class TestPersonalAccount:
    def test_click_personal_account_opens_profile(self, driver):
        driver.get(Urls.LOGIN)
        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.PROFILE)
        )

        assert driver.current_url == Urls.PROFILE

    @pytest.mark.parametrize(
        "navigation_locator",
        [Locators.CONSTRUCTOR_LINK, Locators.LOGO_LINK],
        ids=["constructor-link", "stellar-burgers-logo"],
    )
    def test_from_profile_to_constructor_success(
        self, driver, navigation_locator
    ):
        driver.get(Urls.LOGIN)
        submit_login_form(
            driver, TestData.USER_EMAIL, TestData.USER_PASSWORD
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.url_to_be(Urls.PROFILE)
        )

        driver.find_element(*navigation_locator).click()
        title = WebDriverWait(driver, TestData.WAIT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                Locators.CONSTRUCTOR_TITLE
            )
        )

        assert driver.current_url == Urls.BASE and title.is_displayed()
