class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    output = []
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in ('+', '-', '*', '/'):
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar '('

    while stack:
        output.append(stack.pop())

    return output

def build_expression_tree(postfix_tokens):
    stack = []
    
    for token in postfix_tokens:
        if token.isdigit():
            stack.append(Node(token))
        else:
            node = Node(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    
    return stack.pop()

def evaluate(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return int(node.value)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

# Ejemplo de uso:
expression = "4 + 10 * ( 6 - 15 )"
postfix = infix_to_postfix(expression)
tree = build_expression_tree(postfix)
result = evaluate(tree)

print("Resultado:", result)
