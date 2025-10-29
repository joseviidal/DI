import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Has seleccionado 'Abrir'")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación creada por Josito para Carlangas")

root = tk.Tk()
root.title("Ejercicio 9 - Menú")
root.geometry("400x250")

barra_menu = tk.Menu(root)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=barra_menu)
root.mainloop()
