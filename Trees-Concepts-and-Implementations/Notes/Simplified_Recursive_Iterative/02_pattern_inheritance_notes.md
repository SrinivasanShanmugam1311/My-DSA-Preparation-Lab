# Simplified Pattern Inheritance

## DFS → Height

```text
dfs(root)
    dfs(left)
    dfs(right)
```

becomes:

```text
left = height(root.left)
right = height(root.right)
return 1 + max(left, right)
```

## Height → Diameter

Keep returning height.

Add:

```text
answer = max(answer, left + right)
```

## Height → Balanced

Keep returning height.

Add:

```text
return -1 if subtree is unbalanced
```

## Same Tree → Symmetric

Same two-root comparison.

Only child direction changes:

```text
same:      left-left, right-right
symmetric: left-right, right-left
```

## BFS → Views

Keep queue.

```text
Left view  -> take first node
Right view -> take last node
Zigzag     -> reverse alternate level
```

## BFS → Top/Bottom/Vertical

Queue stores:

```text
(node, horizontal_distance)
```

## DFS → Path Problems

Carry extra state:

```text
path array
target sum
```

## DFS → LCA

Return node pointer upward.

## BST Problems

Use one rule:

```text
left < root < right
```
