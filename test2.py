from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)


driver.get("https://www.devopsalpham.com/")
print(driver.title)

driver.back()
time.sleep(2)
print(driver.title)

driver.forward()
time.sleep(2)
print(driver.title)

