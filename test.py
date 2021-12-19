from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32_org\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")

driver.get("https://www.devopsalpham.com/")
print(driver.title)
