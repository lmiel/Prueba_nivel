from subclases.Coche import Coche
from subclases.Bicicleta import Bicicleta
from subsubclases.Motocicleta import Motocicleta
from subsubclases.Camioneta import Camioneta


if __name__ == "__main__":
    vehiculo1 = Coche("azul", 4, 150, 1200)
    print(vehiculo1)
    
    vehiculo2 = Bicicleta("rojo", 2, "urbana")
    print(vehiculo2)

    vehiculo3 = Camioneta("blanco", 4, 100, 1300, 1500)
    print(vehiculo3)

    vehiculo4 = Motocicleta("gris", 2, "deportiva", 180, 900)
    print(vehiculo4)
