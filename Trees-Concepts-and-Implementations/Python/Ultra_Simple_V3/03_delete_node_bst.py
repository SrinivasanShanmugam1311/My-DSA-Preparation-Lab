"""
DELETE NODE IN BST

First SEARCH using BST property.

When target is found:
1. No child  -> remove node.
2. One child -> return that child.
3. Two children -> take smallest node from RIGHT subtree,
   copy its value, then delete that duplicate.

Time: O(h)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def minimum(root):
    while root.left:
        root = root.left
    return root

def delete_node(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = minimum(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)

    return root
