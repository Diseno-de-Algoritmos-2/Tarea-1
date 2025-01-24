# Daniel vargas
# Santiago Bobadilla
# Lina Ariza

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DESCRIPCIÓN DEL PROBLEMA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5. Una ciudad se diseño de tal modo que todas sus calles fueran de una sola vía. Con el paso del
# tiempo la cantidad de habitantes de la ciudad creció y esto produjo grandes trancones en algunas de
# las vias debido a algunos desvíos innecesarios que tienen que tomar los habitantes de la ciudad para
# poder llegar a sus trabajos. Por lo tanto, el alcalde tomó la decisión de ampliar algunas vias para que
# puedan convertirse en doble via. Dado el mapa de la ciudad y el costo de convertir cada via actual en
# doble via, determinar qué vias se deben convertir, de modo que se pueda transitar de cualquier punto
# a cualquier punto de la ciudad por dobles vias y que el costo de la conversión sea el mínimo posible.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DATOS DE ENTRADA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# La entrada consiste en un archivo de texto llamado input.txt que contiene la información.
# La estructura del archivo es la siguiente:
#   Via I: (Nodo I, Costo I), (Nodo II, Costo II), (Nodo III, Costo III)
#   Via II: (Nodo I, Costo I), (Nodo II, Costo II)
#   Via III: (Nodo I, Costo I), (Nodo III, Costo III), (Nodo IV, Costo IV)
# Para cada línea, el primer nodo es la vía y los nodos que le siguen son los nodos a los que se conecta con su peso.

import os

# Obtenemos la ruta del archivo actual (ruta relativa a la ubicación del archivo dentro del computador).
current_dir = os.path.dirname(os.path.abspath(__file__))
# Añadimos a la ruta del archivo que se va a leer.
PATH_READ = os.path.join(current_dir, 'input.txt')

# Función para leer el archivo de texto y obtener los datos de entrada.
def read_input():

    # Abrir el archivo en modo lectura.
    file = open(PATH_READ, 'r')

    # Leer las líneas del archivo.
    lines = file.readlines()
    
    # Vamos a estructurar el grafo en un diccionario.
    graph = {}
    
    # Recorremos las líneas del archivo.
    for line in lines:

        # Eliminamos los espacios en blanco al inicio y al final de la línea; y separamos la vía de los nodos.
        node, edges = line.strip().split(':')
        node = node.strip()
        
        # Removemos los corchetes y obtenemos los nodos con su respectivo peso.
        edges = edges.strip()[1:-1]
        edge_list = []
        
        if edges:
            # Separamos los nodos y pesos, y los vamos añadiendo a la lista de nodos, del original.
            for edge in edges.split('),'):
                if edge:
                    edge = edge.strip('() ')
                    dest, weight = edge.split(',')
                    edge_list.append((dest.strip(), int(weight)))
        
        # Añadimos la lista de nodos al grafo.
        graph[node] = edge_list
    
    # Cerramos el archivo y retornamos el grafo.
    file.close()
    return graph

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DATOS DE SALIDA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# La salida cosiste en un archivo de texto llamado output.txt que contiene los arcos que se deben convertir a doble vía.
# La estructura del archivo es la siguiente:
#  1. Un mensaje que anuncia: "Vias que se deben convertir:"
#  2. Para cada arco que se debe convertir, se debe mostrar el arco (nodo de inicio y el nodo final) y el costo de la conversión.

# Función para escribir el archivo de texto con los datos de salida.
def write_output(mst):

    # Obtenemos la ruta del archivo actual (ruta relativa a la ubicación del archivo dentro del computador).
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Añadimos a la ruta del archivo que se va a escribir.
    PATH_WRITE = os.path.join(current_dir, 'output.txt')

    # Abrir el archivo en modo escritura.
    file = open(PATH_WRITE, 'w')

    # Escribimos la información en el archivo.
    file.write("Vias que se deben convertir:\n")
    for u, v, cost in mst:
        file.write(f"({u} a {v}) - Costo {cost}\n")

    # Cerramos el archivo.
    file.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ALGORITMO DE SOLUCIÓN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCIÓN PRINCIPAL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

    graph = read_input()

    start_vertex = 'A'
    mst = prim(graph, start_vertex)

    print("Vias que se deben convertir:")
    for u, v, cost in mst:
        print(f"({u} a {v}) - Costo {cost}")

    write_output(mst)