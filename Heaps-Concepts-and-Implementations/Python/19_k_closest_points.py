"""
1. PROBLEM IN SIMPLE WORDS
K Closest Points
Small example: (1,3),(-2,2),(5,8); K=2
Expected: Return (-2,2),(1,3).

2. WHY / PURPOSE
Find K points closest to origin.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Keep K closest chairs; farthest current winner sits at root.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Max heap size K by squared distance.
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
Example: (1,3),(-2,2),(5,8); K=2
Goal: Return (-2,2),(1,3).
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
If I see: Top K smallest distances -> max heap K.

15. ONE-LINE MEMORY TRICK
K closest = kick out farthest winner.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Keep K closest points; a max heap keeps the farthest current winner easy to remove.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(points, k):
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for x, y in points:
        # Compute squared distance from origin. Squared distance is enough because square root would not change which point is closer.
        d = x * x + y * y
        # Check whether this candidate/state needs a heap update.
        if len(h) < k:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (-d, x, y))
        # The first case did not happen, so check this next valid case.
        elif d < -h[0][0]:
            # Remove the current root and insert the new better candidate in one heap operation.
            heapq.heapreplace(h, (-d, x, y))
    # Return the final result produced by the heap process.
    return [(x, y) for _, x, y in h]
# Run the small example and print the result so we can verify the idea.
print(solve([(1, 3), (-2, 2), (5, 8)], 2))
