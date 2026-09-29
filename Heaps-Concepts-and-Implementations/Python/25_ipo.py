"""
1. PROBLEM IN SIMPLE WORDS
IPO
Small example: K=2,W=0; capital=[0,1,1], profit=[1,2,3]
Expected: Return 4.

2. WHY / PURPOSE
Maximize capital after at most K projects.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Capital unlocks projects; among affordable projects choose max profit.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Sort by required capital + max heap of profits.
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
Example: K=2,W=0; capital=[0,1,1], profit=[1,2,3]
Goal: Return 4.
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
If I see: Eligibility threshold + best reward -> max heap.

15. ONE-LINE MEMORY TRICK
Unlock affordable projects; take max profit.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Add projects we can currently afford; among them, choose the highest-profit project.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(k, w, profits, capital):
    # Sort projects by required capital so we can unlock affordable projects from left to right.
    projects = sorted(zip(capital, profits))
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Start at the first not-yet-processed input/project/job.
    i = 0
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for _ in range(k):
        # Keep repeating the heap process while there is still useful work/candidates left.
        while i < len(projects) and projects[i][0] <= w:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, -projects[i][1])
            # Move this counter/index/time forward by one because one step/item has just been processed.
            i += 1
        # If no heap candidate is available, handle the empty/waiting case instead of popping an empty heap.
        if not h:
            # Stop this loop because no more useful work can be done in this direction.
            break
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        w += -heapq.heappop(h)
    # Return the final result produced by the heap process.
    return w
# Run the small example and print the result so we can verify the idea.
print(solve(2, 0, [1, 2, 3], [0, 1, 1]))
