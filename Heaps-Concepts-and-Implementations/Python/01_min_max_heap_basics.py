"""
1. PROBLEM IN SIMPLE WORDS
Min / Max Heap Basics
Small example: [10,20,30]
Expected: Build a min heap and read root.

2. WHY / PURPOSE
Need repeated smallest/largest quickly.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Heap = complete tree; root keeps the current extreme.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Use array indexes to represent a complete tree.
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
Example: [10,20,30]
Goal: Build a min heap and read root.
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
If I see: Repeated extreme -> heap.

15. ONE-LINE MEMORY TRICK
Root is the extreme; children obey heap rule.
"""

# ============================================================
# PYTHON CODE — VERY SIMPLE TEACHING VERSION
# ============================================================
#
# OVERALL PURPOSE:
# Build a MIN HEAP and a MAX HEAP from the same numbers.
# Then read the root to get the smallest or largest value quickly.
# ============================================================

# Import Python's built-in heap library.
# WHY? heapq already knows how to keep MIN-HEAP order after PUSH/POP.
import heapq

# These are the numbers we want to place into both heaps.
# We use the same input so the min-heap and max-heap behavior is easy to compare.
numbers = [10, 20, 30, 5]

# ------------------------------------------------------------
# MIN HEAP
# ------------------------------------------------------------

# Start with an empty MIN HEAP.
# Python heapq is a MIN HEAP by default.
min_heap = []

# Visit every input number one by one.
# "number" means the current value we are inserting now.
for number in numbers:
    # PUSH the number normally.
    # WHAT? Add this number to the heap.
    # WHY? We want all input values to become heap candidates.
    # HOW? heappush() automatically repairs heap order, so the smallest value moves toward index 0.
    heapq.heappush(min_heap, number)

# The root of a Python min heap is at index 0.
# Reading min_heap[0] does NOT remove it.
# Here the root is 5, which is the smallest input value.
print("min root:", min_heap[0])

# ------------------------------------------------------------
# MAX HEAP USING THE NEGATIVE-VALUE TRICK
# ------------------------------------------------------------

# Start another empty heap.
# We will make this behave like a MAX HEAP by storing negative numbers.
max_heap = []

# Visit every original number again.
for number in numbers:
    # Store the NEGATIVE value.
    # Example: original 30 becomes -30.
    #
    # WHY does this create max-heap behavior?
    # Among -10, -20, -30, -5, the smallest value is -30.
    # Python's MIN HEAP therefore puts -30 at the root.
    # But -30 represents the original value 30, which was the LARGEST number.
    heapq.heappush(max_heap, -number)

# max_heap[0] is the most negative stored value, for example -30.
# Negate it again: -(-30) = 30.
# This gives us the largest ORIGINAL value.
print("max root:", -max_heap[0])
