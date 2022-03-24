import tkinter

window=tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500,height=500)


# label
my_label=tkinter.Label(text="I'm Label",font=("Arial",24,"bold"))     # create label
my_label.pack(side="top")         # visible label on screen

# text on screen
# my_label["text"]="New Text"
my_label.config(text="New_Text")

def button_click():
    # my_label.config(text="clicked..")
    text=input.get()
    my_label.config(text=text)
# button

button=tkinter.Button()
button.pack()
button.config(text="Click Me",command=button_click)


# inputs/entry
input=tkinter.Entry()
input.pack()
# input.get() # to get input from entry

# text box
text=tkinter.Text(width=10,height=10)
text.pack()

# number spinbox
spinbox=tkinter.Spinbox(from_=0,to=10,width=5)
spinbox.pack()

# number scale
scale=tkinter.Scale(from_=1,to=20,width=10)
scale.pack()

# check box
var=tkinter.IntVar()
check_box=tkinter.Checkbutton(text="Is On?? ",variable=var)
check_box.pack()

# radiao button
radio_state=tkinter.IntVar()
radio_button=tkinter.Radiobutton(text="Option1",value=1,variable=radio_state)
radio_button2=tkinter.Radiobutton(text="Option2",value=2,variable=radio_state)
radio_button.pack()
radio_button2.pack()

# list box
listbox=tkinter.Listbox(height=4)
fruits=["apple",'grapes','banana','orange']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.pack()


window.mainloop()