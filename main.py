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

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=PEACH)

canvas = Canvas(width=200, height=200, bg=PEACH, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", fg=ORANGE, font=(FONT_NAME, 12), bg=PEACH)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", fg=ORANGE, font=(FONT_NAME, 12), bg=PEACH)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg=ORANGE, font=(FONT_NAME, 12), bg=PEACH)
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



