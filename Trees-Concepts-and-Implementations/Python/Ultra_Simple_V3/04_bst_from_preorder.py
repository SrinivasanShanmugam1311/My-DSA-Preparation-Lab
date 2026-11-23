"""
CONSTRUCT BST FROM PREORDER

Preorder gives:
ROOT -> LEFT -> RIGHT

Mental model:
Each recursive call receives an UPPER LIMIT.
If next value is too large, it does not belong here.

Time: O(n), Space: O(h)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def bst_from_preorder(preorder):
    index = 0

    def build(bound):
        nonlocal index

        if index == len(preorder) or preorder[index] > bound:
            return None

        value = preorder[index]
        index += 1

        root = Node(value)
        root.left = build(value)
        root.right = build(bound)
        return root

    return build(float("inf"))

root = bst_from_preorder([8, 5, 1, 7, 10, 12])
