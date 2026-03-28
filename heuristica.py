# heuristica.py
# Heurística basada en distancia euclidiana (simulación geográfica)

import math

# Coordenadas simuladas de estaciones
estaciones = {
    "Portal Suba": (0, 5),
    "Portal 80": (2, 5),
    "Calle 26": (4, 4),
    "Av Caracas": (6, 3),
    "Restrepo": (7, 2),
    "Portal Usme": (8, 0)
}

def heuristica(nodo, destino):
    x1, y1 = estaciones[nodo]
    x2, y2 = estaciones[destino]

    # Distancia euclidiana
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)