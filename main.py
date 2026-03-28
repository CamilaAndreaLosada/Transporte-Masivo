# main.py
# Prueba directa del algoritmo A* sin interacción

from algoritmo import a_estrella
from grafo import grafo
from heuristica import heuristica

ruta = a_estrella(grafo, heuristica, "Portal Suba", "Portal Usme")
print("Ruta encontrada:", ruta)