from heap_helpers import min_heap_push, min_heap_pop, min_heap_root


class KthLargest:
    def __init__(self, k, numbers):
        self.k = k
        self.winners = []  # Keep only K largest values seen so far.

        for number in numbers:
            self.add(number)

    def add(self, number):
        min_heap_push(self.winners, number)

        # If we have K+1 values, remove the smallest one.
        # That leaves only the K largest winners.
        if len(self.winners) > self.k:
            min_heap_pop(self.winners)

        # Smallest among K largest = Kth largest.
        return min_heap_root(self.winners)


stream = KthLargest(3, [4, 5, 8, 2])
print(stream.add(3))
print(stream.add(10))
print(stream.add(9))
