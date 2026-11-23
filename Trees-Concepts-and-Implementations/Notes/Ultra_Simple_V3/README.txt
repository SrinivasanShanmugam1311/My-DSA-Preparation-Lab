JEGA + TA TREE ULTRA SIMPLE PACK V3
=====================================

Problems
--------
01. LCA in BST
02. Merge Two BSTs
03. Delete Node in BST
04. Construct BST from Preorder
05. Morris Inorder Traversal
06. Diameter of Binary Tree
07. Children Sum Property
08. Maximum Width of Binary Tree
09. Serialize and Deserialize Binary Tree
10. Flatten Binary Tree to Linked List

Mental model used throughout
----------------------------
1. Understand what the problem wants.
2. Identify whether it is BST-specific or general Binary Tree.
3. Decide what information must move down/up the tree.
4. Trace a tiny example.
5. Then read the code.

Folder structure
----------------
C/       -> C implementations
Python/  -> Python implementations
README.txt

Quick pattern map
-----------------
LCA BST              -> use BST ordering
Merge BST            -> inorder gives sorted values
Delete BST           -> search + 3 deletion cases
BST from preorder    -> bounds / valid range
Morris traversal     -> temporary threaded links
Diameter             -> height returned upward
Children sum         -> modify children, recurse, fix parent
Maximum width        -> BFS + positional indices
Serialize            -> preorder + NULL markers
Flatten              -> connect previous subtree in preorder

Study suggestion
----------------
For every problem:
WHAT? -> WHY? -> MENTAL MODEL -> SMALL TRACE -> CODE -> COMPLEXITY
