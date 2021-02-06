import tkinter as tk

class myButtons:
    def __init__(self,master):
        self.Button1=tk.Button(master,text='Print',command=self.printmessage)
        self.Button1.pack(side=tk.LEFT)

        self.Button2=tk.Button(master,text='Quit',command=master.quit)
        self.Button2.pack(side=tk.LEFT)

    def printmessage(self):
        print("Tkinter class")


root=tk.Tk()
first=myButtons(root)
second=myButtons(root)
root.mainloop()