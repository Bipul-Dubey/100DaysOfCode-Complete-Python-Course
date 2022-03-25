from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    n_letters=randint(8,10)
    n_symbols=randint(2,4)
    n_numbers=randint(2,4)

    password_letters=[choice(letters) for i in range(n_letters)]
    password_symbols=[choice(symbols) for i in range(n_symbols)]
    password_number=[choice(numbers) for i in range(n_numbers)]

    password_list=password_number+password_letters+password_symbols
    shuffle(password_list)
    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=web_input.get()
    email=email_input.get()
    password=password_input.get()

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showwarning(title="Ooopppss!! Empty fields",message="hey, don't leave empty field")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are information entered: \nEmail: {email} \nPassword: {password}")
        if is_ok:
            with open("data.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                web_input.delete(0,END)
                password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)

web_input=Entry(width=35)
web_input.grid(row=1,column=1,columnspan=2)
web_input.focus()

username_label=Label(text="Email/Username: ")
username_label.grid(row=2,column=0)

email_input=Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"XYZ@gmail.com")


password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)

password_input=Entry(width=21)
password_input.grid(row=3,column=1)

gen_pass_button=Button(text="Generate Password",command=generate_password)
gen_pass_button.grid(row=3,column=2)

add_button=Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()