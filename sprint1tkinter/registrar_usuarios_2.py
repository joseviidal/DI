import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios - Clase")
        self.root.geometry("450x400")

        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Edad:").pack()
        self.escala_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.escala_edad.pack()

        tk.Label(root, text="Género:").pack()
        self.var_genero = tk.StringVar(value="Otro")
        tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="Masculino").pack()
        tk.Radiobutton(root, text="Femenino", variable=self.var_genero, value="Femenino").pack()
        tk.Radiobutton(root, text="Otro", variable=self.var_genero, value="Otro").pack()

        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack(pady=5)

        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.scroll = tk.Scrollbar(self.frame_lista)
        self.scroll.pack(side="right", fill="y")

        self.lista_usuarios = tk.Listbox(self.frame_lista, width=50, yscrollcommand=self.scroll.set)
        self.lista_usuarios.pack()
        self.scroll.config(command=self.lista_usuarios.yview)

        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack(pady=5)
        tk.Button(root, text="Salir", command=self.salir).pack(pady=5)

        self.barra_menu = tk.Menu(root)
        menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        root.config(menu=self.barra_menu)

    def añadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.escala_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista_usuarios.insert(tk.END, f"{nombre} - {edad} años - {genero}")
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Introduce un nombre")

    def eliminar_usuario(self):
        seleccion = self.lista_usuarios.curselection()
        if seleccion:
            self.lista_usuarios.delete(seleccion)
        else:
            messagebox.showinfo("Eliminar", "Selecciona un usuario para eliminar")

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Lista de usuarios guardada correctamente")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Lista de usuarios cargada correctamente")

    def salir(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
