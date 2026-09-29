HEAPS ULTRA SIMPLE PACK V8 — ONE STANDARD TEMPLATE
==================================================

MAIN RULE OF THIS VERSION
-------------------------
Every numbered C problem uses the SAME readable helper functions:
    swap(), min_push(), min_pop(), max_push(), max_pop()

The helper code uses the SAME meaningful variable names and the SAME simple comments.
There are no compressed h/n/x/i/p/l/r helper versions in the numbered C files.

Start with: 00_ONE_STANDARD_HEAP_TEMPLATE.txt

HEAPS ULTRA SIMPLE PACK V7 — STANDARDIZED + MODULAR
====================================================

WHAT V7 ADDS
------------
- Same reusable heap function names across application problems.
- Meaningful variable-name vocabulary across the pack.
- C and Python helper APIs use matching concepts.
- Templates show how the same functions are invoked again and again.
- Existing V6 teaching comments, mental models, simulations, and problem files are retained.

START HERE
----------
1. 00_MENTAL_MODELS.txt
2. 02_STANDARD_VARIABLE_NAMES_AND_TEMPLATES.txt
3. Python/heap_helpers.py and C/heap_helpers.h/.c
4. Standardized_Examples/
5. Then study the 25 original fully commented problem files.

IMPORTANT
---------
The reusable API is standardized. Problem-specific state cannot always use identical names, because a Twitter problem naturally needs timestamp/user_id while CPU scheduling needs processing_time/current_time. The common heap vocabulary stays identical.

HEAPS ULTRA SIMPLE PACK V6 — REUSABLE FUNCTIONS
================================================

V6 keeps ALL V5 learning notes, comments, C files, and Python files.
Nothing from the fully-commented teaching pack was removed.

NEW IN V6
---------
1. Reusable heap helper modules for C and Python.
2. A reusable-functions guide showing which problems share the same operations.
3. Reusable example programs for the most important heap families.
4. Original 25 fully-commented solutions are still present for problem-by-problem study.

STUDY RULE
----------
Problems 01-06: study the heap implementation itself. Do NOT hide bubble-up / heapify-down.
Problems 07-25: first understand the problem, then reuse heap operations where appropriate.

Think:
    HEAP MECHANICS = learn how PUSH/POP work internally.
    HEAP APPLICATIONS = reuse PUSH/POP and focus on the problem pattern.

HEAPS — ULTRA SIMPLE STUDY PACK V5 — FULLY COMMENTED
==================================

PURPOSE
-------
This pack contains 25 heap problems from our study sequence.
The code is intentionally written for LEARNING, not for code-golf.

Every source file uses:
  • Python files now include line-by-line teaching comments explaining WHAT + WHY + HOW
  • one statement per line
  • clear indentation
  • meaningful variable names where practical
  • comments that explain WHAT a step does
  • comments that explain WHY the step is needed
  • comments that connect the line to the heap mental model

INTERVIEW NOTE
--------------
Heap problems are normally solved ITERATIVELY.
Heapify itself can be recursive or iterative.
For this pack, iterative heap operations are the default because the movement is simple:

  INSERT  → put at end → bubble UP
  POP     → move last to root → heapify DOWN

PROBLEMS AND PATTERNS
---------------------

BASIC HEAP MECHANICS
  01. Min / Max Heap Basics
      Mental model: Root is the extreme. Children obey the heap rule.

  02. Heap Insertion
      Mental model: Put new value at the end, then move it UP.

  03. Delete Heap Root
      Mental model: Save root, move last value to root, then move DOWN.

  04. Heapify
      Mental model: Compare with children, choose the correct child, move DOWN.

  05. Build Heap
      Mental model: Start from the last parent and repair parents bottom-up.

  06. Convert Min Heap to Max Heap
      Mental model: Same complete tree shape; repair using the opposite comparison.

  22. Check Min Heap
      Mental model: Every parent must be <= both existing children.

TOP-K WINNER PATTERN
  07. Top K Largest
      Keep K largest winners in a MIN heap. Root = weakest winner.

  08. Kth Largest
      Keep K largest winners. MIN-heap root = Kth largest.

  09. Top K Smallest
      Keep K smallest winners in a MAX heap. Root = weakest winner.

  17. Kth Largest in a Stream
      Stream arrives → keep only K largest → root = Kth largest.

  19. K Closest Points
      Keep K closest winners → MAX heap lets us remove the farthest winner.

  20. Top K Frequent
      Count first → keep K highest frequencies using a MIN heap.

SMALL CANDIDATE SET / K-WAY MERGE
  10. Sort K-Sorted Array
      Look at K+1 nearby candidates → pop the smallest.

  11. Merge K Sorted Lists
      Put each list's current head in a MIN heap → pop smallest → expose next.

ORDERING / RANKING
  12. Replace Elements by Rank
      Process values smallest-first and assign ranks.

BEST READY / AVAILABLE CANDIDATE
  13. Task Scheduler
      Cooldown decides READY. MAX heap chooses the ready task with most remaining work.

  14. Hand of Straights
      Smallest remaining card starts each consecutive group.

  15. Design Twitter
      MAX heap repeatedly chooses the newest current tweet.

  24. Single-Threaded CPU
      Arrival decides AVAILABLE. MIN heap chooses shortest processing time.

  25. IPO
      Capital decides AFFORDABLE. MAX heap chooses highest profit.

STREAMING
  16. Median From Data Stream
      MAX heap = smaller half. MIN heap = bigger half. Median lives at the roots.

REPEATED TWO EXTREMES
  18. Last Stone Weight
      Pop two largest → subtract → push leftover.

  21. Minimum Cost to Connect Sticks
      Pop two smallest → add cost → push combined stick.

BEST PAIR / FRONTIER
  23. Maximum Sum Combination
      Start with best pair → expose nearby next pairs → MAX heap chooses next best.

QUICK REVISION MAP
------------------
Need smallest repeatedly?                 → MIN HEAP
Need largest repeatedly?                  → MAX HEAP
Need Top K largest?                        → MIN HEAP size K
Need Top K smallest?                       → MAX HEAP size K
Need two largest repeatedly?               → MAX HEAP, POP twice
Need two smallest repeatedly?              → MIN HEAP, POP twice
Candidates become available over time?     → eligibility rule + heap
Need running median?                       → two heaps

BEST LEARNING ORDER
-------------------
01 → 02 → 03 → 04 → 05 → 06 → 22
07 → 08 → 09 → 17 → 19 → 20
10 → 11 → 12
18 → 21
13 → 14 → 15 → 24 → 25
16 → 23

MEMORY
------
Heap = keep the BEST CURRENT candidate easy to reach at the root.
