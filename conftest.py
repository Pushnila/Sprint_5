import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Открывает Chrome для теста и гарантированно закрывает его."""
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
