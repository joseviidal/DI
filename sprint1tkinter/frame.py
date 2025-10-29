import tkinter as tk

def mostrar_texto():
    etiqueta_resultado.config(text=entrada.get())

def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")
root.geometry("400x250")

frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

tk.Label(frame_superior, text="Introduce texto:").grid(row=0, column=0, padx=5, pady=5)
entrada = tk.Entry(frame_superior)
entrada.grid(row=0, column=1, padx=5, pady=5)
etiqueta_resultado = tk.Label(frame_superior, text="")
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=10)

frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto).grid(row=0, column=0, padx=10)
tk.Button(frame_inferior, text="Borrar", command=borrar_texto).grid(row=0, column=1, padx=10)

root.mainloop()
