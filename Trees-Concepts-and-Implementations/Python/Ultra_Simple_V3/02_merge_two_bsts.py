"""
MERGE TWO BSTs
Mental model:
BST inorder traversal gives SORTED values.
So:
BST1 -> sorted list A
BST2 -> sorted list B
Then merge A and B like merge-sort.

Time: O(n+m), Space: O(n+m)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorder(root, out):
    if not root:
        return
    inorder(root.left, out)
    out.append(root.data)
    inorder(root.right, out)

def merge_sorted(a, b):
    i = j = 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans.append(a[i]); i += 1
        else:
            ans.append(b[j]); j += 1
    ans.extend(a[i:])
    ans.extend(b[j:])
    return ans

def merge_bsts(root1, root2):
    a, b = [], []
    inorder(root1, a)
    inorder(root2, b)
    return merge_sorted(a, b)
