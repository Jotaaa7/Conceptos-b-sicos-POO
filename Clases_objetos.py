class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

persona1 = Persona("Juan", 25, "Bogotá")
persona2 = Persona("María", 30, "Medellín")

persona1.hablar()
persona2.comer()
