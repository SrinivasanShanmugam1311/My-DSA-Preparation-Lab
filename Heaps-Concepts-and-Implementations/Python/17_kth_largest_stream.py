"""
1. PROBLEM IN SIMPLE WORDS
Kth Largest in a Stream
Small example: K=3; 4,5,8,2,10,7
Expected: Answers after K filled: 4,4,5,7.

2. WHY / PURPOSE
Report current Kth largest after each arrival.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
K winner chairs; root is weakest winner.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap size K.
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
Example: K=3; 4,5,8,2,10,7
Goal: Answers after K filled: 4,4,5,7.
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
If I see: Streaming Kth largest -> min heap K.

15. ONE-LINE MEMORY TRICK
Keep K largest; root is Kth.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# As numbers arrive, keep only K largest values; the min-heap root is the current Kth largest.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Create an object that keeps heap state alive between multiple stream operations.
class KthLargest:

    # Define the solution/helper function. The actual heap steps happen inside this block.
    def __init__(self, k):
        # Remember K because the stream object must always keep exactly the K largest winners when possible.
        self.k = k
        # Start an empty min heap that will keep the K largest stream values.
        self.h = []

    # Define the solution/helper function. The actual heap steps happen inside this block.
    def add(self, x):
        # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
        heapq.heappush(self.h, x)
        # Check whether this candidate/state needs a heap update.
        if len(self.h) > self.k:
            # POP the current root because it is the candidate we want to process/remove now.
            heapq.heappop(self.h)
        # Return the final result produced by the heap process.
        return self.h[0] if len(self.h) == self.k else None
# Store this intermediate state/value because a later heap decision needs it.
k = KthLargest(3)
# Visit the needed items one by one so each item gets one chance to enter or affect the heap.
for x in [4, 5, 8, 2, 10, 7]:
    # Run the small example and print the result so we can verify the idea.
    print(k.add(x))
