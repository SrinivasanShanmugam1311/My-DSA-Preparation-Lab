from heap_helpers import max_heap_push, max_heap_pop


def last_stone_weight(stones):
    heap = []

    # Every stone is initially available.
    for stone in stones:
        max_heap_push(heap, stone)

    # We need TWO largest stones each round.
    while len(heap) > 1:
        largest = max_heap_pop(heap)
        second_largest = max_heap_pop(heap)

        # Equal stones both disappear.
        # Unequal stones leave the difference as a new stone.
        if largest != second_largest:
            leftover = largest - second_largest
            max_heap_push(heap, leftover)

    return max_heap_pop(heap) if heap else 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
