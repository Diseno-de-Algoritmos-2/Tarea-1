import networkx as nx
import matplotlib.pyplot as plt
import string
import random

def crear_grafo_completo(num_nodos):
    # Create graph
    G = nx.Graph()
    
    # Generate node names (A, B, C, etc.)
    nombres = list(string.ascii_uppercase[:num_nodos])
    
    # Add all nodes
    G.add_nodes_from(nombres)
    
    # Create edges between all pairs of nodes8
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if random.random() < 0.5:
                G.add_edge(nombres[i], nombres[j])
    
    # Create figure with larger size
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw with better styling
    nx.draw(G, 
           with_labels=True,
           node_color='lightblue',
           node_size=500,
           font_size=16,
           font_weight='bold',
           width=2,
           edge_color='gray')
    
    plt.show()
    
    # Return graph structure as dictionary
    return {node: set(G.neighbors(node)) for node in G.nodes()}

# Example usage:
num_nodos = int(input("Ingrese el número de nodos deseado: "))
graph = crear_grafo_completo(num_nodos)
print("\nEstructura del grafo:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")