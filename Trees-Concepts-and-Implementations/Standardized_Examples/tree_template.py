from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    # Empty subtree has zero height (counting nodes).
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)


def preorder(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push right first so left is processed first.
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def level_order(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result


def search_bst(root, key):
    while root is not None and root.val != key:
        if key < root.val:
            root = root.left
        else:
            root = root.right
    return root


if __name__ == '__main__':
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert height(root) == 2
    assert preorder(root) == [2, 1, 3]
    assert level_order(root) == [[2], [1, 3]]
    assert search_bst(root, 3).val == 3
    assert search_bst(root, 4) is None
    print('All template checks passed.')
