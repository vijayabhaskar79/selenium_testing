from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep, time

driver = webdriver.Chrome("E:\\Selenium\\chromedriver.exe")

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("q").send_keys(Keys.RETURN)

title = driver.title
print("Page title is : ", title)

a_class = driver.find_elements_by_class_name("srg")
print(a_class)

for x in a_class:
    print(x.text)

driver.close()