"""
1. PROBLEM IN SIMPLE WORDS
Replace Elements by Rank
Small example: [40,10,20,10]
Expected: Return [3,1,2,1].

2. WHY / PURPOSE
Replace each value with its rank.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Process values from smallest to largest and assign ranks.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap stores (value,index); equal values share rank.
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
Example: [40,10,20,10]
Goal: Return [3,1,2,1].
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
If I see: Need ascending rank order -> min heap.

15. ONE-LINE MEMORY TRICK
Smallest first -> assign ranks.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Process values from smallest to largest and write each rank back to the value’s original position.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a):
    # Store this intermediate state/value because a later heap decision needs it.
    h = [(v, i) for i, v in enumerate(a)]
    # Rearrange the existing list into heap order in-place. This prepares the root for fast extreme selection.
    heapq.heapify(h)
    # Create answer slots so each computed rank can be written back to the original index.
    ans = [0] * len(a)
    # No rank has been assigned yet. Rank increases only when we see a new distinct value.
    rank = 0
    # Remember the previous popped value so duplicates can receive the same rank.
    prev = None
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        v, i = heapq.heappop(h)
        # Check whether this candidate/state needs a heap update.
        if prev is None or v != prev:
            # Move this counter/index/time forward by one because one step/item has just been processed.
            rank += 1
            # Store this intermediate state/value because a later heap decision needs it.
            prev = v
        # Write this value’s rank back into its ORIGINAL array position.
        ans[i] = rank
    # Return the final result produced by the heap process.
    return ans
# Run the small example and print the result so we can verify the idea.
print(solve([40, 10, 20, 10]))
