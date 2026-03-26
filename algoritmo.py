import heapq
from heuristica import heuristica

def aplicar_reglas(nodo, vecino, costo):

    # Simular tráfico
    if nodo == "Héroes":
        costo += 2

    # Penalización por transbordo
    if nodo == "Héroes" and vecino == "Carrera 30":
        costo += 1

    return costo


def astar(grafo, inicio, destino):
    cola = []
    heapq.heappush(cola, (0, inicio, []))

    visitados = set()

    while cola:
        costo, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]

        if nodo == destino:
            return camino, costo

        visitados.add(nodo)

        for vecino, peso in grafo[nodo].items():
            costo_real = aplicar_reglas(nodo, vecino, peso)
            nuevo_costo = costo + costo_real
            prioridad = nuevo_costo + heuristica(vecino, destino)

            heapq.heappush(cola, (prioridad, vecino, camino))

    return None, float("inf")
# Aqui se 