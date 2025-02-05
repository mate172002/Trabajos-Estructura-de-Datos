class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self, raiz):
        self.raiz = raiz

    def evaluar(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return float(nodo.valor)
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
        
nodo1 = Nodo('3')
nodo2 = Nodo('5')
nodo3 = Nodo('+')
nodo3.izquierda = nodo1
nodo3.derecha = nodo2
nodo4 = Nodo('2')
nodo5 = Nodo('*')
nodo5.izquierda = nodo3
nodo5.derecha = nodo4

arbol = ArbolExpresion(nodo5)
resultado = arbol.evaluar(arbol.raiz)
print("Resultado:", resultado) 