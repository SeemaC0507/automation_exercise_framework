from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("sbd@xyz.com", "12345")
    assert login_page.is_logged_in()== True

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("hjkew@bck.com", "asdasd")
    assert "Your email or password is incorrect!" in login_page.get_error_message()   