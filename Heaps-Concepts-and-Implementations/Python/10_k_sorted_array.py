"""
1. PROBLEM IN SIMPLE WORDS
Sort K-Sorted Array
Small example: [3,1,2,5,4], K=2
Expected: Return [1,2,3,4,5].

2. WHY / PURPOSE
Sort an almost-sorted array efficiently.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Correct next value must be among next K+1 candidates.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Min heap of K+1; pop smallest and push next.
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
Example: [3,1,2,5,4], K=2
Goal: Return [1,2,3,4,5].
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
If I see: Element displaced <=K -> min heap K+1.

15. ONE-LINE MEMORY TRICK
K-sorted = look at K+1, pop smallest.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Keep K+1 nearby candidates and repeatedly output the smallest one.
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
    # Store the final answer/order here as heap choices are made.
    out = []
    # Start at the first not-yet-processed input/project/job.
    i = 0
    # Keep repeating the heap process while there is still useful work/candidates left.
    while i < len(a) and i < k + 1:
        # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
        heapq.heappush(h, a[i])
        # Move this counter/index/time forward by one because one step/item has just been processed.
        i += 1
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h:
        # POP the current root because it is the candidate we want to process/remove now.
        out.append(heapq.heappop(h))
        # Check whether this candidate/state needs a heap update.
        if i < len(a):
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, a[i])
            # Move this counter/index/time forward by one because one step/item has just been processed.
            i += 1
    # Return the final result produced by the heap process.
    return out
# Run the small example and print the result so we can verify the idea.
print(solve([3, 1, 2, 5, 4], 2))
