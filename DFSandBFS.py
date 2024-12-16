from collections import deque
class BinaryTree():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def DFS(tree):
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node != None:
            print(node.value)
            stack.append(tree.left_child)
            stack.append(tree.right_child)

def BFS(tree):
    fronta = deque([])
    fronta.append(tree)
    while len(fronta) > 0:
        node = fronta.popleft()
        print(node.value)
        if node.left_child != None:
            fronta.append(node.left_child)
        if node.right_child != None:
            fronta.append(node.right_child)
    
tree = BinaryTree(10, BinaryTree(5, BinaryTree(1), BinaryTree(7)), BinaryTree(20, None, BinaryTree(30)))
BFS(tree)