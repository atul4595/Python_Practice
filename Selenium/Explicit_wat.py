from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
# driver = webdriver.Ie(r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\IEDriverServer.exe")
driver.get("https://www.amazon.in/")
# driver.find_element(By.NAME,"q").send_keys("Atul")
# driver.find_element(By.XPATH,"//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[1]").click()
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='leftNav']/ul[2]/div/li/span/span/div/label/input")))
element.click()
# driver.find_element(By.ID,"location-field-leg1-origin-input").send_keys("Atul")
time.sleep(5)
# driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a/span").click()
driver.close()
