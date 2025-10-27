import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡Texto cambiado correctamente!")

root = tk.Tk()
root.title("Ejercicio 1 - Labels")


etiqueta1 = tk.Label(root, text="¡Bienvenido/a a la interfaz Tkinter!", font=("Arial", 12))
etiqueta1.pack(pady=5)

etiqueta2 = tk.Label(root, text="José Vidal Fernández", font=("Arial", 11))
etiqueta2.pack(pady=5)

etiqueta3 = tk.Label(root, text="Texto original", font=("Arial", 11))
etiqueta3.pack(pady=5)

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

root.mainloop()
