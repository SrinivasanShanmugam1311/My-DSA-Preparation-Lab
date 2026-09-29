"""
1. PROBLEM IN SIMPLE WORDS
Design Twitter
Small example: Alice 10,7; Bob 9,6; You 8,4
Expected: Feed 10,9,8,7,...

2. WHY / PURPOSE
Build recent news feed across followed users.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Each user offers newest tweet; after pop, expose that user’s next older tweet.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Max heap by timestamp over current tweet candidates.
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
Example: Alice 10,7; Bob 9,6; You 8,4
Goal: Feed 10,9,8,7,...
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
If I see: Newest among sorted streams -> max heap.

15. ONE-LINE MEMORY TRICK
Newest tweet POP; expose next older from same user.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Keep the newest current tweet from each user; pop newest overall, then expose that user’s next older tweet.
#
# HOW TO READ THIS FILE:
# Every important line explains WHAT it does and WHY it helps.
# ============================================================

# Import Python’s heap library. heapq is a MIN HEAP by default.
import heapq

# Define the solution/helper function. The actual heap steps happen inside this block.
def feed(streams, limit=10):
    # Start with an empty heap. Candidates will enter only when the algorithm says they are useful/eligible.
    h = []
    # Store the final answer/order here as heap choices are made.
    out = []
    # Visit the needed items one by one so each item gets one chance to enter or affect the heap.
    for u, tweets in enumerate(streams):
        # Check whether this candidate/state needs a heap update.
        if tweets:
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (-tweets[0][0], tweets[0][1], u, 0))
    # Keep repeating the heap process while there is still useful work/candidates left.
    while h and len(out) < limit:
        # POP the heap root. This removes the best current candidate according to this heap’s ordering.
        nt, tid, u, j = heapq.heappop(h)
        # Add the selected heap result to the final output.
        out.append(tid)
        # Check whether this candidate/state needs a heap update.
        if j + 1 < len(streams[u]):
            # Store this intermediate state/value because a later heap decision needs it.
            t, tid2 = streams[u][j + 1]
            # PUSH this candidate into the heap. heapq automatically repairs heap order after insertion.
            heapq.heappush(h, (-t, tid2, u, j + 1))
    # Return the final result produced by the heap process.
    return out
# Store this intermediate state/value because a later heap decision needs it.
streams = [[(10, 'A3'), (7, 'A2')], [(9, 'B3'), (6, 'B2')], [(8, 'Y2'), (4, 'Y1')]]
# Run the small example and print the result so we can verify the idea.
print(feed(streams))
