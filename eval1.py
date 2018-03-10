from tkinter import*
def clr(display):
    display.delete(0,END)
    display.insert(0,'0')

def eql(display):
    exp = display.get()
    exp = exp.replace('%','/100')
    try:
        display.delete(0, END)
        res  = eval(exp)
        display.insert(0, res)
    except:
        display.delete(0, END)
        res = "Invalid input"
        display.insert(0,res)
