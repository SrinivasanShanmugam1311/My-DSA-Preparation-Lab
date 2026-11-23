"""
MAXIMUM WIDTH OF BINARY TREE

Use LEVEL ORDER / BFS.

Imagine array-style positions:
root = 0
left  = 2*i + 1
right = 2*i + 2

At each level:
width = last_position - first_position + 1

Normalize positions each level to avoid huge integers.

Time: O(n), Space: O(n)
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def maximum_width(root):
    if root is None:
        return 0

    q = deque([(root, 0)])
    answer = 0

    while q:
        level_size = len(q)
        base = q[0][1]
        first = last = 0

        for i in range(level_size):
            node, pos = q.popleft()
            pos -= base

            if i == 0:
                first = pos
            if i == level_size - 1:
                last = pos

            if node.left:
                q.append((node.left, 2 * pos + 1))
            if node.right:
                q.append((node.right, 2 * pos + 2))

        answer = max(answer, last - first + 1)

    return answer
