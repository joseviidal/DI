from model.usuario_model import GestorUsuarios
from view.main_view import MainView
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



