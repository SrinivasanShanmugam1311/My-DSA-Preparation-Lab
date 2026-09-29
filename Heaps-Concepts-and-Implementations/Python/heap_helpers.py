"""
ONE STANDARD PYTHON HEAP HELPER TEMPLATE

Same names to remember across the pack:
    min_push(heap, value)
    min_pop(heap)
    max_push(heap, value)
    max_pop(heap)

Python heapq is a MIN HEAP.
For MAX HEAP behavior we store negative values.
"""

import heapq


def min_push(heap, value):
    """Put one value into a MIN HEAP."""
    # WHAT? Add the value to the heap.
    # WHY? The value is now a candidate for the smallest value.
    # HOW? heapq repairs the heap automatically after insertion.
    heapq.heappush(heap, value)


def min_pop(heap):
    """Remove and return the smallest value."""
    # WHAT? Remove the root of the min heap.
    # WHY? The root is the smallest current value.
    # HOW? heapq removes it and repairs the heap automatically.
    return heapq.heappop(heap)


def max_push(heap, value):
    """Put one original value into a MAX HEAP using negative values."""
    # Python heapq is a min heap.
    # Store -value so the largest original value acts like the smallest stored value.
    heapq.heappush(heap, -value)


def max_pop(heap):
    """Remove and return the largest ORIGINAL value."""
    # heapq removes the smallest stored negative value.
    # Negate it again to get the original largest value.
    return -heapq.heappop(heap)
