#include <stdio.h>
#include "../C/heap_helpers.h"

int kth_largest(int values[], int number_of_values, int number_of_winners)
{
    int heap[100];
    int heap_size = 0;

    for (int current_index = 0; current_index < number_of_values; current_index++)
    {
        int incoming_value = values[current_index];
        min_heap_push(heap, &heap_size, incoming_value);

        if (heap_size > number_of_winners)
            min_heap_pop(heap, &heap_size);
    }

    return min_heap_root(heap, heap_size);
}

int main(void)
{
    int values[] = {3, 2, 1, 5, 6, 4};
    printf("%d\n", kth_largest(values, 6, 2));
    return 0;
}
