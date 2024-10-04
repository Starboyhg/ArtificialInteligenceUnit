class GenericList:
    """Implementación de una lista genérica"""
    def __init__(self):
        self.items = []
    
    def add(self, item):
        """Añadir un elemento al final de la lista"""
        self.items.append(item)
    
    def insert(self, index, item):
        """Insertar un elemento en una posición específica"""
        if 0 <= index <= len(self.items):
            self.items.insert(index, item)
        else:
            print(f"Índice fuera de rango: {index}")
    
    def remove(self, item):
        """Eliminar la primera aparición del elemento en la lista"""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Elemento {item} no encontrado en la lista")
    
    def pop(self, index=None):
        """Eliminar y devolver el elemento en la posición indicada"""
        if index is None:
            return self.items.pop()  # Elimina el último si no se especifica un índice
        elif 0 <= index < len(self.items):
            return self.items.pop(index)
        else:
            print(f"Índice fuera de rango: {index}")
            return None
    
    def get(self, index):
        """Obtener el elemento en la posición indicada"""
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            print(f"Índice fuera de rango: {index}")
            return None
    
    def size(self):
        """Devolver el tamaño de la lista"""
        return len(self.items)
    
    def is_empty(self):
        """Verificar si la lista está vacía"""
        return len(self.items) == 0
    
    def clear(self):
        """Vaciar la lista"""
        self.items.clear()
    
    def __str__(self):
        """Devolver una representación en cadena de la lista"""
        return str(self.items)

# # Ejemplo de uso
# generic_list = GenericList()

# # Añadir elementos
# generic_list.add(10)
# generic_list.add(20)
# generic_list.add(30)

# print("Lista después de añadir elementos:", generic_list)

# # Insertar un elemento en una posición específica
# generic_list.insert(1, 15)
# print("Lista después de la inserción:", generic_list)

# # Eliminar un elemento
# generic_list.remove(20)
# print("Lista después de eliminar el 20:", generic_list)

# # Obtener un elemento
# print("Elemento en el índice 2:", generic_list.get(2))

# # Eliminar el último elemento
# generic_list.pop()
# print("Lista después de hacer pop:", generic_list)

# # Verificar si la lista está vacía
# print("¿La lista está vacía?", generic_list.is_empty())

# # Limpiar la lista
# generic_list.clear()
# print("Lista después de vaciarla:", generic_list)

class Queue:
    """Implementación de una cola (FIFO - First In, First Out)"""
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        """Añadir un elemento al final de la cola"""
        self.queue.append(item)
    
    def dequeue(self):
        """Eliminar y devolver el elemento al frente de la cola"""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("La cola está vacía")
            return None
    
    def front(self):
        """Obtener el elemento al frente de la cola sin eliminarlo"""
        if not self.is_empty():
            return self.queue[0]
        else:
            print("La cola está vacía")
            return None
    
    def is_empty(self):
        """Verificar si la cola está vacía"""
        return len(self.queue) == 0
    
    def size(self):
        """Devolver el tamaño de la cola"""
        return len(self.queue)
    
    def clear(self):
        """Vaciar la cola"""
        self.queue.clear()
    
    def __str__(self):
        """Devolver una representación en cadena de la cola"""
        return str(self.queue)

# # Ejemplo de uso de la cola
# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)

# print("Cola después de encolar elementos:", queue)

# queue.dequeue()
# print("Cola después de desencolar un elemento:", queue)

# print("Elemento al frente de la cola:", queue.front())

# print("Tamaño de la cola:", queue.size())

class Stack:
    """Implementación de una pila (LIFO - Last In, First Out)"""
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        """Añadir un elemento a la cima de la pila"""
        self.stack.append(item)
    
    def pop(self):
        """Eliminar y devolver el elemento en la cima de la pila"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("La pila está vacía")
            return None
    
    def top(self):
        """Obtener el elemento en la cima de la pila sin eliminarlo"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("La pila está vacía")
            return None
    
    def is_empty(self):
        """Verificar si la pila está vacía"""
        return len(self.stack) == 0
    
    def size(self):
        """Devolver el tamaño de la pila"""
        return len(self.stack)
    
    def clear(self):
        """Vaciar la pila"""
        self.stack.clear()
    
    def __str__(self):
        """Devolver una representación en cadena de la pila"""
        return str(self.stack)

# # Ejemplo de uso de la pila
# stack = Stack()
# stack.push(100)
# stack.push(200)
# stack.push(300)

# print("Pila después de apilar elementos:", stack)

# stack.pop()
# print("Pila después de desapilar un elemento:", stack)

# print("Elemento en la cima de la pila:", stack.top())

# print("Tamaño de la pila:", stack.size())
