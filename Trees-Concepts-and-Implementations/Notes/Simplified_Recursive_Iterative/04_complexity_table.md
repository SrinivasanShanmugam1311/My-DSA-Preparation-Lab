# Time and Space Complexity

| Topic | Recursive complexity | Iterative complexity |
|---|---|---|
| DFS traversals | O(n), O(h) stack | O(n), O(n) stack |
| Level order | Usually iterative: O(n), O(w) queue | O(n), O(w) |
| Height | O(n), O(h) | O(n), O(w) BFS |
| Diameter | O(n), O(h) optimized | Usually recursive optimized |
| Balanced | O(n), O(h) optimized | Usually recursive optimized |
| Same/Symmetric | O(n), O(h) | O(n), O(n) stack/queue |
| Zigzag/Views | O(n), O(w) | O(n), O(w) |
| Top/Bottom/Vertical | O(n log n), O(n) | O(n log n), O(n) |
| Boundary | O(n), O(h) | O(n), O(n) |
| Path problems | O(n*h) output, O(h) | Recursive preferred |
| LCA BT | O(n), O(h) | Parent-map iterative O(n), O(n) |
| Children Sum | O(n), O(h) | Recursive preferred |
| Complete count | O(log²n), O(logn) | Recursive preferred |
| Build tree | O(n), O(n) with map | Recursive preferred |
| Serialize | O(n), O(h) | O(n), O(n) possible |
| Morris | O(n), O(1) | O(n), O(1) |
| BST search | O(h), O(h) | O(h), O(1) |
| Validate BST | O(n), O(h) | O(n), O(n) |
| Kth smallest | O(h+k), O(h) | O(h+k), O(h) |
| Flatten | O(n), O(h) | O(n), O(n) |
| Ternary tree DFS | O(n), O(h) | O(n), O(n) |
