from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="F:\ENGINEERING\Selenium\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.facebook.com")

print(driver.title)

driver.find_element_by_xpath("//input[@name="firstname"]")

time.sleep(3)

driver.quit()
