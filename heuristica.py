import math
from datos import estaciones

def heuristica(nodo, destino):
    x1, y1 = estaciones[nodo]
    x2, y2 = estaciones[destino]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)