"""
1. PROBLEM IN SIMPLE WORDS
Minimum Cost to Connect Sticks
Small example: [2,4,3]
Expected: Return 14.

2. WHY / PURPOSE
Minimize total connection cost.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Combine two smallest so reused combined cost stays small.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap; pop two smallest; add sum to total; push sum.
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
Example: [2,4,3]
Goal: Return 14.
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
If I see: Repeated cheapest pair merge -> min heap.

15. ONE-LINE MEMORY TRICK
Two smallest + add cost + push sum.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Repeatedly combine the two smallest sticks so the total connection cost stays minimum.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a):
    # Rearrange the existing list into heap order in-place. This prepares the root for fast extreme selection.
    heapq.heapify(a)
    # Accumulate the total cost here as each pair of sticks is connected.
    total = 0
    # Keep repeating the heap process while there is still useful work/candidates left.
    while len(a) > 1:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        x = heapq.heappop(a)
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        y = heapq.heappop(a)
        # Store this intermediate state/value because a later heap decision needs it.
        s = x + y
        # Add this connection cost to the running total because we pay it now.
        total += s
        # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
        heapq.heappush(a, s)
    # Return the final result produced by the heap process.
    return total
# Run the small example and print the result so we can verify the idea.
print(solve([2, 4, 3]))
