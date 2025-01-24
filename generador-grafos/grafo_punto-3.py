# Daniel vargas
# Santiago Bobadilla
# Lina Ariza

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DESCRIPCIÓN DEL PROBLEMA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3. Juan quiere invitar a sus amigos a conocer su nuevo apartamento. Sin embargo tiene la
# dificultad de que sus amigos son algo conflictivos y entonces sabe que varias parejas de
# amigos se han peleado entre ellos.
# 
# Debido a esto, tomó la decisión de organizar dos reuniones. Diseñe un algoritmo que
# determine si es posible distribuir a los amigos de Juan en dos grupos de tal manera
# que dentro de cada reunión no haya parejas de personas que se hayan peleado entre ellas.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GENERADOR DE GRAFOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Libreria de grafos.
import networkx as nx

# Libreria para graficar.
import matplotlib.pyplot as plt

# Libreria para generar números aleatorios.
import random

# Libreria para manipulación de archivos.
import os

# Función para crear el grafo de amistades.
def crear_grafo_amistades(num_amigos):

    # Creamos un grafo vacío.
    G = nx.Graph()
    
    # Generamos los nodos del grafo. Estos son Juan y sus amigos.
    nombres = ['Juan'] + [f'Amigo_{i}' for i in range(1, num_amigos)]
    G.add_nodes_from(nombres)
    
    # Juan conoce a todos sus amigos.
    for i in range(1, len(nombres)):
        G.add_edge('Juan', nombres[i])
    
    # LOs amigos entre sí estan conectados por un eje con probabilidad del 50%.
    for i in range(1, len(nombres)):
        for j in range(i + 1, len(nombres)):
            if random.random() < .5:
                G.add_edge(nombres[i], nombres[j])
    
    # Dibujamos el grafo vacio.
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Añadimos al grafo los nodos.
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500)
    
    # Añadimos al grafo los ejes.
    nx.draw_networkx_edges(G, pos, edge_color='green', width=1)
    
    # Añadimos al grafo las etiquetas.
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    # Con el fin de saber cual es el grafo original, guardamos la imagen.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    output_path = os.path.join(parent_dir, 'punto-3', 'grafo.jpg')
    plt.savefig(output_path, format='jpg', bbox_inches='tight', dpi=300)
    
    # Además, mostramos el grafo.
    plt.show()
    plt.close()
    
    # Guardamos el grafo en un archivo de texto que sigue el mismo formato que el archivo de entrada de 
    # la implementación de la solución (Carpeta: Punto-3).
    output_path = os.path.join(parent_dir, 'punto-3', 'input.txt')
    with open(output_path, 'w') as f:
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            if neighbors:
                f.write(f"{node}: {', '.join(neighbors)}\n")


# Función principal.
if __name__ == '__main__':

    # Solicitamos el número de amigos.
    num_amigos = int(input("Ingrese el número de amigos (incluyendo a Juan): "))
    
    # Creamos el grafo de amistades y lo guardamos.
    crear_grafo_amistades(num_amigos)