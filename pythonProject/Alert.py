from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
# driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()

time.sleep(10)
driver.quit()

