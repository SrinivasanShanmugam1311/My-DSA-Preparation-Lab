"""
1. PROBLEM IN SIMPLE WORDS
Task Scheduler
Small example: A,A,A,B,B,B; n=2
Expected: One valid order A,B,idle,A,B,idle,A,B.

2. WHY / PURPOSE
Schedule repeated tasks with cooldown and avoid idle when possible.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Cooldown says READY? Frequency says WHO next?

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Max heap for ready frequencies + cooldown queue.
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
Example: A,A,A,B,B,B; n=2
Goal: One valid order A,B,idle,A,B,idle,A,B.
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
If I see: Ready task with largest remaining count -> max heap.

15. ONE-LINE MEMORY TRICK
Cooldown decides ready; Max Heap picks most remaining.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Cooldown decides what is READY; a max heap chooses the ready task with the most remaining work.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq
# Counter counts task frequencies. deque stores cooldown items in time order.
from collections import Counter, deque

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(tasks, n):
    # Count each task. Store negative counts so Python’s min heap behaves like a MAX HEAP of remaining frequencies.
    h = [-c for c in Counter(tasks).values()]
    # Rearrange the existing list into heap order in-place. This prepares the root for fast extreme selection.
    heapq.heapify(h)
    # Cooldown queue stores tasks that still have work but are temporarily not allowed to run.
    cool = deque()
    # Track the current simulated time. Availability/cooldown decisions depend on this value.
    time = 0
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h or cool:
        # Move this counter/index/time forward by one because one step/item has just been processed.
        time += 1
        # Check whether this candidate/state needs a heap update.
        if h:
            # POP the heap root. This removes the best current candidate according to this heap’s ordering.
            rem = heapq.heappop(h) + 1
            # Check whether this candidate/state needs a heap update.
            if rem < 0:
                cool.append((time + n, rem))
        # Check whether this candidate/state needs a heap update.
        if cool and cool[0][0] == time:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, cool.popleft()[1])
    # Return the final result produced by the heap process.
    return time
# Run the small example and print the result so we can verify the idea.
print(solve(list('AAABBB'), 2))
