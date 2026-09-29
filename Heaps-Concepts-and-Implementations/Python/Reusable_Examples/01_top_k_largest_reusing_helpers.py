from heap_helpers import min_heap_push, min_heap_root, min_heap_replace_root


def top_k_largest(numbers, k):
    # This heap stores ONLY the current K largest winners.
    winners = []

    for number in numbers:
        # Empty winner chair available? Put the number in.
        if len(winners) < k:
            min_heap_push(winners, number)
            continue

        # Root = smallest among our K winners = weakest winner.
        weakest_winner = min_heap_root(winners)

        # A new number enters only if it is better than the weakest winner.
        if number > weakest_winner:
            min_heap_replace_root(winners, number)

    return sorted(winners)


print(top_k_largest([7, 2, 9, 4, 8], 3))
