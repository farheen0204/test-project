from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver = driver

        self.testbox_username_xpath = "//input[@name='username']"
        self.testbox_password_xpath = "//input[@name='password']"
        self.button_login_xpath = "//button[@type='submit']"
        self.testbox_invalid_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def input_username(self,Username):
        self.driver.find_element(By.XPATH, value = self.testbox_username_xpath ).send_keys(Username)
    def input_password(self,Password):
        self.driver.find_element(By.XPATH, value = self.testbox_password_xpath).send_keys(Password)
    def login_button(self):
        self.driver.find_element(By.XPATH,value = self.button_login_xpath).click()
    def invalid_credential(self):
        return self.driver.find_element(By.XPATH, value = self.testbox_invalid_xpath ).text