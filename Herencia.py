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

    def matricularse(self):
        print(f"{self.nombre} se ha matriculado en la carrera de {self.carrera}")

estudiante1 = Estudiante("Ana", 20, "Cali", "Ingeniería")
estudiante1.hablar()
estudiante1.matricularse()
