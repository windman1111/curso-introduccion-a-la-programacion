class coche():
    def __init__(self, puertas):
        self.puertas = puertas
    
    def mostrar_info(self):
	    print(f"El coche tiene {self.puertas} puerta") 
        
miCoche = coche(1)

miCoche.mostrar_info()