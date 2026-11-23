"""
LCA IN BST
Mental model:
- If both values are smaller than root -> go LEFT.
- If both are larger than root -> go RIGHT.
- Otherwise root is the SPLIT point -> LCA.

Time: O(h), Space: O(h) recursive stack
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lca(root, p, q):
    if root is None:
        return None

    if p < root.data and q < root.data:
        return lca(root.left, p, q)

    if p > root.data and q > root.data:
        return lca(root.right, p, q)

    return root

# Example
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)

ans = lca(root, 2, 4)
print("LCA:", ans.data if ans else None)
