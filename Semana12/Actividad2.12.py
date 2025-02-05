class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self, raiz=None):
        self.raiz = raiz
    
    def evaluar(self, nodo):
        if nodo is None:
            return 0
        
        if nodo.izquierda is None and nodo.derecha is None:
            return int(nodo.valor)
        
        izquierda_valor = self.evaluar(nodo.izquierda)
        derecha_valor = self.evaluar(nodo.derecha)
        
        if nodo.valor == '+':
            return izquierda_valor + derecha_valor
        elif nodo.valor == '-':
            return izquierda_valor - derecha_valor
        elif nodo.valor == '*':
            return izquierda_valor * derecha_valor
        elif nodo.valor == '/':
            return izquierda_valor / derecha_valor

    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.derecha)

    def recorrido_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)

    def recorrido_postorden(self, nodo):
        if nodo is not None:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(nodo.valor, end=' ')

raiz = Nodo('*')
raiz.izquierda = Nodo('+')
raiz.izquierda.izquierda = Nodo('3')
raiz.izquierda.derecha = Nodo('5')
raiz.derecha = Nodo('-')
raiz.derecha.izquierda = Nodo('2')
raiz.derecha.derecha = Nodo('4')

arbol = ArbolExpresion(raiz)

print("Recorrido inorden:")
arbol.recorrido_inorden(arbol.raiz)
print("\nRecorrido preorden:")
arbol.recorrido_preorden(arbol.raiz)
print("\nRecorrido postorden:")
arbol.recorrido_postorden(arbol.raiz)
print("\nResultado de la evaluación de la expresión:", arbol.evaluar(arbol.raiz))
