class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, ciudad, carrera):
        super().__init__(nombre, edad, ciudad)
        self.carrera = carrera

    def hablar(self):
        super().hablar()
        print(f"Y estoy estudiando {self.carrera}")

persona1 = Persona("Juan", 25, "Bogotá")
estudiante1 = Estudiante("Ana", 20, "Cali", "Ingeniería")

persona1.hablar()
estudiante1.hablar()
