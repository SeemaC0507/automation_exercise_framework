class RegisterPage:
    def __init__(self,page):
        self.page = page
        self.name = page.locator("[data-qa='signup-name']")
        self.email = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")

    def goto(self):    
        self.page.goto("https://www.automationexercise.com/login")

    def enter_signup_details(self, name, email):
        self.name.fill(name)
        self.email.fill(email)

    def click_signup(self):
        self.signup_button.click()

    def is_on_signup_page(self):
        return self.page.get_by_text("Enter Account Information").is_visible()   
      
    