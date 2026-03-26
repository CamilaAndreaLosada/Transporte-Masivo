from grafo import grafo
from algoritmo import astar

inicio = "Portal Usme"
destino = "Portal 80"

ruta, costo = astar(grafo, inicio, destino)

print("Ruta óptima:")
print(" -> ".join(ruta))
print("Costo total:", costo)

# ejecución del programa de transporte masivo