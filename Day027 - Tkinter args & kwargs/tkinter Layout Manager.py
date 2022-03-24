from tkinter import *

window=Tk()
window.title("My Window")
window.minsize(width=500,height=500)
window.config(padx=20,pady=20)

# label
my_label=Label(text="My Label",font=("Arial",22,"bold"))
my_label.config(text="Label")
# my_label.pack()
# my_label.place(x=10,y=10)   # place takes coordinates and place at that coordinate
my_label.grid(column=0,row=0)       # grid takes row and column and adjust at that position

# button
button=Button(text='Click')
button.grid(row=1,column=1)

button2=Button(text='Click')
button2.grid(row=0,column=2)


# Entry
input=Entry()
input.grid(row=2,column=3)


window.mainloop()