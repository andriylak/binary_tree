class BinaryTree:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def TraversPreOrder(tree):
    if tree != None:
        print(tree.value)
        TraversPreOrder(tree.left_child)
        TraversPreOrder(tree.right_child)


def TraversInOrder(tree):
    if tree != None:
        TraversInOrder(tree.left_child)
        print(tree.value)
        TraversInOrder(tree.right_child)


def TraversPostOrder(tree):
    if tree != None:
        TraversPostOrder(tree.left_child)
        TraversPostOrder(tree.right_child)
        print(tree.value)


def TraversSum(tree):
    if tree != None:
        return TraversSum(tree.left_child) + TraversSum(tree.right_child) + tree.value
    else:
        return 0


def TraversDepthv2(tree):
    if tree != None:
        if tree.left_child != None:
            left = TraversDepthv2(tree.left_child)
        else:
            return 0
        if tree.right_child != None:
            right = TraversDepthv2(tree.right_child)
        else:
            return 0
        return max(left, right) + 1
    else:
        return 0


def TraversReturnValues(tree, array=[]):
    if tree != None:
        array.append(tree.value)
        TraversReturnValues(tree.left_child)
        TraversReturnValues(tree.right_child)
    return array


def NumberOfEdgesInTheLayer(tree, depth=0, count=[]):
    if tree != None:
        if len(count) <= depth:
            count.append(0)
            count[depth] += 1
        else:
            count[depth] += 1
        NumberOfEdgesInTheLayer(tree.left_child, depth + 1, count)
        NumberOfEdgesInTheLayer(tree.right_child, depth + 1, count)
    return count


def getListsOfNodesInTheLayer(tree, depth=0, result=[]):
    if tree != None:
        if len(result) <= depth:
            result.append([tree.value])
        else:
            result[depth].append(tree.value)
        getListsOfNodesInTheLayer(tree.left_child, depth + 1, result)
        getListsOfNodesInTheLayer(tree.right_child, depth + 1, result)
    return result


def VerticalBST(tree, depth=0, space=3):
    if tree != None:
        VerticalBST(tree.right_child, depth + 1)
        print(f"{tree.value:{(depth*space)}d}")
        VerticalBST(tree.left_child, depth + 1)


tree = BinaryTree(
    10,
    BinaryTree(5, BinaryTree(1), BinaryTree(7)),
    BinaryTree(20, None, BinaryTree(30)),
)
