class Persona:
    def __init__(self, nombre, edad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def obtener_imc(self):
        imc = self.calcular_imc()
        return f"El IMC de {self.nombre} es {imc}"

persona1 = Persona("Juan", 25, 1.75, 75)
imc = persona1.obtener_imc()
print(imc)
