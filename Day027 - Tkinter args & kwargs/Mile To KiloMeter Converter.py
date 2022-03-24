from tkinter import *

window=Tk()
window.minsize(width=300,height=200)
window.title("Mile to KiloMeter Convertor")
window.config(padx=40,pady=40)

# miles input
mile_input=Entry(width=7)
mile_input.grid(row=1,column=2)

mile_label=Label(text="Miles",font=("arial",10,"bold"))
mile_label.grid(row=1,column=3)

is_equal_label=Label(text="Is Equal to ",font=("arial",10,"bold"))
is_equal_label.grid(row=2,column=1)

km_label=Label(text="Km",font=("arial",10,"bold"))
km_label.grid(row=2,column=3)

km_result_label=Label(text="0",font=("arial",10,"bold"))
km_result_label.grid(row=2,column=2)

def MileToKm():
    miles=float(mile_input.get())
    km=miles*1.609
    km_result_label.config(text=f"{km}")


calc_button=Button(text="Calculate",command=MileToKm)
calc_button.grid(row=3,column=2)

window.mainloop()