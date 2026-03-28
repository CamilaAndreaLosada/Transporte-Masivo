# algoritmo.py
# Implementación del algoritmo A* para encontrar la mejor ruta

import heapq  # Para manejar la cola de prioridad

def a_estrella(grafo, heuristica, inicio, destino):
    """
    grafo: diccionario con conexiones entre estaciones
    heuristica: función que estima distancia al destino
    inicio: estación inicial
    destino: estación final
    """

    cola = []  # Cola de prioridad
    heapq.heappush(cola, (0, inicio))

    costos = {inicio: 0}  # Costo acumulado
    padres = {inicio: None}  # Para reconstruir la ruta

    while cola:
        _, actual = heapq.heappop(cola)

        # Si llegamos al destino
        if actual == destino:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = padres[actual]
            return ruta[::-1]

        # Explorar vecinos
        for vecino, costo in grafo[actual]:
            nuevo_costo = costos[actual] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo

                # A* = costo real + heurística
                prioridad = nuevo_costo + heuristica(vecino, destino)

                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = actual

    return None