import tkinter as tk
import Excel
# from tkinter import ttk
from tkinter import filedialog
# from tkinter import *
from PIL import ImageTk ,Image
# from functools import partial

root=tk.Tk()
root.geometry("600x260")
# Mainframe=F``     rame(root,width=600,height=260)
filename = ''
filename1 = ''
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          filetypes=(("All Files",
                                                      "*.*"),
                                                     ("Text Files",
                                                      "*.txt*")))
    # text1.insert(0,filename)
    text1.insert(tk.END, filename)
    # Entry(root,text = filename).place(x=220,y=80)
    # print("filename:",filename)



# browseFiles()
# print("filename:",filename)
# a=filename
# text1 = Entry(root).place(x=220, y=80)
# text1.insert(100,a)
def browseFiles1():
    global filename1
    filename1 = filedialog.askopenfilename(initialdir="/",
                                        title="Select a File",
                                           filetypes=(("All Files",
                                                       "*.*"),
                                                      ("Text Files",
                                                       "*.txt*")))
    text2.insert(tk.END, filename1)

tk.Label(root,text="Automation Test",font="comicsansms 25 bold").place(x=200,y=15)
File_P=tk.Label(root,text="Enter excel file Location").place(x=10,y=80)
Web_l=tk.Label(root,text="Enter Selenium Driver Location").place(x=10,y=120)

photo1 = Image.open("Filw.jpg")
photo1=photo1.resize((80,20),Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(photo1)
button1= tk.Button(root,text="Browse Files",command=browseFiles,height=15,width=70,image=photoImg).place(x=500,y=80)

photo2 = Image.open("Google_Chrome_icon-icons.com_75711.ico")
photo2=photo2.resize((80,20),Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(photo2)

button2= tk.Button(root,text="Browse Files",command=browseFiles1,height=15,width=70,image=photoImg2).place(x=500,y=120)

# button3= Button(root,text="Start",command=Excel.on_open(),height=1,width=10).place(x=250,y=180)
# root.browseFile(filename)
def Work():
    Excel.on_open(filename1,filename)

def exit():
    root.destroy()

text1=tk.Text(root,height=1,width=32)
text1.place(x=220,y=80)

text2=tk.Text(root,height=1,width=32)
text2.place(x=220,y=120)

button3= tk.Button(root,text="Start",command=Work,height=1,width=10).place(x=250,y=180)
button4= tk.Button(root,text="Exit",command=exit,height=1,width=10).place(x=350,y=180)

# text1.insert(INSERT,filename)
# text1=Entry(root,width=40)


# rt=text1.get("1.0",'end-1c')
#
# print(rt)
root.mainloop()
