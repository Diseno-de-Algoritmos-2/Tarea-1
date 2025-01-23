# 3. Juan quiere invitar a sus amigos a conocer su nuevo apartamento. Sin embargo tiene la
# dificultad de que sus amigos son algo conflictivos y entonces sabe que varias parejas de
# amigos se han peleado entre ellos.
# 
# Debido a esto, tomó la decisión de organizar dos reuniones. Diseñe un algoritmo que
# determine si es posible distribuir a los amigos de Juan en dos grupos de tal manera
# que dentro de cada reunión no haya parejas de personas que se hayan peleado entre ellas.

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
            2
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
    
    
    
    
    
# Grafo1: no es posible organizar las dos reuniones
graph1 = {
    'Juan': {'Pedro', 'Maria'},
    'Pedro': {'Juan'},
    'Maria': {'Juan', 'Ana'},
    'Carlos': {'Ana'},
    'Ana': {'Maria', 'Carlos'}
}

# Grafo2: es posible organizar las dos reuniones, porque todos son amigos entre si
graph2 = {
    'Juan': {'Pedro', 'Maria', 'Carlos', 'Ana'},
    'Pedro': {'Juan', 'Maria', 'Carlos', 'Ana'},
    'Maria': {'Juan', 'Pedro', 'Carlos', 'Ana'},
    'Carlos': {'Juan', 'Pedro', 'Maria', 'Ana'},
    'Ana': {'Juan', 'Pedro', 'Maria', 'Carlos'}
}

# Grafo 3: es posible organizar las dos reuniones (aqui hay dos posibles soluciones)
graph3 = {
    'Juan': {'Pedro', 'Maria', 'Carlos'},
    'Carlos': {'Juan'},
    'Pedro': {'Juan', 'Maria'},
    'Maria': {'Juan', 'Pedro'}
}


friends_meeting(graph1, list(graph1.keys())) # No es posible
friends_meeting(graph2, list(graph2.keys())) # Es posible
friends_meeting(graph3, list(graph3.keys())) # Es posible
    


