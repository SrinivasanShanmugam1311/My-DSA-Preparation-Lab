#ifndef HEAP_HELPERS_H
#define HEAP_HELPERS_H

void swap(int *first_value, int *second_value);
void min_push(int heap[], int *size, int value);
int min_pop(int heap[], int *size);
void max_push(int heap[], int *size, int value);
int max_pop(int heap[], int *size);

#endif
