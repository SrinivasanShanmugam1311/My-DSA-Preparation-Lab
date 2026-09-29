"""
1. PROBLEM IN SIMPLE WORDS
Median From Data Stream
Small example: 5,2,10,8,3
Expected: Medians 5,3.5,5,6.5,5.

2. WHY / PURPOSE
Get median anytime as numbers arrive.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Split numbers into smaller half and bigger half; median sits at boundary.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Max heap left + min heap right; balance sizes.
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
Example: 5,2,10,8,3
Goal: Medians 5,3.5,5,6.5,5.
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
If I see: Streaming median -> two balanced heaps.

15. ONE-LINE MEMORY TRICK
Two halves; median lives at the roots.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Split numbers into a smaller half and bigger half; the median stays at the two heap roots.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Create an object that keeps heap state alive between multiple stream operations.
class MedianFinder:

    # Define the solution/helper function. The actual heap steps happen inside this block.
    def __init__(self):
        # LEFT heap stores the smaller half. We use negatives so it behaves like a MAX HEAP.
        self.left = []
        # RIGHT heap stores the bigger half as a normal MIN HEAP.
        self.right = []

    # Define the solution/helper function. The actual heap steps happen inside this block.
    def add(self, x):
        # Check whether this candidate/state needs a heap update.
        if not self.left or x <= -self.left[0]:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(self.left, -x)
        # Use this path when the earlier condition is false.
        else:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(self.right, x)
        # Check whether this candidate/state needs a heap update.
        if len(self.left) > len(self.right) + 1:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(self.right, -heapq.heappop(self.left))
        # The first case did not happen, so check this next valid case.
        elif len(self.right) > len(self.left) + 1:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(self.left, -heapq.heappop(self.right))

    # Define the solution/helper function. The actual heap steps happen inside this block.
    def median(self):
        # Check whether this candidate/state needs a heap update.
        if len(self.left) == len(self.right):
            # Return the final result produced by the heap process.
            return (-self.left[0] + self.right[0]) / 2
        # Return the final result produced by the heap process.
        return float(-self.left[0] if len(self.left) > len(self.right) else self.right[0])
# Store this intermediate state/value because a later heap decision needs it.
m = MedianFinder()
# Visit the needed items one by one so each item gets one chance to enter or affect the heap.
for x in [5, 2, 10, 8, 3]:
    m.add(x)
    # Run the small example and print the result so we can verify the idea.
    print(m.median())
