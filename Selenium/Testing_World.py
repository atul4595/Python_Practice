from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings/")
driver.find_element(By.NAME,"fld_username").send_keys("Atul")
driver.find_element(By.NAME,"fld_email").send_keys("test@gmail.com")
driver.find_element(By.NAME,"fld_password").send_keys("abcd123")
driver.find_element(By.NAME,"fld_cpassword").send_keys("abcd123")
# driver.find_element(By.NAME,"fld_username").send_keys("abcd123")
driver.find_element(By.XPATH,"//*[@id='tab-content1']/form/input[9]").click()
driver.find_element(By.XPATH,"//*[@id='tab-content1']/form/div/input[1]").click()
driver.find_element(By.XPATH,"//*[@id='tab-content1']/form/div/input[2]").click()
time.sleep(5)
driver.close()