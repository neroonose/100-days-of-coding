KM = 1.60934
from tkinter import *

def button_clicked():
    figure = input.get()
    result = round(float(figure) * KM)
    answer.config(text=result)

window = Tk()
window.title("🔘🔘🔘 Mile to Km Converter")
window.minsize(width=400, height=80)
window.config(padx=50, pady=50)

#Label
is_equal_to = Label(text="is equal to",font=("Arial", 15))
is_equal_to.grid(column=0,row=1)

miles = Label(text="Miles",font=("Arial", 15))
miles.grid(column=2,row=0)

km = Label(text="Km",font=("Arial", 15))
km.grid(column=2,row=1)

answer = Label(text="0",font=("Arial", 13))
answer.grid(column=1,row=1)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1,row=2)

input = Entry(width=7)
input.insert(END, string= "0")
input.grid(column=1,row=0)





window.mainloop()