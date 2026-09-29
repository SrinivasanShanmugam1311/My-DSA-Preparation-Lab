"""
1. PROBLEM IN SIMPLE WORDS
Top K Largest
Small example: [7,2,9,4,8], K=3
Expected: Return 7,8,9.

2. WHY / PURPOSE
Find K largest without sorting everything.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Keep K winner chairs; root is weakest winner.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap size K; replace root only with a bigger value.
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
Example: [7,2,9,4,8], K=3
Goal: Return 7,8,9.
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
If I see: Top K largest -> min heap size K.

15. ONE-LINE MEMORY TRICK
K largest = Min Heap of K winners.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Keep only the K largest winners; the min-heap root is the weakest current winner.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a, k):
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for x in a:
        # Check whether this candidate/state needs a heap update.
        if len(h) < k:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, x)
        # The first case did not happen, so check this next valid case.
        elif x > h[0]:
            # Remove the current root and insert the new better candidate in one heap operation.
            heapq.heapreplace(h, x)
    # Return the final result produced by the heap process.
    return sorted(h)
# Run the small example and print the result so we can verify the idea.
print(solve([7, 2, 9, 4, 8], 3))
