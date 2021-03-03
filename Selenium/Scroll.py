from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

Driver=webdriver.Chrome(executable_path=r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
Driver.maximize_window()
Driver.implicitly_wait(5)
Driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
# Scroll Down page by pixel
# Driver.execute_script("window.scrollBy(0,1000)","")
# Scroll Down page till the element is visible
# flag=Driver.find_element(By.XPATH,"//*[@id='q11']/label")
# Driver.execute_script("arguments[0].scrollIntoView();",flag)
Driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")