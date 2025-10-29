import tkinter as tk

def cambiar_color():
    color = color_favorito.get()
    root.config(bg=color)

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")

color_favorito = tk.StringVar(value="white")

tk.Label(root, text="Elige tu color favorito:", font=("Arial", 12), bg="white").pack(pady=10)

# Radiobuttons
tk.Radiobutton(root, text="Rojo", variable=color_favorito, value="red", command=cambiar_color, bg="white").pack()
tk.Radiobutton(root, text="Verde", variable=color_favorito, value="green", command=cambiar_color, bg="white").pack()
tk.Radiobutton(root, text="Azul", variable=color_favorito, value="blue", command=cambiar_color, bg="white").pack()

root.mainloop()
