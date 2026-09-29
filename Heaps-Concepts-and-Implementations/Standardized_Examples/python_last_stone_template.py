from Python.heap_helpers import max_heap_build, max_heap_pop, max_heap_push, heap_size


def last_stone_weight(stones):
    """Repeatedly take the two heaviest stones."""
    heap = max_heap_build(stones)

    while heap_size(heap) > 1:
        heaviest_stone = max_heap_pop(heap)
        second_heaviest_stone = max_heap_pop(heap)

        if heaviest_stone != second_heaviest_stone:
            leftover_stone = heaviest_stone - second_heaviest_stone
            max_heap_push(heap, leftover_stone)

    if heap_size(heap) == 1:
        return max_heap_pop(heap)

    return 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
