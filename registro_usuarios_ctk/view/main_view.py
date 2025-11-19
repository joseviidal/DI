import customtkinter as ctk
import tkinter

class MainView:
    def __init__(self, master):
        self.master = master

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(master)
        self.lista_usuarios_scrollable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.detalles_frame = ctk.CTkFrame(master)
        self.detalles_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_nombre = ctk.CTkLabel(self.detalles_frame, text="Nombre:")
        self.label_nombre.pack(anchor="w")

        self.label_edad = ctk.CTkLabel(self.detalles_frame, text="Edad:")
        self.label_edad.pack(anchor="w")

        self.label_genero = ctk.CTkLabel(self.detalles_frame, text="Género:")
        self.label_genero.pack(anchor="w")

        self.avatar_label = ctk.CTkLabel(self.detalles_frame, text="")
        self.avatar_label.pack(pady=10)

    def actualizar_lista_usuarios(self, usuarios, on_select_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_select_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")


class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x300")
        self.window.grab_set()

        self.nombre_entry = ctk.CTkEntry(self.window, placeholder_text="Nombre")
        self.nombre_entry.pack(pady=5)

        self.edad_entry = ctk.CTkEntry(self.window, placeholder_text="Edad")
        self.edad_entry.pack(pady=5)

        self.genero_entry = ctk.CTkEntry(self.window, placeholder_text="Género")
        self.genero_entry.pack(pady=5)

        self.avatar_entry = ctk.CTkEntry(self.window, placeholder_text="Nombre avatar.png")
        self.avatar_entry.pack(pady=5)

        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(pady=10)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_entry.get(),
            "avatar": self.avatar_entry.get()
        }
