from subclases.Coche import Coche
from subclases.Bicicleta import Bicicleta

if __name__ == "__main__":
    coche = Coche("azul", 4, 150, 1200)
    print(coche)
    
    bicicleta = Bicicleta("rojo", 2, "urbana")
    print(bicicleta)
