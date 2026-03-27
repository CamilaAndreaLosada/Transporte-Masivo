from algoritmo import a_estrella
from grafo import grafo
from heuristica import heuristica

# Función para calcular el costo total de la ruta
def calcular_costo(ruta):
    costo = 0
    for i in range(len(ruta) - 1):
        for vecino, peso in grafo[ruta[i]]:
            if vecino == ruta[i + 1]:
                costo += peso
    return costo

# Normalizar texto
def normalizar(texto):
    return texto.strip().lower()

def ejecutar():
    print("=== SISTEMA DE RUTAS TRANSMILENIO ===\n")

    print("Estaciones disponibles:")
    for estacion in grafo.keys():
        print("-", estacion)

    # Entrada
    inicio = normalizar(input("\nIngrese origen: "))
    destino = normalizar(input("Ingrese destino: "))

    # Mapeo correcto
    mapa = {k.lower(): k for k in grafo.keys()}

    if inicio not in mapa or destino not in mapa:
        print("\nError: estación no válida")
        return

    inicio_real = mapa[inicio]
    destino_real = mapa[destino]

    # Ejecutar A*
    ruta = a_estrella(grafo, heuristica, inicio_real, destino_real)

    if ruta:
        print("\nRuta encontrada:", ruta)
        print("Costo total:", calcular_costo(ruta))
    else:
        print("\nNo se encontró ruta")

if __name__ == "__main__":
    ejecutar()
