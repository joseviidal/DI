import tkinter as tk
from tkinter import messagebox

def mostrar_fruta():
    seleccion = lista_frutas.curselection()
    if seleccion:
        fruta = lista_frutas.get(seleccion)
        etiqueta_resultado.config(text=f"Has seleccionado: {fruta}")
    else:
        messagebox.showwarning("Atención", "Selecciona una fruta primero")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")

tk.Label(root, text="Selecciona una fruta:", font=("Arial", 12)).pack(pady=10)

lista_frutas = tk.Listbox(root, font=("Arial", 11))
frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
for fruta in frutas:
    lista_frutas.insert(tk.END, fruta)
lista_frutas.pack(pady=10)

tk.Button(root, text="Mostrar fruta", command=mostrar_fruta).pack(pady=5)

etiqueta_resultado = tk.Label(root, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

root.mainloop()
