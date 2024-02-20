class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

persona1 = Persona("Juan", 25, "Bogotá")
persona1.hablar() # Mensaje
