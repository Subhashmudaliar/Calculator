from  tkinter import*
from Buttons import*


root = Tk()
display = Entry(font=('Ubuntu',16),relief=RAISED,justify=RIGHT)
display.insert(0,'0')
display.grid(row=0,column=0,columnspan=5)
Buttons(display)
root.mainloop()
