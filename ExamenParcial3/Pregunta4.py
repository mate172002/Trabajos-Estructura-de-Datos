class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Cola:
    def __init__(self):
        self.frente = None
        self.fondo = None

    def esta_vacia(self):
        return self.frente is None

    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.frente = self.fondo = nuevo_nodo
        else:
            self.fondo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.fondo
            self.fondo = nuevo_nodo

    def dequeue(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.fondo = None
        else:
            self.frente.anterior = None
        return dato

    def mostrar(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            actual = self.frente
            while actual:
                print(actual.dato, end=" <- ")
                actual = actual.siguiente
            print("NULL")

# Prueba de la cola con lista doblemente enlazada
cola = Cola()
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.mostrar()

print(f"Elemento removido: {cola.dequeue()}")
cola.mostrar()
