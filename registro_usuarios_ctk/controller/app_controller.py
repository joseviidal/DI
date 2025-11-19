from view.main_view import AddUserView, MainView
from model.usuario_model import Usuario, GestorUsuarios
from tkinter import messagebox
from pathlib import Path
import customtkinter as ctk

class AppController:
    def __init__(self, master):
        self.master = master
        self.model = GestorUsuarios()
        self.view = MainView(master)

        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"

        self.avatar_images = {}

        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario = self.model.obtener(indice)
        self.view.mostrar_detalles_usuario(usuario)

    def abrir_ventana_añadir(self):
        self.add_view = AddUserView(self.master)
        self.add_view.guardar_button.configure(
            command=lambda: self.añadir_usuario(self.add_view)
        )

    def añadir_usuario(self, add_view):
        datos = add_view.get_data()

        try:
            edad = int(datos["edad"])
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        nuevo = Usuario(
            datos["nombre"],
            edad,
            datos["genero"],
            datos["avatar"]
        )

        self.model._usuarios.append(nuevo)
        self.refrescar_lista_usuarios()
        add_view.window.destroy()

