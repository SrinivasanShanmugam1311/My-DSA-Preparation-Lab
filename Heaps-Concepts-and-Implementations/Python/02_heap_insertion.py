"""
1. PROBLEM IN SIMPLE WORDS
Heap Insertion
Small example: [10,20,30] + 5
Expected: Insert 5 into min heap.

2. WHY / PURPOSE
Keep heap valid after adding one value.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
New item takes next empty seat, then bubbles UP.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Append then compare with parent and swap upward.
A simple full scan can work on tiny input, but repeated scans may redo a lot of work. A heap keeps the best current candidate at the root.

5. EVERY VARIABLE
heap -> current candidates.
root -> best current candidate.
answer/out -> result built so far.
i/j/index -> where a value/task came from when needed.
k -> how many answers/winners are required when the problem has K.

6. PICTORIAL EXPLANATION
CANDIDATES
    ↓
  HEAP
    ↓
ROOT = best current candidate
    ↓
 POP / PROCESS
    ↓
UPDATE → maybe PUSH → repeat

7. STEP-BY-STEP SIMULATION
Example: [10,20,30] + 5
Goal: Insert 5 into min heap.
1) Start with the candidates allowed by the problem.
2) Put the useful candidates in the heap.
3) Read/POP the root because the root is the best current candidate.
4) Update the state. PUSH a new candidate only when the problem makes it available.
5) Repeat until the answer is complete.

8. RECURSION V-SHAPE
Not used in the interview solution here. Heap problems are normally solved iteratively. Heapify itself can be recursive, but an iterative loop is simple and avoids call-stack space.

9. WHOLE MOVIE
Find/receive eligible candidates -> PUSH -> root is best -> POP/process -> state changes -> PUSH newly eligible candidate -> repeat.

10/11. CODE
See this file for the language-specific implementation.

12. MAP CODE TO MENTAL MODEL
heappush / heap push = candidate enters the waiting room.
heappop / heap pop = choose the best current candidate.
comparison = defines what “best” means for this problem.

13. TIME AND SPACE COMPLEXITY
A heap PUSH/POP is usually O(log H), where H is current heap size. Root lookup is O(1). Exact total complexity depends on how many items are pushed/popped; see comments/code pattern.

14. PATTERN RECOGNITION
If I see: Add item to heap -> append + bubble up.

15. ONE-LINE MEMORY TRICK
Insert = end, then UP.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Insert a new value at the end, then bubble it UP until the min-heap rule is correct.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Define the solution/helper function. The actual heap steps happen inside this block.
def push_min(h, x):
    # Put the new value at the END first. This preserves the complete-tree shape.
    h.append(x)
    # Start at the new value’s index because this is the value that may need to move UP.
    i = len(h) - 1
    # Keep repeating the heap process while there is still useful work/candidates left.
    while i > 0:
        # Find the parent index so we can check whether the min-heap parent<=child rule is broken.
        p = (i - 1) // 2
        # Check whether this candidate/state needs a heap update.
        if h[p] <= h[i]:
            # Stop this loop because no more useful work can be done in this direction.
            break
        # Swap child with parent so the smaller value moves one level UP toward the min-heap root.
        h[p], h[i] = (h[i], h[p])
        # Continue from the new parent position because the value may still need to move farther UP.
        i = p
# Store this intermediate state/value because a later heap decision needs it.
h = [10, 20, 30]
push_min(h, 5)
# Run the small example and print the result so we can verify the idea.
print(h)
