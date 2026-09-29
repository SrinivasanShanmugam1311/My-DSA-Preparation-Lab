"""
1. PROBLEM IN SIMPLE WORDS
Single-Threaded CPU
Small example: [1,2],[2,4],[3,1]
Expected: Order 0,2,1.

2. WHY / PURPOSE
Find CPU execution order for tasks arriving over time.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Arrival decides AVAILABLE; shortest processing time decides NEXT.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Sort by enqueue time + min heap (processing,index).
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
Example: [1,2],[2,4],[3,1]
Goal: Order 0,2,1.
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
If I see: Arriving jobs + shortest available -> min heap.

15. ONE-LINE MEMORY TRICK
Arrived? PUSH. Shortest? POP. Finish. Repeat.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Add jobs that have arrived; among available jobs, run the shortest processing-time job.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def solve(tasks):
    # Sort jobs by enqueue time so newly arrived jobs can be added in time order.
    jobs = sorted(((e, p, i) for i, (e, p) in enumerate(tasks)))
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Store the final answer/order here as heap choices are made.
    out = []
    # Track the current simulated time. Availability/cooldown decisions depend on this value.
    t = 0
    # Start at the first not-yet-processed input/project/job.
    i = 0
    # Keep repeating the heap process while there is still useful work/candidates left.
    while i < len(jobs) or h:
        # If no heap candidate is available, handle the empty/waiting case instead of popping an empty heap.
        if not h and t < jobs[i][0]:
            # Store this intermediate state/value because a later heap decision needs it.
            t = jobs[i][0]
        # Keep repeating the heap process while there is still useful work/candidates left.
        while i < len(jobs) and jobs[i][0] <= t:
            # Store this intermediate state/value because a later heap decision needs it.
            e, p, idx = jobs[i]
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (p, idx))
            # Move this counter/index/time forward by one because one step/item has just been processed.
            i += 1
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        p, idx = heapq.heappop(h)
        # Add the selected heap result to the final output.
        out.append(idx)
        # Advance current time by this task’s full processing time; the CPU does not interrupt the task midway.
        t += p
    # Return the final result produced by the heap process.
    return out
# Run the small example and print the result so we can verify the idea.
print(solve([[1, 2], [2, 4], [3, 1]]))
