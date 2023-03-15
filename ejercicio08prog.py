class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

persona = Persona(18, "Andres", 64787858)

print(persona.edad)