"""
FLATTEN BINARY TREE TO LINKED LIST

Wanted order = PREORDER:
ROOT -> LEFT -> RIGHT

Final tree uses only RIGHT pointers.

Simple reverse-preorder mental model:
RIGHT -> LEFT -> ROOT

Keep 'previous'.
After processing children:
current.right = previous
current.left = None
previous = current

Time: O(n), Space: O(h)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def flatten(root):
    previous = None

    def dfs(node):
        nonlocal previous

        if node is None:
            return

        dfs(node.right)
        dfs(node.left)

        node.right = previous
        node.left = None
        previous = node

    dfs(root)
