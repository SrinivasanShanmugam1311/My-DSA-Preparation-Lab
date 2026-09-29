"""
1. PROBLEM IN SIMPLE WORDS
Maximum Sum Combination
Small example: A=[4,2,5], B=[8,0,3], K=3
Expected: Return 13,12,10.

2. WHY / PURPOSE
Get K largest pair sums without generating N^2 pairs.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Start best+best; expose one-step-down pairs; heap picks best exposed sum.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Sort descending + max heap frontier + visited pairs.
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
Example: A=[4,2,5], B=[8,0,3], K=3
Goal: Return 13,12,10.
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
If I see: Top pair combinations -> sorted frontier + max heap.

15. ONE-LINE MEMORY TRICK
Best pair -> expose neighbors -> heap picks next best.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Start from the best pair, then reveal nearby next pairs while a max heap chooses the best discovered sum.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(A, B, k):
    # Sort descending so index 0 starts with the largest value and moving right means a smaller choice.
    A = sorted(A, reverse=True)
    # Sort descending so index 0 starts with the largest value and moving right means a smaller choice.
    B = sorted(B, reverse=True)
    # Start with the best possible pair A[0]+B[0]. Store negative sum so heapq acts like a MAX HEAP.
    h = [(-(A[0] + B[0]), 0, 0)]
    # Remember already-discovered pairs so the same pair is never pushed into the heap twice.
    seen = {(0, 0)}
    # Store the final answer/order here as heap choices are made.
    out = []
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h and len(out) < k:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        ns, i, j = heapq.heappop(h)
        # Add the selected heap result to the final output.
        out.append(-ns)
        # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
        for ni, nj in ((i + 1, j), (i, j + 1)):
            # Check whether this candidate/state needs a heap update.
            if ni < len(A) and nj < len(B) and ((ni, nj) not in seen):
                seen.add((ni, nj))
                # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
                heapq.heappush(h, (-(A[ni] + B[nj]), ni, nj))
    # Return the final result produced by the heap process.
    return out
# Run the small example and print the result so we can verify the idea.
print(solve([4, 2, 5], [8, 0, 3], 3))
