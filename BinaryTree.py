class BinaryTree():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def traverz(tree):
    if tree != None:
        print(tree.value)
        traverz(tree.left_child)
        traverz(tree.right_child)
        
def TraverzInOrder(tree):
    if tree != None:
        TraverzInOrder(tree.left_child)
        print(tree.value)
        TraverzInOrder(tree.right_child)

def TraverzSum(tree):
    if tree != None:
        return TraverzSum(tree.left_child) + TraverzSum(tree.right_child)
    else:
        return 0

def TraverzDepth(tree):
    if tree != None:
        return max(TraverzDepth(tree.left_child), TraverzDepth(tree.right_child)) + 1
    else:
        return 0

def TraverzDepthv2(tree, h = 0):
    if tree.left_child != None or tree.right_child != None:
        return max(TraverzDepth(tree.left_child, h + 1), TraverzDepth(tree.right_child, h + 1)) + 1
    else:
        return 0

def TraverzReturnValues(tree, array = []):
    if tree != None:
        array.append(tree.value)
        TraverzReturnValues(tree.left_child)
        TraverzReturnValues(tree.right_child)
    return array

def NumberOfEdgesInTheLayer(tree, depth = 0, count = []):
    if tree != None:
        if len(count)<=depth:
            count.append(0)
            count[depth] += 1
        else:
            count[depth] += 1
        NumberOfEdgesInTheLayer(tree.left_child, depth + 1, count)
        NumberOfEdgesInTheLayer(tree.right_child, depth + 1, count)
    return count

    
def VerticalBST(tree, depth=0, space = 3):
    if tree != None:
        VerticalBST(tree.right_child,depth+1)
        print(depth*space*' ', tree.value, sep='')
        VerticalBST(tree.left_child, depth+1)
