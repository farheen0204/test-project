from selenium.webdriver import ActionChains

from PageObjects.DashboardPage import dashboard
from PageObjects.LoginPage import Login
from PageObjects.EmployementStatusPage import EmpStatus
import pytest
import time

@pytest.mark.usefixtures("setup")
class Testdashboad:
    def test_001(self):
        lg = Login(self.driver)
        db = dashboard(self.driver)
        es = EmpStatus(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.login_button()
        #db.click_admin()

        ActionChains(self.driver).move_to_element(db.click_admin()).click().perform()
        ActionChains(self.driver).move_to_element(db.click_job()).click().perform()
        ActionChains(self.driver).move_to_element(db.click_emp_status()).click().perform()
        old_status_count = 0
        new_status_count = 0
        for i in es.total_count():
            old_status_count = old_status_count + 1
        print("Old status",old_status_count)
        es.click_add_button()
        es.input_new_status("Automation Tester")
        es.click_save()
        for i in es.total_count():
            new_status_count = new_status_count + 1
        if  new_status_count == old_status_count + 1:
            assert True
        else:
            assert False
