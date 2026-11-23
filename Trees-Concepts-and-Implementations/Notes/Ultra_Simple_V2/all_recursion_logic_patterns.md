# TREE RECURSION LOGIC PATTERNS — VERY SIMPLE NOTES

## 1. The basic recursion shape

Every recursive tree function usually has three parts:

```text
1. Base condition
2. Recursive calls
3. Work before, between, or after the calls
```

Basic form:

```text
solve(node):
    if node is NULL:
        return

    work with current node

    solve(node.left)
    solve(node.right)
```

The position of the work decides the traversal.

---

# 2. PREORDER — CURRENT NODE FIRST

Order:

```text
Current
Left
Right
```

Template:

```text
solve(node):
    if node is NULL:
        return

    DO CURRENT WORK

    solve(node.left)
    solve(node.right)
```

Think:

> The parent does its work first.  
> Then the children continue.

Use when:

- Carrying information downward
- Modifying the current node first
- Saving the current node before children

Examples:

- Path Sum
- Good Nodes
- Root-to-Leaf Paths
- Validate BST using min/max range
- Invert Tree
- Serialize

Important logic change:

```text
PREORDER = work is before recursive calls
```

---

# 3. INORDER — LEFT FIRST, CURRENT IN THE MIDDLE

Order:

```text
Left
Current
Right
```

Template:

```text
solve(node):
    if node is NULL:
        return

    solve(node.left)

    DO CURRENT WORK

    solve(node.right)
```

Think:

> Finish the left side.  
> Process the current node.  
> Then go right.

Use mainly for BST problems because BST inorder is sorted.

Examples:

- Kth Smallest
- Validate BST using previous value
- Recover BST
- BST Iterator
- Inorder Successor

Important logic change:

```text
INORDER = work is between left and right calls
```

---

# 4. POSTORDER — CHILDREN FIRST

Order:

```text
Left
Right
Current
```

Template:

```text
solve(node):
    if node is NULL:
        return base_value

    left_answer = solve(node.left)
    right_answer = solve(node.right)

    DO CURRENT WORK USING CHILD ANSWERS

    return answer
```

Think:

> The parent waits.  
> Children finish first.  
> Then the parent calculates.

Use when parent needs child results.

Examples:

- Height
- Diameter
- Balanced Tree
- LCA
- Maximum Path Sum
- Largest BST Subtree
- House Robber III
- Binary Tree Cameras

Important logic change:

```text
POSTORDER = work is after recursive calls
```

---

# 5. CARRY INFORMATION DOWNWARD

Template:

```text
solve(node, state):
    if node is NULL:
        return

    new_state = update(state, node)

    solve(node.left, new_state)
    solve(node.right, new_state)
```

Information flow:

```text
Parent
  ↓
Child
  ↓
Grandchild
```

Examples:

- Path Sum carries remaining target
- Good Nodes carries maximum value seen
- Root-to-Leaf Paths carries current path
- Validate BST carries allowed range

Question to ask:

> What information does the child need from the parent?

---

# 6. RETURN INFORMATION UPWARD

Template:

```text
solve(node):
    if node is NULL:
        return base_value

    left = solve(node.left)
    right = solve(node.right)

    return combine(left, right, node)
```

Information flow:

```text
Child
  ↑
Parent
  ↑
Grandparent
```

Examples:

- Height returns height
- Diameter returns height but updates diameter
- LCA returns a node pointer
- Balanced Tree returns height or -1
- Maximum Path Sum returns one-side gain

Question to ask:

> What answer must each child return to its parent?

---

# 7. BACKTRACKING

Template:

```text
add current choice
recurse left
recurse right
remove current choice
```

Example:

```text
path.append(node)
recurse
path.pop()
```

Use when one shared path/list is reused.

Examples:

- Root-to-Leaf Paths
- Path Sum II
- All root-to-leaf strings

Memory:

```text
Choose
Explore
Undo
```

---

# 8. DOUBLE DFS / COMPARE

Template:

```text
compare(node1, node2):
    compare current pair
    compare child pair 1
    compare child pair 2
```

Usually preorder-style because current nodes are compared first.

Examples:

- Same Tree
- Symmetric Tree
- Subtree of Another Tree

Same Tree:

```text
left with left
right with right
```

Symmetric Tree:

```text
left.left with right.right
left.right with right.left
```

---

# 9. SINGLE-PATH BST RECURSION

This is not a full preorder traversal.

It is preorder-style because current node decides first.

Template:

```text
if target < node.value:
    go left
else:
    go right
```

Only one path is followed.

Examples:

- Search
- Insert
- Delete
- Floor
- Ceil
- LCA in BST
- Successor
- Predecessor

---

# 10. TREE DP

Tree DP is usually postorder.

Template:

```text
left_state = solve(left)
right_state = solve(right)

current_state = combine(left_state, right_state)

return current_state
```

Examples:

- House Robber III returns:
  - rob current
  - skip current

- Cameras returns:
  - needs camera
  - has camera
  - covered

- Largest BST returns:
  - is BST
  - minimum
  - maximum
  - size

---

# 11. RECURSION STACK PUSH AND POP

Example:

```text
solve(1)
  calls solve(2)
    calls solve(4)
```

Stack while going down:

```text
Top -> solve(4)
       solve(2)
       solve(1)
```

This is PUSH.

When solve(4) finishes:

```text
solve(4) is removed
```

This is POP.

Then control returns to the exact line after:

```text
solve(node.left)
```

V shape:

```text
solve(1)
   \
   solve(2)
      \
      solve(4)
      /
   return to 2
   /
return to 1
```

Left side of V:

```text
calls / push
```

Right side of V:

```text
returns / pop
```

---

# 12. MASTER DECISION QUESTIONS

Ask these in order:

```text
1. Do I need levels?
   Yes -> BFS

2. Do I carry information from parent to child?
   Yes -> Preorder / Carry Downward

3. Does parent need child answers first?
   Yes -> Postorder / Return Upward

4. Is BST sorted order needed?
   Yes -> Inorder

5. Am I comparing two trees or two sides?
   Yes -> Double DFS

6. Do I follow only one BST direction?
   Yes -> BST Single Path

7. Do I need all paths?
   Yes -> Backtracking

8. Does each child return multiple states?
   Yes -> Tree DP
```
