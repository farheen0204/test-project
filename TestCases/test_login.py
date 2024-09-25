import pytest
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        log.info("TEST CASES 001")
        log.info("test cases starting")
        lg.input_username(config.get("credential","correct_username"))
        lg.input_password(config.get("credential","correct_password"))
        lg.login_button()

        if "Dashboard" in db.welcome_dashboard():
            assert True
            log.info("Test Case Pass")
        else:
            self.driver.save_screenshot('Screenshots/Testlogin_001.png')
            log.critical("Test case failed")
            assert False

    # def test_002(self):
    #     lg = Login(self.driver)
    #     db = dashboard(self.driver)
    #     lg.input_username("Amin")
    #     lg.input_password("admin123")
    #     lg.login_button()
    #     if "Invalid credentials" in lg.invalid_credential():
    #         assert True
    #     else:
    #         assert False
    #
    # def test_003(self):
    #     lg = Login(self.driver)
    #     db = dashboard(self.driver)
    #     lg.input_username("Amin")
    #     lg.input_password("admn123")
    #     lg.login_button()
    #     if "Invalid credentials" in lg.invalid_credential():
    #         assert True
    #     else:
    #         assert False
