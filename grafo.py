# grafo.py
# Representación del sistema de transporte como grafo

# Grafo base (una sola dirección)
grafo_base = {
    "Portal Suba": [("Portal 80", 5)],
    "Portal 80": [("Calle 26", 7)],
    "Calle 26": [("Av Caracas", 6)],
    "Av Caracas": [("Restrepo", 5)],
    "Restrepo": [("Portal Usme", 6)],
}

# Convertir a bidireccional automáticamente
grafo = {}

for origen in grafo_base:
    for destino, costo in grafo_base[origen]:

        grafo.setdefault(origen, []).append((destino, costo))
        grafo.setdefault(destino, []).append((origen, costo))