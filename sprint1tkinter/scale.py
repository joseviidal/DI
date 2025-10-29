import tkinter as tk

def actualizar(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

root = tk.Tk()
root.title("Ejercicio 11 - Scale")
root.geometry("400x200")

escala = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
escala.pack(pady=20)

etiqueta = tk.Label(root, text="Valor seleccionado: 0")
etiqueta.pack()

root.mainloop()
