# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# Driver=webdriver.Chrome(r"C:\Users\Jayendra\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
# Driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# Driver.implicitly_wait(10)
# wait=WebDriverWait(Driver,10)
# wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label"))).click()
# # opt1.click()
# # Driver.find_element_by_id("RESULT_RadioButton-7_0").submit()
# # Driver.find_element(By.XPATH,"//*[@id='q26']/table/tbody/tr[1]/td/label").click()
# # print(status)
# # Driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()
#
# # status2=Driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
# # print(status2)
# # Driver.find_element(By.ID,"RESULT_RadioButton-7_1").click()
# time.sleep(5)
# Driver.close()
from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")

num_1 = StringVar()
num_2 = StringVar()


def addition():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    result = n1 + n2
    # print("Addition:",result)
    # lb_result.config(text="Your result is:"+" "+str(result))
    entry_1.insert(0, result)


def subtract():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    result = n1 - n2
    # print("Subtraction",result)
    # lb_result.config(text="Your result is:"+" "+str(result))
    entry_1.insert(0, result)


def multiply():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    result = n1 * n2
    # print("Multiplication:",result)
    # lb_result.config(text="Your result is:"+" "+str(result))
    entry_1.insert(0, result)


def division():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    result = n1 / n2
    # print("Division",result)
    # lb_result.config(text="Your result is:"+" "+str(result))
    entry_1.insert(0, result)


def modulus():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    result = n1 % n2
    # print("Modulus",result)
    # lb_result.config(text="Your result is:"+" "+str(result))
    entry_1.insert(0, result)


def exit_1():
    window.destroy()


def clear():
    number_1.delete(first=0, last=100)
    number_2.delete(first=0, last=100)


lb_1 = Label(window, text="Calculator", fg="red", bg="green", relief="solid", font=("arial", 20, "bold"))
lb_1.place(x=180, y=25)

number_1 = Entry(window, textvar=num_1)
number_1.place(x=260, y=95)
lb_2 = Label(window, text="Enter number 1", font=("arial", 14, "bold", "underline"))
lb_2.place(x=75, y=90)

number_2 = Entry(window, textvar=num_2)
number_2.place(x=260, y=145)
lb_3 = Label(window, text="Enter number 2", font=("arial", 14, "bold", "underline"))
lb_3.place(x=75, y=140)

# lb_result = Label(window)
# lb_result.place(x=275,y=400)

entry_1 = Entry(window)
entry_1.place(x=205, y=400)

button_1 = Button(window, text="Addition", width=12, bg="black", fg="white", command=addition)
button_1.place(x=150, y=200)

button_2 = Button(window, text="Subtaction", width=12, bg="black", fg="white", command=subtract)
button_2.place(x=280, y=200)

button_3 = Button(window, text="Multiplication", width=12, bg="black", fg="white", command=multiply)
button_3.place(x=150, y=250)

button_4 = Button(window, text="Division", width=12, bg="black", fg="white", command=division)
button_4.place(x=280, y=250)

button_5 = Button(window, text="Moddulus", width=12, bg="black", fg="white", command=modulus)
button_5.place(x=150, y=300)

button_6 = Button(window, text="Exit", width=12, bg="black", fg="white", command=exit_1)
button_6.place(x=280, y=300)

button_6 = Button(window, text="Clear Data", width=12, bg="black", fg="white", command=clear)
button_6.place(x=150, y=350)

window.mainloop()