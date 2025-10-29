import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entry_nombre.get()
    edad = escala_edad.get()
    genero = var_genero.get()
    if nombre:
        lista_usuarios.insert(tk.END, f"{nombre} - {edad} años - {genero}")
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Introduce un nombre")

def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        lista_usuarios.delete(seleccion)
    else:
        messagebox.showinfo("Eliminar", "Selecciona un usuario para eliminar")

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Lista de usuarios guardada correctamente")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Lista de usuarios cargada correctamente")

def salir():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")
root.geometry("450x400")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
escala_edad.pack()

tk.Label(root, text="Género:").pack()
var_genero = tk.StringVar(value="Otro")
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

tk.Button(root, text="Añadir", command=añadir_usuario).pack(pady=5)

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista_usuarios = tk.Listbox(frame_lista, width=50, yscrollcommand=scroll.set)
lista_usuarios.pack()
scroll.config(command=lista_usuarios.yview)

tk.Button(root, text="Eliminar", command=eliminar_usuario).pack(pady=5)
tk.Button(root, text="Salir", command=salir).pack(pady=5)

barra_menu = tk.Menu(root)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=barra_menu)
root.mainloop()
