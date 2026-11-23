"""
MORRIS INORDER TRAVERSAL

Goal: inorder WITHOUT recursion and WITHOUT explicit stack.

Mental model:
If current has no LEFT:
    print current -> move RIGHT

If LEFT exists:
    find predecessor = rightmost node in left subtree.

    predecessor.right is None:
        create temporary THREAD back to current
        move LEFT

    predecessor.right already points to current:
        remove THREAD
        print current
        move RIGHT

Time: O(n), Extra Space: O(1)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def morris_inorder(root):
    current = root
    result = []

    while current:
        if current.left is None:
            result.append(current.data)
            current = current.right
        else:
            predecessor = current.left

            while predecessor.right and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.data)
                current = current.right

    return result
