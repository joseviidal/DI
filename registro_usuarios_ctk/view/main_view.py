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
