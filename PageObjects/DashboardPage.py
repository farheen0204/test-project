from selenium.webdriver.common.by import By


class dashboard:
    def __init__(self,driver):
        self.driver = driver

        self.testbox_dashboard_xpath = "//h6[normalize-space()='Dashboard']"
        self.button_admin_xpath = "//a[@href='/web/index.php/admin/viewAdminModule']"
        self.button_job_xpath = "//span[normalize-space()='Job']"
        self.button_employment_status_xpath = "//a[normalize-space()='Employment Status']"

        self.driver.implicitly_wait(15)

    def welcome_dashboard(self):
        return self.driver.find_element(By.XPATH,value = self.testbox_dashboard_xpath).text

    def click_admin(self):
        return self.driver.find_element(By.XPATH, value = self.button_admin_xpath)

    def click_job(self):
        return self.driver.find_element(By.XPATH,value = self.button_job_xpath)

    def click_emp_status(self):
        return self.driver.find_element(By.XPATH,value = self.button_employment_status_xpath)