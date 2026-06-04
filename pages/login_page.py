class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = page.locator("[data-qa='login-email']")
        self.password = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")
        self.error_message = page.locator("p[style='color: red;']")

    def goto(self):    
        self.page.goto("https://www.automationexercise.com/login")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        return self.page.get_by_text(" Logged in as ").is_visible()

    def get_error_message(self):
        return self.error_message.text_content()                 