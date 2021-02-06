from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()
# wait=WebDriverWait(driver,10)
admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usermgnt=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()
driver.quit()

