"""
1. PROBLEM IN SIMPLE WORDS
Check Min Heap
Small example: [10,20,30,40,50,60]
Expected: Return true.

2. WHY / PURPOSE
Verify whether array already satisfies min-heap rule.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Every parent must be <= each existing child.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Scan parent indexes and compare children.
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
Example: [10,20,30,40,50,60]
Goal: Return true.
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
If I see: Verify heap -> parent-child comparisons.

15. ONE-LINE MEMORY TRICK
Every parent <= both children.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Check every parent against its existing children; no parent may be larger than a child.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(a):
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for i in range(len(a) // 2):
        # Calculate the left-child index of the current parent.
        l = 2 * i + 1
        # Calculate the right-child index of the current parent.
        r = 2 * i + 2
        # Check whether this candidate/state needs a heap update.
        if l < len(a) and a[i] > a[l]:
            # Return the final result produced by the heap process.
            return False
        # Check whether this candidate/state needs a heap update.
        if r < len(a) and a[i] > a[r]:
            # Return the final result produced by the heap process.
            return False
    # Return the final result produced by the heap process.
    return True
# Run the small example and print the result so we can verify the idea.
print(solve([10, 20, 30, 40, 50, 60]))
