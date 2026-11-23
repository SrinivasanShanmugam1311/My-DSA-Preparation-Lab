from collections import deque, defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# ============================================================
# Jega 171: DFS Traversals
# Pattern: Root position decides preorder/inorder/postorder.
# ============================================================

def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def postorder_recursive(root):
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def preorder_iterative(root):
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans


def inorder_iterative(root):
    stack = []
    ans = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        ans.append(node.val)
        node = node.right
    return ans


def postorder_iterative_two_stack(root):
    if not root:
        return []
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    return [node.val for node in reversed(s2)]


# ============================================================
# Jega 172: BFS Level Order
# Pattern: Queue + level size.
# ============================================================

def level_order_iterative(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def level_order_recursive(root):
    ans = []

    def dfs(node, level):
        if not node:
            return
        if level == len(ans):
            ans.append([])
        ans[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return ans


# ============================================================
# Jega 174: Height / Max Depth
# Inherits from DFS.
# ============================================================

def height_recursive(root):
    if not root:
        return 0
    left = height_recursive(root.left)
    right = height_recursive(root.right)
    return 1 + max(left, right)


def height_iterative(root):
    if not root:
        return 0
    q = deque([root])
    height = 0
    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return height


# ============================================================
# Jega 176: Diameter
# Inherits from height.
# Delta: update answer with left + right.
# ============================================================

def diameter_optimized(root):
    answer = 0

    def height(node):
        nonlocal answer
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        answer = max(answer, left + right)
        return 1 + max(left, right)

    height(root)
    return answer


# ============================================================
# Jega 175: Balanced Tree
# Inherits from height.
# Delta: return -1 if invalid.
# ============================================================

def is_balanced_optimized(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


# ============================================================
# Jega 181: Identical Tree / Same Tree
# Pattern: Compare two roots.
# ============================================================

def is_same_tree_recursive(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return is_same_tree_recursive(a.left, b.left) and \
           is_same_tree_recursive(a.right, b.right)


def is_same_tree_iterative(a, b):
    stack = [(a, b)]
    while stack:
        left, right = stack.pop()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        stack.append((left.left, right.left))
        stack.append((left.right, right.right))
    return True


# ============================================================
# Jega 185: Symmetric Tree
# Inherits from same-tree.
# Delta: compare mirror children.
# ============================================================

def is_symmetric_recursive(root):
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return mirror(left.left, right.right) and \
               mirror(left.right, right.left)

    return True if not root else mirror(root.left, root.right)


def is_symmetric_iterative(root):
    if not root:
        return True
    q = deque([(root.left, root.right)])
    while q:
        left, right = q.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        q.append((left.left, right.right))
        q.append((left.right, right.left))
    return True


# ============================================================
# Jega 182/185: Zigzag / Left View / Right View
# Inherits from level order.
# ============================================================

def zigzag_iterative(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    left_to_right = True
    while q:
        size = len(q)
        level = [0] * size
        for i in range(size):
            node = q.popleft()
            index = i if left_to_right else size - 1 - i
            level[index] = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
        left_to_right = not left_to_right
    return ans


def left_view_iterative(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0:
                ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans


def right_view_iterative(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:
                ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans


# ============================================================
# Jega 184: Top / Bottom / Vertical View
# Inherits from BFS.
# Delta: queue stores horizontal distance.
# ============================================================

def vertical_order_iterative(root):
    if not root:
        return []
    table = defaultdict(list)
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        table[hd].append(node.val)
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    return [table[x] for x in sorted(table)]


def top_view_iterative(root):
    if not root:
        return []
    seen = {}
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        if hd not in seen:
            seen[hd] = node.val
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    return [seen[x] for x in sorted(seen)]


def bottom_view_iterative(root):
    if not root:
        return []
    seen = {}
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        seen[hd] = node.val
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    return [seen[x] for x in sorted(seen)]


# ============================================================
# Jega 183: Boundary Traversal
# Optimized: O(n)
# ============================================================

def boundary_traversal(root):
    if not root:
        return []

    def is_leaf(node):
        return node and not node.left and not node.right

    ans = []
    if not is_leaf(root):
        ans.append(root.val)

    node = root.left
    while node:
        if not is_leaf(node):
            ans.append(node.val)
        node = node.left if node.left else node.right

    def add_leaves(node):
        if not node:
            return
        if is_leaf(node):
            ans.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    add_leaves(root)

    stack = []
    node = root.right
    while node:
        if not is_leaf(node):
            stack.append(node.val)
        node = node.right if node.right else node.left

    ans.extend(reversed(stack))
    return ans


# ============================================================
# Jega 186: Path Problems
# Pattern: push -> recurse -> pop.
# ============================================================

def root_to_leaf_paths(root):
    ans = []
    path = []

    def dfs(node):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            ans.append(path.copy())
        else:
            dfs(node.left)
            dfs(node.right)
        path.pop()

    dfs(root)
    return ans


def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return has_path_sum(root.left, target - root.val) or \
           has_path_sum(root.right, target - root.val)


# ============================================================
# Jega 193: Lowest Common Ancestor
# Pattern: return node pointer upward.
# ============================================================

def lca_recursive(root, p, q):
    if not root:
        return None
    if root is p or root is q:
        return root

    left = lca_recursive(root.left, p, q)
    right = lca_recursive(root.right, p, q)

    if left and right:
        return root

    return left or right


# ============================================================
# Jega 194: Children Sum
# Optimized recursive modify.
# ============================================================

def change_tree_children_sum(root):
    if not root:
        return

    child_sum = 0
    if root.left:
        child_sum += root.left.val
    if root.right:
        child_sum += root.right.val

    if child_sum >= root.val:
        root.val = child_sum
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val

    change_tree_children_sum(root.left)
    change_tree_children_sum(root.right)

    total = 0
    if root.left:
        total += root.left.val
    if root.right:
        total += root.right.val

    if root.left or root.right:
        root.val = total


# ============================================================
# Jega 196/197: Count Complete Tree Nodes
# Optimized: O(log^2 n)
# ============================================================

def count_complete_nodes(root):
    def left_height(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def right_height(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    if not root:
        return 0

    left = left_height(root)
    right = right_height(root)

    if left == right:
        return (1 << left) - 1

    return 1 + count_complete_nodes(root.left) + count_complete_nodes(root.right)


# ============================================================
# Jega 198/199/200: Build Tree
# Optimized with hashmap.
# ============================================================

def build_pre_in(preorder, inorder):
    pos = {val: i for i, val in enumerate(inorder)}
    index = 0

    def build(left, right):
        nonlocal index
        if left > right:
            return None
        root_val = preorder[index]
        index += 1
        root = TreeNode(root_val)
        mid = pos[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(inorder) - 1)


def build_post_in(inorder, postorder):
    pos = {val: i for i, val in enumerate(inorder)}
    index = len(postorder) - 1

    def build(left, right):
        nonlocal index
        if left > right:
            return None
        root_val = postorder[index]
        index -= 1
        root = TreeNode(root_val)
        mid = pos[root_val]
        root.right = build(mid + 1, right)
        root.left = build(left, mid - 1)
        return root

    return build(0, len(inorder) - 1)


# ============================================================
# Jega 203: Serialize / Deserialize
# Optimized preorder with # markers.
# ============================================================

def serialize(root):
    out = []

    def dfs(node):
        if not node:
            out.append("#")
            return
        out.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return " ".join(out)


def deserialize(data):
    tokens = iter(data.split())

    def dfs():
        val = next(tokens)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# ============================================================
# Jega 204/205: Morris Traversal
# Optimized O(1) space.
# ============================================================

def morris_inorder(root):
    ans = []
    node = root
    while node:
        if not node.left:
            ans.append(node.val)
            node = node.right
        else:
            prev = node.left
            while prev.right and prev.right is not node:
                prev = prev.right
            if not prev.right:
                prev.right = node
                node = node.left
            else:
                prev.right = None
                ans.append(node.val)
                node = node.right
    return ans


def morris_preorder(root):
    ans = []
    node = root
    while node:
        if not node.left:
            ans.append(node.val)
            node = node.right
        else:
            prev = node.left
            while prev.right and prev.right is not node:
                prev = prev.right
            if not prev.right:
                ans.append(node.val)
                prev.right = node
                node = node.left
            else:
                prev.right = None
                node = node.right
    return ans


# ============================================================
# Jega 206: Invert / Flatten
# Pointer manipulation.
# ============================================================

def invert_tree(root):
    if not root:
        return None
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    root.left = right
    root.right = left
    return root


def flatten_recursive(root):
    prev = None

    def dfs(node):
        nonlocal prev
        if not node:
            return
        dfs(node.right)
        dfs(node.left)
        node.right = prev
        node.left = None
        prev = node

    dfs(root)


def flatten_iterative(root):
    if not root:
        return
    stack = [root]
    prev = None
    while stack:
        node = stack.pop()
        if prev:
            prev.right = node
            prev.left = None
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        prev = node


# ============================================================
# Jega 207-215: BST Master
# ============================================================

def search_bst_recursive(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return search_bst_recursive(root.left, val)
    return search_bst_recursive(root.right, val)


def search_bst_iterative(root, val):
    node = root
    while node:
        if node.val == val:
            return node
        node = node.left if val < node.val else node.right
    return None


def floor_bst(root, key):
    ans = None
    node = root
    while node:
        if node.val == key:
            return node.val
        if node.val < key:
            ans = node.val
            node = node.right
        else:
            node = node.left
    return ans


def ceil_bst(root, key):
    ans = None
    node = root
    while node:
        if node.val == key:
            return node.val
        if node.val > key:
            ans = node.val
            node = node.left
        else:
            node = node.right
    return ans


def is_valid_bst(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return dfs(node.left, min_val, node.val) and \
               dfs(node.right, node.val, max_val)

    return dfs(root, float("-inf"), float("inf"))


def kth_smallest(root, k):
    stack = []
    node = root
    count = 0
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right
    return None


def lca_bst(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return None


def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def delete_bst(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        node = root.right
        while node.left:
            node = node.left
        root.val = node.val
        root.right = delete_bst(root.right, node.val)
    return root


# ============================================================
# TA 266/267: Ternary Tree
# ============================================================

class TernaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None


def ternary_dfs_recursive(root):
    if not root:
        return []
    return [root.val] + \
           ternary_dfs_recursive(root.left) + \
           ternary_dfs_recursive(root.middle) + \
           ternary_dfs_recursive(root.right)


def ternary_dfs_iterative(root):
    if not root:
        return []
    ans = []
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.middle:
            stack.append(node.middle)
        if node.left:
            stack.append(node.left)
    return ans
