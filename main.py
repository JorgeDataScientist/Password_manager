from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
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

# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO 2.1: Guardar datos de entrada que provienen de la interfas de usuario
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password}"
                                                              f" \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

#TODO 1.1: Creando Interfas de Usuario, Titulo, Pading
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#TODO 1.2: COnfigurando Imagen
canvas = Canvas(height=200, width=200)  #alto y ancho de ventana
logo_img = PhotoImage(file="logo.png")  #Guardo en variable Imagen de aplicacion
canvas.create_image(100, 100, image=logo_img)   #Posicionamiento: X, Y  +  imagen
canvas.grid(row=0, column=1)    #Posicion de imagen

#TODO 1.3: Etiquetas
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#TODO 1.4: Entradas de datos
website_entry = Entry(width=43)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()   #para que el cursor inicie en esta entrada en particular
email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# TODO 1.5: Botones
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=15, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()   #Ejecutor de Ventana