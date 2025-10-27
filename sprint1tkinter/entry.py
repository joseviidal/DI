import tkinter as tk

def saludar():
    nombre = entrada.get()
    if nombre.strip() == "":
        etiqueta_resultado.config(text="Por favor, escribe tu nombre.")
    else:
        etiqueta_resultado.config(text=f"¡Hola, {nombre}! 😊")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")

etiqueta = tk.Label(root, text="Escribe tu nombre:", font=("Arial", 12))
etiqueta.pack(pady=5)

entrada = tk.Entry(root, font=("Arial", 12))
entrada.pack(pady=5)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta_resultado = tk.Label(root, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

root.mainloop()
