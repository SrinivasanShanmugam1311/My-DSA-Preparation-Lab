"""
SERIALIZE / DESERIALIZE BINARY TREE

Serialize:
Tree -> string

Deserialize:
string -> same tree

Use PREORDER:
ROOT -> LEFT -> RIGHT

Important:
Store NULL markers (#).
Without NULL markers we cannot know the exact tree shape.

Time: O(n), Space: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def serialize(root):
    values = []

    def dfs(node):
        if node is None:
            values.append("#")
            return

        values.append(str(node.data))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(values)

def deserialize(data):
    values = iter(data.split(","))

    def dfs():
        value = next(values)

        if value == "#":
            return None

        node = Node(int(value))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()
