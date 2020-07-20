from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\ENGINEERING\Selenium\chromedriver.exe")

driver.get("http://timesheet.aqmtechnologies.com/")

uname_ele=driver.find_element_by_id("txtUserName")
print(uname_ele.is_displayed())
print(uname_ele.is_enabled())

pass_ele=driver.find_element_by_id("txtPassword")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

uname_ele.send_keys("shivang.swadia")
pass_ele.send_keys("Shivang@123")

driver.find_element_by_id("btnLogin").click()

driver.find_element_by_xpath("//a[@href='EmployeeTimesheetCalender.aspx']").click()

decimal_radio=driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_rbTimeFormat_0']")
print("Status of decimal radio button",decimal_radio.is_selected())

hrmm_radio=driver.find_element_by_xpath("//input[@id='ctl00_ContentPlaceHolder1_rbTimeFormat_1']")
print("Status of HRMM radio button",hrmm_radio.is_selected())

time.sleep(2)
driver.close()