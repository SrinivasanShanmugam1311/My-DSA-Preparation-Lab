"""
1. PROBLEM IN SIMPLE WORDS
Merge K Sorted Lists
Small example: [1,4],[2,5],[3,6]
Expected: Return 1,2,3,4,5,6.

2. WHY / PURPOSE
Merge many sorted lists.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Each list offers only its current head.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap of current heads; pop then push next from same list.
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
Example: [1,4],[2,5],[3,6]
Goal: Return 1,2,3,4,5,6.
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
If I see: K sorted sources -> heap of K current heads.

15. ONE-LINE MEMORY TRICK
Pop smallest head; expose next from same list.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Keep one current head from each list; pop the smallest head and expose the next item from that list.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(lists):
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Store the final answer/order here as heap choices are made.
    out = []
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for li, a in enumerate(lists):
        # Check whether this candidate/state needs a heap update.
        if a:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (a[0], li, 0))
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        v, li, j = heapq.heappop(h)
        # Add the selected heap result to the final output.
        out.append(v)
        # Check whether this candidate/state needs a heap update.
        if j + 1 < len(lists[li]):
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (lists[li][j + 1], li, j + 1))
    # Return the final result produced by the heap process.
    return out
# Run the small example and print the result so we can verify the idea.
print(solve([[1, 4], [2, 5], [3, 6]]))
