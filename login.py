import tkinter as tk

# Créer la fenêtre principale
app = tk.Tk()
app.geometry("400x240")

# Créer les étiquettes
username_label = tk.Label(
    app,
    text="Username",
    width=80,
    height=25,
    relief="solid",
    bd=1,
)
username_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

password_label = tk.Label(
    app,
    text="Password",
    width=80,
    height=25,
    relief="solid",
    bd=1,
)
password_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

# Créer les champs de saisie
username_entry = tk.Entry(app, width=20)
username_entry.place(relx=0.65, rely=0.3, anchor=tk.CENTER)

password_entry = tk.Entry(app, width=20, show="*")
password_entry.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

# Créer les boutons
login_button = tk.Button(
    app,
    text="Login",
    width=10,
    height=2,
    relief="solid",
    bd=1,
)
login_button.place(relx=0.71, rely=0.7, anchor=tk.CENTER)

signup_button = tk.Button(
    app,
    text="SignUp",
    width=10,
    height=2,
    relief="solid",
    bd=1,
)
signup_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Exécuter la boucle principale
app.mainloop()
