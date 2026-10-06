import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData, Urls
from locators import Locators


class TestConstructor:
    @pytest.mark.parametrize(
        (
            "target_locator, preliminary_locator, "
            "preliminary_section, expected_section"
        ),
        [
            (
                Locators.BUNS_TAB,
                Locators.SAUCES_TAB,
                "Соусы",
                "Булки",
            ),
            (
                Locators.SAUCES_TAB,
                Locators.FILLINGS_TAB,
                "Начинки",
                "Соусы",
            ),
            (
                Locators.FILLINGS_TAB,
                Locators.SAUCES_TAB,
                "Соусы",
                "Начинки",
            ),
        ],
        ids=["buns", "sauces", "fillings"],
    )
    def test_click_ingredient_tab_activates_section(
        self,
        driver,
        target_locator,
        preliminary_locator,
        preliminary_section,
        expected_section,
    ):
        driver.get(Urls.BASE)
        wait = WebDriverWait(driver, TestData.WAIT_TIMEOUT)

        wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.CONSTRUCTOR_TITLE
            )
        )

        driver.find_element(*preliminary_locator).click()
        wait.until(
            expected_conditions.text_to_be_present_in_element(
                Locators.ACTIVE_TAB,
                preliminary_section,
            )
        )

        driver.find_element(*target_locator).click()
        active_tab = wait.until(
            expected_conditions.visibility_of_element_located(
                Locators.ACTIVE_TAB
            )
        )

        assert active_tab.text == expected_section