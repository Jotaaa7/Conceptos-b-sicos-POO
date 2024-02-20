class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado")

    def acelerar(self):
        print(f"El coche {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El coche {self.marca} {self.modelo} está frenando")

coche1 = Coche("Renault", "Megane", "Azul")
coche1.arrancar()
coche1.acelerar()
coche1.frenar()
