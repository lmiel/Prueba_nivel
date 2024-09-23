from subclases.Coche import Coche
from subclases.Bicicleta import Bicicleta
from subsubclases.Motocicleta import Motocicleta
from subsubclases.Camioneta import Camioneta


vehiculos = []

vehiculo1 = Coche("azul", 4, 150, 1200)
vehiculos.append(vehiculo1)

vehiculo2 = Bicicleta("rojo", 2, "urbana")
vehiculos.append(vehiculo2)

vehiculo3 = Camioneta("blanco", 4, 100, 1300, 1500)
vehiculos.append(vehiculo3)

vehiculo4 = Motocicleta("gris", 2, "deportiva", 180, 900)
vehiculos.append(vehiculo4)


def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            
    



