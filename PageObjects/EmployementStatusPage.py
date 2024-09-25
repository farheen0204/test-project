from selenium.webdriver.common.by import By

class EmpStatus:
    def __init__(self,driver):
        self.driver = driver

        self.button_add_xpath = "//button[normalize-space()='Add']"
        self.input_name_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.total_count_xpath = "//div[@class='oxd-table-card']"
        self.button_save_xpath = "//button[@type='submit']"
        self.already_exist_xpath = "//div[@class='oxd-table-card']/div/div[2]"
        self.delete_already_exist = "//div[@role='table']//div[1]//div[1]//div[3]//div[1]//button[1]//i[1]"
        self.driver.implicitly_wait(15)

    def click_add_button(self):
        self.driver.find_element(By.XPATH,value = self.button_add_xpath).click()

    def input_new_status(self,name):
        self.driver.find_element(By.XPATH, value= self.input_name_xpath).send_keys(name)

    def total_count(self):
        return self.driver.find_elements(By.XPATH, value = self.total_count_xpath)

    def click_save(self):
        self.driver.find_element(By.XPATH, value = self.button_save_xpath).click()

    def check_already_exist(self):
        return self.driver.find_element(By.XPATH, value = self.already_exist_xpath).text

    def click_delete_button(self):
        self.driver.find_element(By.XPATH, value=self.delete_already_exist).click()
