import pytest
from pages.login_page import LoginPage
import os
import pytest
pytestmark = pytest.mark.skipif(os.getenv("CI") == "true", reason="Blocked on CI")

@pytest.mark.parametrize("email, password, expected", [
    ("sbd@xyz.com", "12345", True),
    ("wrong@email.com", "wrongpass", False),
    ("bademail", "12345", False),
])

def test_login_scenarios(page, email, password, expected):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(email, password)
    assert login_page.is_logged_in() == expected