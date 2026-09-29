#include <stdio.h>
#include "../heap_helpers.h"

int main(void)
{
    int numbers[] = {7, 2, 9, 4, 8};
    int count = 5;
    int k = 3;

    int winners[20];
    int size = 0;

    for (int i = 0; i < count; i++)
    {
        int number = numbers[i];

        if (size < k)
        {
            min_push(winners, &size, number); /* Fill the K winner chairs first. */
        }
        else if (number > min_root(winners))
        {
            min_pop(winners, &size);          /* Remove weakest current winner. */
            min_push(winners, &size, number); /* Better candidate takes its chair. */
        }
    }

    printf("Kth-largest boundary / weakest winner = %d\n", min_root(winners));
    return 0;
}
