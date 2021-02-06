from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

# driver=webdriver.Chrome(ChromeDriverManager().install())
# chr=r"‪C:/Users/Jayendra/Desktop/Selenium/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Ie(r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\IEDriverServer.exe")
driver.get("http://newtours.demout.com/")
driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title
# driver.back()
# driver.forward()
# pwd_ele=driver.find_element_by_name("Password")
# pwd_ele.is_enabled()
# pwd_ele.is_displayed()
# pwd_ele.is_selected()
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.close()

