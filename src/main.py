import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()

email = os.getenv("EMAIL_USER")
password = os.getenv("PASSWORD_USER")

# === FUNCTIONS ===
def get_user_password():
    """Aquí debe validar el email del usuario y su contraseña"""
    pass

# === TKINTER ===
ventana = tk.Tk()
ventana.title("Validar contraseñas")
ventana.geometry("300x300")

# == Email ==
label_email = tk.Label(ventana, text="Ingrese su correo electrónico")
label_email.pack()

entry_email = tk.Entry(ventana)
entry_email.pack()

# == Password ==
label_password = tk.Label(ventana, text="Ingrese su contraseña")
label_password.pack()

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()


# == Butón ==
button = tk.Button(ventana, text="Ingresar", command=get_user_password)
button.pack()


ventana.mainloop()
