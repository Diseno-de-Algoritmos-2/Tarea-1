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
# DATOS DE ENTRADA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# La entrada consiste en un archivo de texto llamado input.txt que contiene la información.
# La estructura del archivo es la siguiente:
#   Nodo: Amigo1: Amigo2, Amigo3, Amigo4, Amigo5
#   Nodo: Amigo1: Amigo3, Amigo4
#   Nodo: Amigo1: Amigo2
# Para cada línea, el primer amigo es el nodo y los amigos que le siguen son los amigos.
# por tanto, para leer el archivo vamos linea por linea y separamos el nodo de los amigos
# con el caracter ':'. Luego separamos los amigos con el caracter ','.


import os

# Obtenemos la ruta del archivo actual (ruta relativa a la ubicación del archivo dentro del computador).
current_dir = os.path.dirname(os.path.abspath(__file__))
# Añadimos a la ruta del archivo que se va a leer.
PATH = os.path.join(current_dir, 'input.txt')

# Función para leer el archivo de texto y obtener los datos de entrada.
def read_input():

    # Abrir el archivo en modo lectura.
    file = open(PATH, 'r')

    # Leer las líneas del archivo.
    lines = file.readlines()

    # Vamos a estructurar el grafo en un diccionario.
    graph = {}

    # Recorremos las líneas del archivo.
    for line in lines:
        
        # Eliminamos los espacios en blanco al inicio y al final de la línea; y separamos el nodo de los amigos.
        line = line.strip()
        friend, friends = line.split(':')

        # Eliminamos los espacios en blanco al inicio y al final de los amigos; y separamos los amigos.
        friend = friend.strip()
        friends = friends.split(',')

        # Eliminamos los espacios en blanco al inicio y al final de cada amigo; y los agregamos al grafo.
        friends = [f.strip() for f in friends]
        graph[friend] = set(friends)
    
    # Cerramos el archivo y retornamos el grafo.
    file.close()
    return graph

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DATOS DE SALIDA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ALGORITMO DE SOLUCIÓN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Estrategia:

# 1. Crear un grafo de relaciones de 'amigos no pelados'
# 2. Recorrer el grafo comenzando por un amigo aleatorio, estos amigos que si se llevan bien
#    serán la primera reunión
# 3. Si existe al menos un amigo que no pudo ser agregago a la primera reunión, entonces se
#    recorre el grafo una segunda vez ver si todos los amigos faltantes se llevan bien entre ellos
#    para formar la segunda reunión
# 4. Si no se puede formar la segunda reunión, entonces no es posible organizar las dos reuniones

from collections import deque # Queue

def friend_bfs(graph, start):
    visited = set()
    invited = {start}
    queue = deque([start])

    while queue:
        friend = queue.popleft() # Dequeue
        if friend not in visited:
            
            visited.add(friend)
            friendsOfFriend = graph[friend]
            
            # puedo agregar al amigo a la reunión SOLO si es amigo de TODOS los invitados
            if invited.issubset(friendsOfFriend):
                invited.add(friend)
            
            for neighbor in friendsOfFriend:
                if neighbor not in visited:
                    queue.append(neighbor) # Enqueue
                    
    return invited

def friends_meeting(graph, friendList):
    
    # Crear dos sets para las dos reuniones
    meeting1 = set()
    meeting2 = set()
    
    # Recorrer el grafo comenzando por un amigo aleatorio, estos amigos que si se llevan bien
    # entre si serán la primera reunión
    meeting1 = friend_bfs(graph, friendList[0])
    
    # Revisar si falta algún amigo en la primera reunión
    missingFriends = list(set(friendList) - meeting1)
    
    # Si falta algún amigo en la primera reunión, entonces se recorre el grafo una segunda vez ver
    # si todos los amigos faltantes se llevan bien entre ellos
    if missingFriends:
        meeting2 = friend_bfs(graph, missingFriends[0])
        # Si hay amigos que ya invitamos en la primera reunión, estos sobran
        meeting2 = meeting2 - meeting1
    
    # revisar si ya invitamos a todos los amigos
    if len(meeting1) + len(meeting2) == len(friendList):
        print('Es posible organizar las dos reuniones\n')
        print('Reunión 1:')
        print(meeting1)
        print('Reunión 2:')
        print(meeting2)
        print()
        
    else:
        print('No es posible organizar las dos reuniones')
        print()


graph = read_input()
friends_meeting(graph, list(graph.keys())) # Es posible
    


