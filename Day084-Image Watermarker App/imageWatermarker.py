from tkinter import *
from PIL import ImageTk,Image

window=Tk()
window.title('Image Water Marker')
window.geometry('800x500')

label=Label(text='Insert WaterMark',font=('BOLD',20))
label.grid(row=0,column=3)

label_insert_img=Label(text='Insert image Here...',font=('BOLD',12))
label_insert_img.grid(row=1,column=0)

window.mainloop()
