# Archivo: artista.py
class Artista:
    """Clase que representa a un artista en el contexto de Soundwave."""
    def __init__(self, id_artista, nombre, genero, popularidad, redes):
        self.id_artista = id_artista
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad  # Un atributo adicional para Soundwave
        self.redes = redes

    def __str__(self):
        return (f"ID: {self.id_artista}, Nombre: {self.nombre}, Género: {self.genero}, "
                f"Popularidad: {self.popularidad}, Redes: {', '.join(self.redes)}")

# Archivo: crud.py
from artista import Artista

class CRUDArtista:
    """Clase para gestionar operaciones CRUD de artistas en Soundwave."""
    def __init__(self):
        self.artistas = []

    def crear_artista(self, id_artista, nombre, genero, popularidad, redes):
        nuevo_artista = Artista(id_artista, nombre, genero, popularidad, redes)
        self.artistas.append(nuevo_artista)
        print(f"Artista {nombre} creado exitosamente.")

    def leer_artistas(self):
        if not self.artistas:
            print("No hay artistas registrados.")
        for artista in self.artistas:
            print(artista)

    def actualizar_artista(self, id_artista, nombre=None, genero=None, popularidad=None, redes=None):
        for artista in self.artistas:
            if artista.id_artista == id_artista:
                if nombre:
                    artista.nombre = nombre
                if genero:
                    artista.genero = genero
                if popularidad:
                    artista.popularidad = popularidad
                if redes:
                    artista.redes = redes
                print(f"Artista {id_artista} actualizado exitosamente.")
                return
        print(f"Artista con ID {id_artista} no encontrado.")

    def eliminar_artista(self, id_artista):
        for artista in self.artistas:
            if artista.id_artista == id_artista:
                self.artistas.remove(artista)
                print(f"Artista {id_artista} eliminado exitosamente.")
                return
        print(f"Artista con ID {id_artista} no encontrado.")

# Archivo: main.py
from crud import CRUDArtista

def menu():
    print("""
    ==== SOUNDWAVE: Gestión de Artistas ====
    1. Crear Artista 🎤
    2. Leer Artistas 📋
    3. Actualizar Artista ✏️
    4. Eliminar Artista 🗑️
    5. Salir 🚪
    """)

def main():
    crud = CRUDArtista()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_artista = input("ID del Artista: ")
            nombre = input("Nombre del Artista: ")
            genero = input("Género Musical: ")
            popularidad = input("Popularidad (1-100): ")
            redes = input("Redes Sociales (separadas por coma): ").split(',')
            crud.crear_artista(id_artista, nombre, genero, popularidad, redes)

        elif opcion == "2":
            crud.leer_artistas()

        elif opcion == "3":
            id_artista = input("ID del Artista a actualizar: ")
            nombre = input("Nuevo Nombre (deja en blanco para no cambiar): ")
            genero = input("Nuevo Género (deja en blanco para no cambiar): ")
            popularidad = input("Nueva Popularidad (deja en blanco para no cambiar): ")
            redes = input("Nuevas Redes (separadas por coma, deja en blanco para no cambiar): ")
            redes = redes.split(',') if redes else None
            crud.actualizar_artista(id_artista, nombre, genero, popularidad, redes)

        elif opcion == "4":
            id_artista = input("ID del Artista a eliminar: ")
            crud.eliminar_artista(id_artista)

        elif opcion == "5":
            print("Saliendo del programa. ¡Gracias por usar Soundwave!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
