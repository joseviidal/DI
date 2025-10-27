import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón de mensaje!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 2 - Botones")

etiqueta = tk.Label(root, text="", font=("Arial", 12))
etiqueta.pack(pady=10)

boton_mensaje = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=5)

root.mainloop()
