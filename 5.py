# 5. Una ciudad se diseño de tal modo que todas sus calles fueran de una sola vía. Con el paso del
# tiempo la cantidad de habitantes de la ciudad creció y esto produjo grandes trancones en algunas de
# las vias debido a algunos desvíos innecesarios que tienen que tomar los habitantes de la ciudad para
# poder llegar a sus trabajos. Por lo tanto, el alcalde tomó la decisión de ampliar algunas vias para que
# puedan convertirse en doble via. Dado el mapa de la ciudad y el costo de convertir cada via actual en
# doble via, determinar qué vias se deben convertir, de modo que se pueda transitar de cualquier punto
# a cualquier punto de la ciudad por dobles vias y que el costo de la conversión sea el mínimo posible.

# Estrategia:

# 1. Esto es basicamente un mst. Se puede usar el algoritmo de Prim para encontrar el árbol de expansión
# minimom que es el minimo costo para que todos los nodos estén conectados.

import heapq # Priority Queue

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, current_vertex, previous_vertex)

    while min_heap:
        cost, current_vertex, previous_vertex = heapq.heappop(min_heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if previous_vertex is not None:
                mst.append((previous_vertex, current_vertex, cost))

            for neighbor, weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current_vertex))

    return mst

# Ejemplo
# Grafo representado como un diccionario de listas de adyacencia
# Cada entrada es una lista de tuplas (Punto de la ciudad, costo de conversión)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
mst = prim(graph, start_vertex)

print("Vías que se deben convertir:")
for u, v, cost in mst:
    print(f"{u} - {v} con costo {cost}")