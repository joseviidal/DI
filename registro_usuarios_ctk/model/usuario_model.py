import csv

class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__ (self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("José Vidal", 20, "Masculino", "avatarJoseVidal.jpeg"))
        self._usuarios.append(Usuario("Carlitos Mendez", 35, "Masculino", "avatarCarlitosMendez.jpeg"))

    def listar(self):
        return self.usuarios

    def obtener(self, indice):
        return self.usuarios[indice]

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)