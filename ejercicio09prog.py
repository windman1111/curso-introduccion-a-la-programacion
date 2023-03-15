class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono,credito):
        Persona.__init__(nombre, edad, telefono,credito)
        self.credito = credito

cliente01 = Cliente("Andrés", "19", "456434454", "1000")

print(f"El cliente {cliente01.nombre} tiene {cliente01.edad} años, su número de teléfono es {cliente01.telefono} y tiene un crédito de {cliente01} euros")
