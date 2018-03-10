from  tkinter import*
from eval1 import*
def Display(text,button,display):
    button.configure(bg='red')
    button.after(500, lambda: button.configure(bg='white'))
    Displaytext = display.get()
    txtLength = len(Displaytext)
    if Displaytext == '0':
        display.delete(0,END)
        display.insert(0,text)
    else:
        display.insert(txtLength,text)
        
def Buttons(display):
    sevBtn = Button(font=('Ubuntu',11),text='7',bg='#FFFFFF',borderwidth=0,command=lambda:Display('7',sevBtn,display))
    sevBtn.grid(row=1,column=0,sticky='NWNESWSE')


    eigBtn = Button(font=('Ubuntu', 11), text='8',bg='#FFFFFF', borderwidth=0,command=lambda:Display('8',eigBtn,display))
    eigBtn.grid(row=1, column=1, sticky='NWNESWSE')

    ninBtn = Button(font=('Ubuntu', 11), text='9', bg='#FFFFFF',borderwidth=0,command=lambda:Display('9',ninBtn,display))
    ninBtn.grid(row=1, column=2, sticky='NWNESWSE')

    divBtn = Button(font=('Ubuntu', 11), text='/',bg='#FFFFFF', borderwidth=0,command=lambda:Display('/',divBtn,display))
    divBtn.grid(row=1, column=3, sticky='NWNESWSE')

    clrBtn = Button(font=('Ubuntu', 11), text='C', bg='#FFFFFF',borderwidth=0,command=lambda:clr(display))
    clrBtn.grid(row=1, column=4, sticky='NWNESWSE')

    forBtn = Button(font=('Ubuntu', 11), text='4',bg='#FFFFFF', borderwidth=0,command=lambda:Display('4',forBtn,display))
    forBtn.grid(row=2, column=0, sticky='NWNESWSE')

    fivBtn = Button(font=('Ubuntu', 11), text='5',bg='#FFFFFF', borderwidth=0,command=lambda:Display('5',fivBtn,display))
    fivBtn.grid(row=2, column=1, sticky='NWNESWSE')

    sixBtn = Button(font=('Ubuntu', 11), text='6',bg='#FFFFFF', borderwidth=0,command=lambda:Display('6',sixBtn,display))
    sixBtn.grid(row=2, column=2, sticky='NWNESWSE')

    mulBtn = Button(font=('Ubuntu', 11), text='*', bg='#FFFFFF',borderwidth=0,command=lambda:Display('*',mulBtn,display))
    mulBtn.grid(row=2, column=3, sticky='NWNESWSE')

    perBtn = Button(font=('Ubuntu', 11), text='%', bg='#FFFFFF',borderwidth=0,command=lambda:Display('%',perBtn,display))
    perBtn.grid(row=2, column=4, sticky='NWNESWSE')

    oneBtn = Button(font=('Ubuntu', 11), text='1',bg='#FFFFFF', borderwidth=0,command=lambda:Display('1',oneBtn,display))
    oneBtn.grid(row=3, column=0, sticky='NWNESWSE')

    twoBtn = Button(font=('Ubuntu', 11), text='2',bg='#FFFFFF', borderwidth=0,command=lambda:Display('2',twoBtn,display))
    twoBtn.grid(row=3, column=1, sticky='NWNESWSE')

    thrBtn = Button(font=('Ubuntu', 11), text='3',bg='#FFFFFF', borderwidth=0,command=lambda:Display('3',thrBtn,display))
    thrBtn.grid(row=3, column=2, sticky='NWNESWSE')

    subBtn = Button(font=('Ubuntu', 11), text='-',bg='#FFFFFF', borderwidth=0,command=lambda:Display('-',subBtn,display))
    subBtn.grid(row=3, column=3, sticky='NWNESWSE')

    eqlBtn = Button(font=('Ubuntu', 11), text='=',bg='#FFFFFF', borderwidth=0,command=lambda:eql(display))
    eqlBtn.grid(row=3, column=4, sticky='NWNESWSE',rowspan=2)

    zroBtn = Button(font=('Ubuntu', 11), text='0', bg='#FFFFFF',borderwidth=0,command=lambda:Display('0',zroBtn,display))
    zroBtn.grid(row=4, column=0, sticky='NWNESWSE',columnspan=2)

    decBtn = Button(font=('Ubuntu', 11), text='.', bg='#FFFFFF',borderwidth=0,command=lambda:Display('.',decBtn,display))
    decBtn.grid(row=4, column=2, sticky='NWNESWSE')

    addBtn = Button(font=('Ubuntu', 11), text='+', bg='#FFFFFF',borderwidth=0,command=lambda:Display('+',addBtn,display))
    addBtn.grid(row=4, column=3, sticky='NWNESWSE')
