from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links are available",len(links))
print(links)
for li in reversed(links):
    print(li.text)
# driver.find_element(By.LINK_TEXT,"Report abuse").click()
wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div[2]/p/a")))
driver.find_element(By.LINK_TEXT,"Report abuse").click()

driver.close()
# driver.quit()
# driver.close()