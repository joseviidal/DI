class Usuario:
    def __init__(self, nombre, edad, genero, avatar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

class GestorUsuarios:
    def __init__ (self):
        self._usuarios = []

    def _cargar_datos_De_ejemplo(self):
        self._usuarios.append(Usuario("José Vidal", 20, "Masculino", "avatarJoseVidal.jpeg"))
        self._usuarios.append(Usuario("Carlitos Mendez", 35, "Masculino", "avatarCarlitosMendez.jpeg"))

    def listar(self):
        return self._usuarios