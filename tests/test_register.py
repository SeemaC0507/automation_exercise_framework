from pages.register_page import RegisterPage

def test_signup_navigation(page):
    register_page = RegisterPage(page)
    register_page.goto()
    register_page.enter_signup_details("Test User", "testuser853@test.com")
    register_page.click_signup()
    assert register_page.is_on_signup_page() == True