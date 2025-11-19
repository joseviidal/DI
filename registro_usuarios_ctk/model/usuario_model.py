import csv
from pathlib import Path

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
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]

    def guardar_csv(self, ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["nombre", "edad", "genero", "avatar"])

            for u in self._usuarios:
                writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                reader = csv.reader(archivo)
                next(reader)

                self._usuarios.clear()

                for fila in reader:
                    try:
                        nombre, edad, genero, avatar = fila
                        self._usuarios.append(Usuario(nombre, int(edad), genero, avatar))
                    except:
                        pass
        except FileNotFoundError:
            pass