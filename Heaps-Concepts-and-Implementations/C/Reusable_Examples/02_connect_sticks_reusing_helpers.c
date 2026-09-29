#include <stdio.h>
#include "../heap_helpers.h"

int main(void)
{
    int sticks[] = {2, 4, 3};
    int heap[20];
    int size = 0;
    int total_cost = 0;

    for (int i = 0; i < 3; i++)
    {
        min_push(heap, &size, sticks[i]); /* Every stick becomes a candidate. */
    }

    while (size > 1)
    {
        int first = min_pop(heap, &size);  /* Smallest stick. */
        int second = min_pop(heap, &size); /* Second-smallest stick. */
        int combined = first + second;

        total_cost += combined;            /* This connection costs first + second. */
        min_push(heap, &size, combined);   /* New combined stick returns to heap. */
    }

    printf("minimum total cost = %d\n", total_cost);
    return 0;
}
