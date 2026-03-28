#  Sistema Inteligente de Rutas - Transporte Masivo (TransMilenio)

##  Descripción del proyecto

Este proyecto implementa un **sistema inteligente basado en conocimiento** que permite encontrar la mejor ruta entre dos estaciones del sistema de transporte masivo de Bogotá.

Se utiliza el algoritmo de búsqueda heurística **A\*** (A estrella), el cual combina:
- Costo real del recorrido
- Estimación heurística hacia el destino

Esto permite encontrar rutas óptimas de manera eficiente.

---

##  Tecnologías y conceptos utilizados

- Python
- Algoritmo A*
- Búsqueda heurística
- Representación del conocimiento mediante grafos
- Validación de entrada de usuario

---

##  Estructura del proyecto

- `algoritmo.py` → Implementación del algoritmo A*
- `grafo.py` → Representación del sistema de estaciones y conexiones
- `heuristica.py` → Función heurística (estimación de distancia)
- `main.py` → Prueba básica del algoritmo
- `transporte_masivo_v2.py` →  Módulo mejorado con interacción de usuario

---

## Cómo ejecutar el programa

1. Ubicarse en la carpeta del proyecto:

```bash
cd ruta/del/proyecto
............................
2. Ejecutar el Sitema
python -u transporte_masivo_v2.py
..............................
Funcionalidades principales

✔ Selección de estación origen y destino
✔ Cálculo de la mejor ruta usando A*
✔ Cálculo del costo total del recorrido
✔ Validación de estaciones ingresadas
✔ Normalización de texto (mayúsculas/minúsculas)
✔ Soporte para alias (ejemplo: "av restrepo")
✔ Búsqueda en ambos sentidos (A → B y B → A)

Ejemplo de ejecución
Ingrese origen:
Portal Suba
Ingrese destino:
Portal Usme

Ruta encontrada: ['Portal Suba', 'Portal 80', 'Calle 26', 'Av Caracas', 'Restrepo', 'Portal Usme']
Costo total: 29
.....................................................
🆕 Mejoras implementadas (Versión 2)
Interfaz interactiva con el usuario
Manejo de errores en entradas
Normalización de texto
Inclusión de alias para estaciones
Cálculo automático del costo total de la ruta
.......................................................
Trabajo en equipo

Este proyecto fue desarrollado como parte de una actividad académica.
La versión actual incluye mejoras orientadas a la interacción con el usuario y robustez del sistema.

 Evidencia

El proyecto incluye:

Código fuente en Python
Documento PDF con pruebas realizadas
Video explicativo del funcionamiento del sistema
Conclusión

El uso del algoritmo A* demuestra cómo la inteligencia artificial puede aplicarse en problemas reales como la optimización de rutas en sistemas de transporte, mejorando la toma de decisiones y la eficiencia del sistema.


---