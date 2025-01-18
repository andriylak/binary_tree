This repository contains implementation of binary tree and basic functions for them:

DFSandBFS.py:
  - DFS(tree) : implementation of DFS on binary trees
  - BFS(tree) : implementation of BFS on binary trees

BinaryTree.py:
  - TraversPreOrder(tree) : traverses the tree in the order: Node → Left Child → Right Child.
  - TraversInOrder(tree) : traverses the tree in the order: Left Child → Node → Right Child.
  - TraversPostOrder(tree) : traverses the tree in the order: Left Child → Right Child → Node.
  - TraversSum(tree) : returns the sum of all binary tree nodes.
  - TraversDepthv2(tree) : returns the depth of the binary tree. 
  - TraversReturnValues(tree) : returns the list of all binary tree nodes (In-order).
  - NumberOfEdgesInTheLayer(tree) : returns the list with the number of nodes on each layer.
  - getListsOfNodesInTheLayer(tree) : returns the list with the lists of nodes on each layer.
  - VerticalBST(tree) : prints the binary tree vertically.

all_correct_bracketings.py - identifies the number of all possible combinations from given number of bracket-pairs.

TreesAndBracketings.py - indicates whether the list of full binary tree is right or left child from given sequence of 
brackets (we can represent full binary tree as a system of correct bracketings).
