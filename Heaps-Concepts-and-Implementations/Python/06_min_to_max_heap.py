"""
1. PROBLEM IN SIMPLE WORDS
Convert Min Heap to Max Heap
Small example: [1,3,2,7,6,4]
Expected: Convert to max heap.

2. WHY / PURPOSE
Convert heap type without changing elements.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Keep the same complete-tree shape; change the rule.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Run max-heapify bottom-up.
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
Example: [1,3,2,7,6,4]
Goal: Convert to max heap.
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
If I see: Change heap priority -> rebuild with new comparison.

15. ONE-LINE MEMORY TRICK
Min to Max = same tree, opposite comparison.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Turn the same complete-tree array into a max heap by repairing parents with the max-heap rule.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Define the solution/helper function. The actual heap steps happen inside this block.
def down(a, n, i):
    # Keep repeating the heap process while there is still useful work/candidates left.
    while True:
        # Assume the current node is already the largest; children may prove otherwise.
        b = i
        # Calculate the left-child index of the current parent.
        l = 2 * i + 1
        # Calculate the right-child index of the current parent.
        r = 2 * i + 2
        # Check whether this candidate/state needs a heap update.
        if l < n and a[l] > a[b]:
            # Remember the larger child as the node that should move UP.
            b = l
        # Check whether this candidate/state needs a heap update.
        if r < n and a[r] > a[b]:
            # Remember the larger child as the node that should move UP.
            b = r
        # Check whether this candidate/state needs a heap update.
        if b == i:
            # Stop this loop because no more useful work can be done in this direction.
            break
        # Swap with the larger child so the max-heap rule becomes correct one level at a time.
        a[i], a[b] = (a[b], a[i])
        # Store this intermediate state/value because a later heap decision needs it.
        i = b
# Store this intermediate state/value because a later heap decision needs it.
a = [1, 3, 2, 7, 6, 4]
# Visit the needed items one by one so each item gets one chance to enter or affect the heap.
for i in range(len(a) // 2 - 1, -1, -1):
    down(a, len(a), i)
# Run the small example and print the result so we can verify the idea.
print(a)
