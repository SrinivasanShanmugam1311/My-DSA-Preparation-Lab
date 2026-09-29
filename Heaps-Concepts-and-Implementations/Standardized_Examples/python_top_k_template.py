from Python.heap_helpers import min_heap_push, min_heap_pop, min_heap_root, heap_size


def kth_largest(values, number_of_winners):
    """Keep only the K largest values. Root becomes the Kth largest."""
    heap = []

    for incoming_value in values:
        # New value becomes a candidate.
        min_heap_push(heap, incoming_value)

        # We only have K winner chairs.
        # If we have too many, remove the weakest winner.
        if heap_size(heap) > number_of_winners:
            min_heap_pop(heap)

    # Smallest among the K winners = Kth largest overall.
    return min_heap_root(heap)


print(kth_largest([3, 2, 1, 5, 6, 4], 2))
