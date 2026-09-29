"""
1. PROBLEM IN SIMPLE WORDS
Top K Frequent
Small example: [1,1,1,2,2,3], K=2
Expected: Return 1,2.

2. WHY / PURPOSE
Find K most frequent values.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Count first; then keep K largest frequencies.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Frequency map + min heap size K.
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
Example: [1,1,1,2,2,3], K=2
Goal: Return 1,2.
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
If I see: Frequency then Top-K largest -> min heap K.

15. ONE-LINE MEMORY TRICK
COUNT first; keep K strongest frequencies.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Count frequencies first, then keep the K values with the largest counts.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq
# Counter quickly tells us how many times each value appears.
from collections import Counter

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a, k):
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for v, c in Counter(a).items():
        # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
        heapq.heappush(h, (c, v))
        # Check whether this candidate/state needs a heap update.
        if len(h) > k:
            # POP the current root because it is the candidate we want to process/remove now.
            heapq.heappop(h)
    # Return the final result produced by the heap process.
    return [v for c, v in h]
# Run the small example and print the result so we can verify the idea.
print(solve([1, 1, 1, 2, 2, 3], 2))
