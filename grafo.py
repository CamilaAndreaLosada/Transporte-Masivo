grafo = {
    # estaciones principal que se mantiene en linea
    "Portal Usme": {"Flores": 2},
    "Flores": {"Portal Usme": 2, "Kennedy": 2},
    "Kennedy": {"Flores": 2, "Calle 100": 1},
    "Calle 100": {"Kennedy": 1, "Héroes": 1},
    "Héroes": {"Calle 100": 1, "Nariño": 1, "Carrera 30": 2},
    "Nariño": {"Héroes": 1, "Las aguas": 1},
    "Las aguas": {"Nariño": 1, "Sevillana": 1},
    "Sevillana": {"Las aguas": 1},

    # estaciones secundarias que se mantiene el linea, pero se encuentra en la linea de la estaciones de linea principal
    "Portal 80": {"Boyacá": 2},
    "Boyacá": {"Portal 80": 2, "Av 68": 1},
    "Av 68": {"Boyacá": 1, "Carrera 30": 1},
    "Carrera 30": {"Av 68": 1, "Héroes": 2}
}
## rutas de transmilenio 