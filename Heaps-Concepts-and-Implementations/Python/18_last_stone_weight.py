"""
1. PROBLEM IN SIMPLE WORDS
Last Stone Weight
Small example: [2,7,4,1,8,1]
Expected: Return 1.

2. WHY / PURPOSE
Simulate repeated largest-pair operation.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Repeatedly take two heaviest stones, smash, push leftover.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Max heap; pop twice; push difference.
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
Example: [2,7,4,1,8,1]
Goal: Return 1.
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
If I see: Repeated two largest -> max heap.

15. ONE-LINE MEMORY TRICK
POP two largest, subtract, PUSH leftover.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Repeatedly remove the two heaviest stones and push back their difference.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a):
    # Negate every stone weight so Python’s min heap behaves like a MAX HEAP of stone weights.
    h = [-x for x in a]
    # Rearrange the existing list into heap order in-place. This prepares the root for fast extreme selection.
    heapq.heapify(h)
    # Keep repeating the heap process while there is still useful work/candidates left.
    while len(h) > 1:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        x = -heapq.heappop(h)
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        y = -heapq.heappop(h)
        # Check whether this candidate/state needs a heap update.
        if x != y:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, -(x - y))
    # Return the final result produced by the heap process.
    return -h[0] if h else 0
# Run the small example and print the result so we can verify the idea.
print(solve([2, 7, 4, 1, 8, 1]))
