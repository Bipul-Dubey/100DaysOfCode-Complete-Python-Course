from tkinter import *
import tkinter.messagebox

window=Tk()
window.title('Tic Tac Toe - By Bipul')
window.iconbitmap('icon.ico')
window.resizable(False,False)
click=True
count=0

btn1=StringVar()
btn2=StringVar()
btn3=StringVar()
btn4=StringVar()
btn5=StringVar()
btn6=StringVar()
btn7=StringVar()
btn8=StringVar()
btn9=StringVar()

xPhoto=PhotoImage(file='cross.png')
oPhoto=PhotoImage(file='circle.png')


def press(num,r,c):
    global click,count
    if click:
        labelphoto=Label(window,image=xPhoto)
        labelphoto.grid(row=r,column=c)
        if num==1:
            btn1.set('X')
        if num==2:
            btn2.set('X')
        if num==3:
            btn3.set('X')
        if num==4:
            btn4.set('X')
        if num==5:
            btn5.set('X')
        if num==6:
            btn6.set('X')
        if num==7:
            btn7.set('X')
        if num==8:
            btn8.set('X')
        if num==9:
            btn9.set('X')
        count+=1
        click=False
        checkwin()
    else:
        labelphoto=Label(window, image=oPhoto)
        labelphoto.grid(row=r, column=c)
        if num==1:
            btn1.set('O')
        if num==2:
            btn2.set('O')
        if num==3:
            btn3.set('O')
        if num==4:
            btn4.set('O')
        if num==5:
            btn5.set('O')
        if num==6:
            btn6.set('O')
        if num==7:
            btn7.set('O')
        if num==8:
            btn8.set('O')
        if num==9:
            btn9.set('O')
        count+=1
        click=True
        checkwin()


def play():
    button1=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffe6f0',textvariable=btn1,command=lambda:press(1,0,0))
    button2=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffe6f0',textvariable=btn2,command=lambda:press(2,0,1))
    button3=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffe6f0',textvariable=btn3,command=lambda:press(3,0,2))
    button4=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffb3d1',textvariable=btn4,command=lambda:press(4,1,0))
    button5=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffb3d1',textvariable=btn5,command=lambda:press(5,1,1))
    button6=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ffb3d1',textvariable=btn6,command=lambda:press(6,1,2))
    button7=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ff80b3',textvariable=btn7,command=lambda:press(7,2,0))
    button8=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ff80b3',textvariable=btn8,command=lambda:press(8,2,1))
    button9=Button(window,height=9,width=19,bd=0.5,relief='ridge',bg='#ff80b3',textvariable=btn9,command=lambda:press(9,2,2))

    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)


def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')


def checkwin():
    global click,count
    if(btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
           btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
           btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
           btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
           btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
           btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
           btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
           btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):
        tkinter.messagebox.showinfo('tic tac toe','X Wins!!!')
        click=True
        count=0
        clear()
        play()

    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
             btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
             btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
             btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
             btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
             btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
             btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
             btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
        tkinter.messagebox.showinfo('tic tac toe', 'O Wins!!!')
        count=0
        clear()
        play()
    elif count==9:
        tkinter.messagebox.showinfo('tic tac toe','tie game!!!')
        click=True
        count=0
        clear()
        play()


play()
window.mainloop()
