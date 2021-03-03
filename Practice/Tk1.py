import tkinter as tk

root=tk.Tk()
frame=tk.Frame(root,width=800,height=300)
button1=tk.Button(frame,text="Button 1")
button2=tk.Button(frame,text="Button 2")
button3=tk.Button(frame,text="Button 3")
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
frame.pack()

frame1=tk.Frame(root)
button4=tk.Button(frame1,text="Button 4")
button4.pack()
frame1.pack(side=tk.BOTTOM)




root.mainloop()
