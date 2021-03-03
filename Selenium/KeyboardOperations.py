from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.thetestingworld.com/testings/")
driver.find_element(By.NAME,"fld_username").send_keys("Hello")
act=ActionChains(driver)
# act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("a").perform()
# driver.quit()