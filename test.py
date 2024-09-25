from selenium import webdriver

#driver = webdriver.Chrome(executable_path="/Users/arpitkhare/Downloads/chromedriver")

from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
