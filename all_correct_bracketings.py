def allPossibleFullBinaryTrees(vertexes):
    if vertexes == 1:
        return 1
    result = 0
    for left_vertexes in range(1, vertexes, 2):
        right_vertexes = vertexes - left_vertexes - 1
        left_subtree_count = allPossibleFullBinaryTrees(left_vertexes)
        right_subtree_count = allPossibleFullBinaryTrees(right_vertexes)
        result += left_subtree_count * right_subtree_count
    return result

bracket_pairs = int(input())
vertexes = 2 * bracket_pairs + 1
print(allPossibleFullBinaryTrees(vertexes))