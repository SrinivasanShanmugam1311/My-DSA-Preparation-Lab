"""
1. PROBLEM IN SIMPLE WORDS
Delete Heap Root
Small example: [2,5,10,8]
Expected: Delete min root 2.

2. WHY / PURPOSE
Remove min/max while keeping complete-tree shape.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Last item fills root hole, then moves DOWN.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Move last to root, then heapify down.
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
Example: [2,5,10,8]
Goal: Delete min root 2.
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
If I see: Remove heap root -> last to root + down.

15. ONE-LINE MEMORY TRICK
Delete root = last to root, then DOWN.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Remove the minimum root, move the last value to the root, then repair DOWN.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Define the solution/helper function. The actual heap steps happen inside this block.
def pop_min(h):
    # Save the root before changing the heap. In a min heap this is the smallest value we must return.
    ans = h[0]
    # Remove the last value. It is the safe value to move into the root hole while keeping complete-tree shape.
    last = h.pop()
    # If no heap candidate is available, handle the empty/waiting case instead of popping an empty heap.
    if not h:
        # Return the final result produced by the heap process.
        return ans
    # Move the old last value to the root. Now only heap order may be broken, so we repair DOWN.
    h[0] = last
    # Start at the first not-yet-processed input/project/job.
    i = 0
    # Keep repeating the heap process while there is still useful work/candidates left.
    while True:
        # Calculate the left-child index of the current parent.
        l = 2 * i + 1
        # Calculate the right-child index of the current parent.
        r = 2 * i + 2
        # Assume the current node is already the smallest; children may prove otherwise.
        s = i
        # Check whether this candidate/state needs a heap update.
        if l < len(h) and h[l] < h[s]:
            # Remember the smaller child as the node that should move UP.
            s = l
        # Check whether this candidate/state needs a heap update.
        if r < len(h) and h[r] < h[s]:
            # Remember the smaller child as the node that should move UP.
            s = r
        # Check whether this candidate/state needs a heap update.
        if s == i:
            # Stop this loop because no more useful work can be done in this direction.
            break
        # Swap with the smaller child so the min-heap rule becomes correct one level at a time.
        h[i], h[s] = (h[s], h[i])
        # Store this intermediate state/value because a later heap decision needs it.
        i = s
    # Return the final result produced by the heap process.
    return ans
# Store this intermediate state/value because a later heap decision needs it.
h = [2, 5, 10, 8]
# Run the small example and print the result so we can verify the idea.
print(pop_min(h), h)
