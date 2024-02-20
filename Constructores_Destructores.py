class Persona:
    def __init__(self, nombre, edad, ciudad):
        print(f"Se ha creado un objeto de la clase Persona")
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __del__(self):
        print(f"Se ha eliminado un objeto de la clase Persona")

persona1 = Persona("Juan", 25, "Bogotá")

del persona1
