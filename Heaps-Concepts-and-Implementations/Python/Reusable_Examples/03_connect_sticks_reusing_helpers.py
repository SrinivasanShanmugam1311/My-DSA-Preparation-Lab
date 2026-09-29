from heap_helpers import min_heap_push, min_heap_pop


def connect_sticks(sticks):
    heap = []

    for length in sticks:
        min_heap_push(heap, length)

    total_cost = 0

    # Cheapest strategy: repeatedly connect the TWO smallest sticks.
    while len(heap) > 1:
        first = min_heap_pop(heap)
        second = min_heap_pop(heap)

        combined = first + second
        total_cost += combined

        # The combined stick becomes a candidate for the next round.
        min_heap_push(heap, combined)

    return total_cost


print(connect_sticks([2, 4, 3]))
