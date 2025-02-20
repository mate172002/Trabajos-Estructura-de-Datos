class NodoAVL:
    def __init__(self, turno, prioridad):
        self.turno = turno  # ID del paciente o turno
        self.prioridad = prioridad  # Prioridad del paciente
        self.izquierda = None  # Subárbol izquierdo
        self.derecha = None  # Subárbol derecho
        self.altura = 1  # Altura del nodo para el balanceo

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        return y

    def insertar(self, nodo, turno, prioridad):
        if not nodo:
            return NodoAVL(turno, prioridad)

        if prioridad < nodo.prioridad:
            nodo.izquierda = self.insertar(nodo.izquierda, turno, prioridad)
        else:
            nodo.derecha = self.insertar(nodo.derecha, turno, prioridad)

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

        balance_factor = self.balance(nodo)

        # Caso de rotación a la derecha
        if balance_factor > 1 and prioridad < nodo.izquierda.prioridad:
            return self.rotacion_derecha(nodo)

        # Caso de rotación a la izquierda
        if balance_factor < -1 and prioridad > nodo.derecha.prioridad:
            return self.rotacion_izquierda(nodo)

        # Caso de rotación izquierda-derecha
        if balance_factor > 1 and prioridad > nodo.izquierda.prioridad:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Caso de rotación derecha-izquierda
        if balance_factor < -1 and prioridad < nodo.derecha.prioridad:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def insertar_turno(self, turno, prioridad):
        self.raiz = self.insertar(self.raiz, turno, prioridad)

    def inorder(self, nodo):
        if not nodo:
            return []
        return self.inorder(nodo.izquierda) + [(nodo.turno, nodo.prioridad)] + self.inorder(nodo.derecha)

    def mostrar_turnos(self):
        return self.inorder(self.raiz)

# Función principal para la interfaz de usuario
def menu():
    arbol = ArbolAVL()
    while True:
        print("\nSistema de Gestión de Turnos - Hospital")
        print("1. Insertar paciente")
        print("2. Ver turnos")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            turno = input("Ingrese el ID del paciente: ")
            prioridad = int(input("Ingrese la prioridad (menor número = mayor urgencia): "))
            arbol.insertar_turno(turno, prioridad)
            print(f"Paciente {turno} insertado con prioridad {prioridad}.")
        
        elif opcion == 2:
            turnos = arbol.mostrar_turnos()
            print("Turnos ordenados por prioridad:")
            for t in turnos:
                print(f"Paciente {t[0]} - Prioridad {t[1]}")
        
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
