class Persona:
    def __init__(self, nombre, edad, ciudad):
        self._nombre = nombre # Atributo privado
        self.edad = edad
        self.ciudad = ciudad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

persona1 = Persona("Juan", 25, "Bogotá")

print(persona1.nombre) # Obtener el nombre

persona1.nombre = "Ana" # Modificar el nombre

print(persona1.nombre)
