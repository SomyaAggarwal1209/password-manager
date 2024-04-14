from tkinter import *

PINK = "#FFB6B9"
PEACH = "#FAE3D9"
GREEN = "#BBDED6"
TEAL = "#61C0BF"

BLUE = "#2B2E4A"
ORANGE = "#E84545"
MAROON = "#903749"
BROWN = "#53354A"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        added_label = Label(text="Password Added Successfully!", fg=GREEN, font=(FONT_NAME, 8, "bold"), bg=PEACH)
        added_label.grid(row=0, column=1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=PEACH)

canvas = Canvas(width=200, height=200, bg=PEACH, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", fg=BLUE, font=(FONT_NAME, 12), bg=PEACH)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", fg=BLUE, font=(FONT_NAME, 12), bg=PEACH)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg=BLUE, font=(FONT_NAME, 12), bg=PEACH)
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dummy_email@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



