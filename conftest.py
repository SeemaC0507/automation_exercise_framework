import pytest
from pages.login_page import LoginPage

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("sbd@xyz.com", "12345")
    return page