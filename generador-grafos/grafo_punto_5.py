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
# GENERADOR DE GRAFOS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Libreria de grafos
import networkx as nx

# Libreria para graficar
import matplotlib.pyplot as plt

# Libreria para generar números aleatorios
import random

# Libreria para manipulación de archivos.
import os

# Función para crear el grafo de ciudades.
def crear_grafo_ciudad(num_vias, prob_arista=0.5, max_costo=10):

    # Creamos un grafo vacío.
    G = nx.Graph()

    # Generamos los nodos del grafo: A, B, C... 
    nodos = [chr(ord('A') + i) for i in range(num_vias)]
    G.add_nodes_from(nodos)

    # Para cada par de nodos (i, j), decidimos aleatoriamente si hay calle y su costo
    for i in range(num_vias):
        for j in range(i + 1, num_vias):
            # Generamos un valor aleatorio en [0, 1) y lo comparamos con 'prob_arista'.
            if random.random() < prob_arista:
                # Si se cumple, definimos un costo aleatorio para la arista.
                costo = random.randint(1, max_costo)
                # Añadimos la arista (i, j) al grafo 'G' con un atributo 'weight' igual a 'costo'.
                G.add_edge(nodos[i], nodos[j], weight=costo)

    # Con el fin de saber cual es el grafo original, guardamos la imagen.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    output_dir = os.path.join(parent_dir, 'punto-5')
    os.makedirs(output_dir, exist_ok=True)

    # Dibujamos el grafo y guardamos la imagen.
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, k=1, iterations=50)

    # Añadimos al grafo los nodos.
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    
    # Añadimos al grafo los ejes.
    nx.draw_networkx_edges(G, pos, edge_color='green', width=1)
    
    # Añadimos al grafo las etiquetas.
    nx.draw_networkx_labels(G, pos, font_size=9)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    img_path = os.path.join(output_dir, 'grafo.jpg')
    plt.savefig(img_path, format='jpg', bbox_inches='tight', dpi=300)
    plt.show()
    plt.close()

    # Generamos el archivo input.txt.
    input_path = os.path.join(output_dir, 'input.txt')

    with open(input_path, 'w') as f:
        for via in G.nodes():
            conexiones = []
            # Recorremos los vecinos de via.
            for vecino in G[via]:
                # Extraemos el costo de la arista.
                costo = G[via][vecino]['weight']
                conexiones.append(f"({vecino}, {costo})")

            # Si el nodo via tiene conexiones.
            if conexiones:
                line_str = ", ".join(conexiones)
                f.write(f"{via}: {line_str}\n")
            else:
                # Si no tiene conexiones, lo dejamos vacío.
                f.write(f"{via}: ()\n")


# Función principal.
if __name__ == '__main__':
    # Solicitamos la cantidad de vías.
    num_vias = int(input("Ingrese el número de vías:"))

    # Creamos el grafo de ciudades y lo guardamos.
    crear_grafo_ciudad(num_vias, prob_arista=0.5, max_costo=10)
