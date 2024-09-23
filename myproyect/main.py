from subclases.Coche import Coche
from subclases.Bicicleta import Bicicleta
from subsubclases.Motocicleta import Motocicleta
from subsubclases.Camioneta import Camioneta
import lanzador

if __name__ == "__main__":
    vehiculos = [] 
    lanzador.catalogar(lanzador.vehiculos)
