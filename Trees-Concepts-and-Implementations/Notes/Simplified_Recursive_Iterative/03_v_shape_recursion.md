# V-shaped Recursion

Every recursive tree function goes down and then comes back up.

```text
dfs(root)
   \
    \ call child
     \
   base case
     /
    / return answer
   /
combine at parent
```

## Example: Height

```text
height(1)
    -> height(2)
        -> height(NULL) returns 0
    <- node 2 returns 1
<- node 1 returns 2
```

## Stack frame remembers

```text
current node
left result
right result
next line
return address
```

Memory line:

```text
Ask left.
Ask right.
Combine.
Return.
```
