from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe')

driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)

ele=driver.find_element_by_name("userName")

print(ele.is_displayed())
print(ele.is_enabled())

elepass=driver.find_element_by_name("password")
print(elepass.is_displayed())

print(elepass.is_enabled())

ele.send_keys("deepika")
elepass.send_keys("password")

driver.find_element_by_name("submit").click()



