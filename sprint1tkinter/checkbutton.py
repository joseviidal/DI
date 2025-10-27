import tkinter as tk

def actualizar():
    """Actualiza la etiqueta con las aficiones seleccionadas."""
    seleccionadas = []
    if var_leer.get() == 1:
        seleccionadas.append("Leer")
    if var_deporte.get() == 1:
        seleccionadas.append("Deporte")
    if var_musica.get() == 1:
        seleccionadas.append("Música")

    if seleccionadas:
        etiqueta_resultado.config(text="Aficiones: " + ", ".join(seleccionadas))
    else:
        etiqueta_resultado.config(text="Ninguna afición seleccionada.")

root = tk.Tk()
root.title("Ejercicio 4 - Checkbuttons")
root.geometry("400x250")

var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()

tk.Label(root, text="Selecciona tus aficiones:", font=("Arial", 12)).pack(pady=5)

tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar).pack()
tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar).pack()
tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar).pack()

etiqueta_resultado = tk.Label(root, text="Ninguna afición seleccionada.", font=("Arial", 11))
etiqueta_resultado.pack(pady=15)

root.mainloop()
