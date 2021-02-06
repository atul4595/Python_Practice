from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import XLUtils
import ctypes


from selenium.webdriver.common.keys import Keys
def on_open(Driver_P,Excel_P):
    driver = webdriver.Chrome(executable_path=Driver_P)
    # driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
    driver.get("http://quotes.toscrape.com/")
    driver.maximize_window()
    path=Excel_P
    # path=r"C://Users//Jayendra//Desktop//Selenium//Login.xlsx"
    # path=r"C://Users//Jayendra//Desktop//Selenium//Login.xlsx"
    print(path)
    driver.implicitly_wait(5)
    rows=XLUtils.getRowCount(path,"Sheet1")
    wait=WebDriverWait(driver,5)

    for r in range(2,rows+1):
        username=XLUtils.readData(path,"Sheet1",r,1)
        password=XLUtils.readData(path,"Sheet1",r,2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/p/a"))).click()
        driver.find_element(By.ID,"username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH,"/html/body/div/form/input[2]").click()
        # driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div[2]/p/a"))).click()
        XLUtils.writeData(path,"Sheet1",r,3,"Passed")
        # ctypes.windll.user32.MessageBoxW(0, "Your user Name:" + username, "Status", 0)
    driver.close()
    ctypes.windll.user32.MessageBoxW(0, "Done", "Status", 0)

# on_open()

