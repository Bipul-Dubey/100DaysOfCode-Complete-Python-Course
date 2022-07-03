import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image,ImageDraw

window=Tk()
window.title('Image Water Marker')
window.geometry('600x600')
window.config(padx=50,pady=50)

label=Label(text='WaterMarker',font=('BOLD',20))
label.grid(row=0,column=1)

lbl1=Label(window,text='Image.....')
lbl1.grid(row=1,column=0)

frn=Frame(window)
frn.grid(row=2,column=1)

lbl=Label(frn,text='Image Here ',font=('BOLD',40))
lbl.grid(row=2,column=1)

global i
demo_img=Image
def open_image():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetypes=(('JPG File','*.jpg'),
                                                                                               ('PNG File','*.png')))
    demo_img=Image.open(fln)
    demo_img.thumbnail((350,350))
    return demo_img


def add_watermark():
    i=0
    i+=1
    img=open_image()
    img_width,img_height=img.size

    draw_img=ImageDraw.Draw(img)
    text_image='Bipul_watermarker'
    if watermark_text.get()!='':
        text_image=watermark_text.get()

    text_width, text_height = draw_img.textsize(text_image)

    font_margin = 10
    x = img_width - text_width - font_margin
    y = img_height - text_height - font_margin

    draw_img.text((x, y), text_image, font_size=30)
    img2=ImageTk.PhotoImage(img)
    lbl.config(image=img2)
    lbl.image=img2


def save_image():
    pass


watermark_text=Entry(width=45)
watermark_text.grid(row=4,column=0,columnspan=2)
watermark_text.focus()


add_watermark_btn=Button(window,text='Browse Image - Add Water Mark',command=add_watermark)
add_watermark_btn.grid(row=5,column=1)

save_btn=Button(window,text='Save',command=save_image)
save_btn.grid(row=6,column=1)

exit_btn=Button(window,text='Exit',command=lambda :exit())
exit_btn.grid(row=6,column=2,pady=2,padx=5)


window.mainloop()
