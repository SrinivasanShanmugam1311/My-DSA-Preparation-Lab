"""
DIAMETER OF BINARY TREE

Mental model:
Every node asks:
"How tall is my LEFT side?"
"How tall is my RIGHT side?"

Path through current node = left_height + right_height.
Keep the maximum.

The recursive function RETURNS HEIGHT upward.

Time: O(n), Space: O(h)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def diameter(root):
    best = 0

    def height(node):
        nonlocal best
        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        best = max(best, left + right)

        return 1 + max(left, right)

    height(root)
    return best
