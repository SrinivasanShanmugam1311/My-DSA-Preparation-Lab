"""
CHILDREN SUM PROPERTY

Required:
parent value = left child value + right child value

Mental model:
1. Going DOWN:
   if children total is smaller, push parent's value downward.
2. Recurse LEFT and RIGHT.
3. Coming UP:
   set parent = left + right.

This is a DOWN + UP recursion pattern.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def change_tree(root):
    if root is None:
        return

    child_sum = 0
    if root.left:
        child_sum += root.left.data
    if root.right:
        child_sum += root.right.data

    if child_sum >= root.data:
        root.data = child_sum
    else:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data

    change_tree(root.left)
    change_tree(root.right)

    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data

    if root.left or root.right:
        root.data = total
