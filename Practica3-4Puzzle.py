class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def clear(self):
        self.queue.clear()
    
    def __str__(self):
        return str(self.queue)

def vecino(estado):
    vecinos = []
    zero_pos = estado.index(0)  # Encuentra la posición del espacio vacío (0)
    
    # Definir las posiciones adyacentes dependiendo de dónde esté el espacio vacío
    movimientos_pos = {
        0: [1, 2],  # Posiciones a las que se puede mover desde la posición 0
        1: [0, 3],  # Posiciones a las que se puede mover desde la posición 1
        2: [0, 3],  # Posiciones a las que se puede mover desde la posición 2
        3: [1, 2],  # Posiciones a las que se puede mover desde la posición 3
    }
    
    for m in movimientos_pos[zero_pos]:
        nuevo = estado[:]
        # Intercambia el espacio vacío (0) con la ficha de la posición adyacente
        nuevo[zero_pos], nuevo[m] = nuevo[m], nuevo[zero_pos]
        vecinos.append(nuevo)
    
    return vecinos

def bfs_4_puzzle(estado_ini, estado_obj):
    queue = Queue()
    queue.enqueue((estado_ini, []))  # (estado actual, ruta de movimientos)
    visited = set()
    
    while not queue.is_empty():
        estado_actual, camino = queue.dequeue()
        
        if estado_actual == estado_obj:
            return camino + [estado_actual]  # Devolvemos la ruta completa

        visited.add(tuple(estado_actual))  # Marcamos el estado como visitado
        
        # Generar estados vecinos
        for v in vecino(estado_actual):
            if tuple(v) not in visited:
                queue.enqueue((v, camino + [estado_actual]))

    return None  # No se encontró solución

# Estado inicial y estado objetivo del 4-puzzle
estado_ini = [1, 2, 3, 0]  # 0 representa el espacio vacío
estado_obj = [1, 2, 3, 0]    # Queremos ordenar las fichas en el mismo orden

# Resolver el puzzle
res = bfs_4_puzzle(estado_ini, estado_obj)

if res:
    print("Camino de solución encontrado:")
    for step in res:
        print(step)
else:
    print("No se encontró solución para el puzzle.")
