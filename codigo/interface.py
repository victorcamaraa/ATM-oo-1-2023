import tkinter as tk
import MenuGerente
import MenuCliente

def fazer_login():
    MenuCliente.fazer_login()

def abrir_menu_gerente():
    # Lógica para abrir o menu do gerente
    pass

def sair():
    root.destroy()

root = tk.Tk()
root.title("Meu Programa")
root.geometry("300x200")

label = tk.Label(root, text="Menu")
label.pack()

button_login = tk.Button(root, text="Fazer login", command=fazer_login)
button_login.pack()

button_gerente = tk.Button(root, text="Gerente", command=abrir_menu_gerente)
button_gerente.pack()

button_sair = tk.Button(root, text="Sair", command=sair)
button_sair.pack()

root.mainloop()
