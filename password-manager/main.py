from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

#----------- Password Generator-------- #

def gen_paswrd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



def save():
    pwrd = password_entry.get()
    site = website_entry.get()
    mail = email_entry.get()

    

    if len(site) < 1 or len(pwrd) < 1:
        messagebox.showinfo(title="Error", message= "Hey!⚠️ Make sure you haven't left any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {mail} "
                           f"\nPassword: {pwrd} \nIs it okay to save?")
        with open("password-manager\data.txt", mode="a") as file:
            file.write(f"{site} | {mail} | {pwrd}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="password-manager\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1,row=0)

website = Label(text="Website:", font=25)
website.grid(column=0, row=1)

email = Label(text='Email/Username:', font=25)
email.grid(column=0, row=2)

password = Label(text="Password:", font=25)
password.grid(column=0, row=3)

website_entry = Entry(width=36)
website_entry.grid(row =1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(row =2, column=1, columnspan=2)
email_entry.insert(0, "nero@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row =3, column=1)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, columnspan=2, row=4)

generate_pswrd = Button(text="Generate Password", command=gen_paswrd)
generate_pswrd.grid(column=2,row=3)


window.mainloop()