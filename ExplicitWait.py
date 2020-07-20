from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="F:\ENGINEERING\Selenium\chromedriver.exe")

driver.get("https://www.expedia.co.in/")

driver.find_element(By.XPATH,"//a[@href='?pwaLOB=wizard-flight-pwa']").click()

driver.find_element(By.ID,"location-field-leg1-origin").send_keys("BOM")
driver.find_element(By.ID,"location-field-leg1-destination").send_keys("AMD")

