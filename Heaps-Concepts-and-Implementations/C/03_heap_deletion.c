/*
1. PROBLEM IN SIMPLE WORDS
Delete Heap Root
Small example: [2,5,10,8]
Expected: Delete min root 2.

2. WHY / PURPOSE
Remove min/max while keeping complete-tree shape.
Main difficulty: we need the correct next candidate without repeatedly scanning everything.

3. CORE MENTAL MODEL
Last item fills root hole, then moves DOWN.

4. WHY THIS DATA STRUCTURE / ALGORITHM?
Move last to root, then heapify down.
A simple full scan can work on tiny input, but repeated scans may redo a lot of work. A heap keeps the best current candidate at the root.

5. EVERY VARIABLE
heap -> current candidates.
root -> best current candidate.
answer/out -> result built so far.
i/j/index -> where a value/task came from when needed.
k -> how many answers/winners are required when the problem has K.

6. PICTORIAL EXPLANATION
CANDIDATES
    ↓
  HEAP
    ↓
ROOT = best current candidate
    ↓
 POP / PROCESS
    ↓
UPDATE → maybe PUSH → repeat

7. STEP-BY-STEP SIMULATION
Example: [2,5,10,8]
Goal: Delete min root 2.
1) Start with the candidates allowed by the problem.
2) Put the useful candidates in the heap.
3) Read/POP the root because the root is the best current candidate.
4) Update the state. PUSH a new candidate only when the problem makes it available.
5) Repeat until the answer is complete.

8. RECURSION V-SHAPE
Not used in the interview solution here. Heap problems are normally solved iteratively. Heapify itself can be recursive, but an iterative loop is simple and avoids call-stack space.

9. WHOLE MOVIE
Find/receive eligible candidates -> PUSH -> root is best -> POP/process -> state changes -> PUSH newly eligible candidate -> repeat.

10/11. CODE
See this file for the language-specific implementation.

12. MAP CODE TO MENTAL MODEL
heappush / heap push = candidate enters the waiting room.
heappop / heap pop = choose the best current candidate.
comparison = defines what “best” means for this problem.

13. TIME AND SPACE COMPLEXITY
A heap PUSH/POP is usually O(log H), where H is current heap size. Root lookup is O(1). Exact total complexity depends on how many items are pushed/popped; see comments/code pattern.

14. PATTERN RECOGNITION
If I see: Remove heap root -> last to root + down.

15. ONE-LINE MEMORY TRICK
Delete root = last to root, then DOWN.
*/


// ============================================================
// TEACHING-COMMENT EDITION
// Read each block as: WHAT happens -> WHY it is needed -> HOW it helps.
// Heap movement is kept on separate lines for easy debugging and study.
// ============================================================

#include <stdio.h>
#include <stdlib.h>

/*
 * CODE MENTAL MODEL
 * Remove the root. Move the last value to the root. Then repair downward.
 *
 * Read the code from top to bottom.
 * Helper functions do one heap operation at a time.
 */

/*
 * ============================================================
 * ONE STANDARD HEAP TEMPLATE USED IN THIS PACK
 * ============================================================
 *
 * Keep these SAME function names in every heap problem:
 *
 *     swap()
 *     min_push()
 *     min_pop()
 *     max_push()
 *     max_pop()
 *
 * Keep these SAME variable names inside the helper functions:
 *
 *     heap      -> array that stores the heap
 *     size      -> how many values are currently in the heap
 *     value     -> new value we want to insert
 *     index     -> position we are currently checking
 *     parent    -> parent position
 *     left      -> left-child position
 *     right     -> right-child position
 *     smallest  -> smallest position found while fixing a min heap
 *     largest   -> largest position found while fixing a max heap
 *     answer    -> root value that we are removing and returning
 *
 * The goal is simple:
 * Learn ONE heap template and reuse it everywhere.
 */

/* Swap two values.
 * We need this when a heap value has to move UP or DOWN.
 */
static void swap(int *first_value, int *second_value)
{
    // Save the first value before changing it.
    int temporary_value = *first_value;

    // Put the second value in the first position.
    *first_value = *second_value;

    // Put the saved first value in the second position.
    *second_value = temporary_value;
}

/*
 * Add one value to a MIN HEAP.
 *
 * Movie:
 * put value at END -> compare with parent -> smaller value moves UP.
 */
static void min_push(int heap[], int *size, int value)
{
    // The current size is also the next empty array position.
    int index = *size;

    // One new value is entering the heap.
    (*size)++;

    // Always insert at the END first.
    // This keeps the binary tree complete.
    heap[index] = value;

    // The new value may be smaller than its parent.
    // If so, keep moving the new value UP.
    while (index > 0)
    {
        // Find the parent of the current position.
        int parent = (index - 1) / 2;

        // MIN-HEAP rule: parent <= child.
        // If this is already true, the value is in the correct place.
        if (heap[parent] <= heap[index])
        {
            break;
        }

        // The child is smaller than the parent.
        // Swap them so the smaller value moves one level UP.
        swap(&heap[parent], &heap[index]);

        // Our value moved to the parent's old position.
        // Continue checking from that new position.
        index = parent;
    }
}

/*
 * Remove and return the MIN-HEAP root.
 * The root is the smallest value.
 *
 * Movie:
 * save root -> last value comes to root -> smaller child moves UP -> repair DOWN.
 */
static int min_pop(int heap[], int *size)
{
    // Save the root before changing the heap.
    // In a min heap, this is the smallest value.
    int answer = heap[0];

    // One value is leaving the heap.
    (*size)--;

    // Move the LAST value to the root.
    // This removes the root without creating a hole in the complete tree.
    heap[0] = heap[*size];

    // The root changed, so start repairing from index 0.
    int index = 0;

    // Move the new root DOWN until the min-heap rule is correct again.
    while (1)
    {
        // Find the left and right child positions.
        int left = (2 * index) + 1;
        int right = (2 * index) + 2;

        // First assume the current value is already the smallest.
        int smallest = index;

        // If the left child exists and is smaller,
        // remember the left child as the best value to move UP.
        if (left < *size && heap[left] < heap[smallest])
        {
            smallest = left;
        }

        // If the right child exists and is even smaller,
        // remember the right child instead.
        if (right < *size && heap[right] < heap[smallest])
        {
            smallest = right;
        }

        // If the current value is already the smallest,
        // the min-heap rule is correct. Stop.
        if (smallest == index)
        {
            break;
        }

        // A child is smaller than the current value.
        // Move that smaller child UP and the current value DOWN.
        swap(&heap[index], &heap[smallest]);

        // Continue from the position where our value moved DOWN.
        index = smallest;
    }

    // Return the old root: the smallest value that we removed.
    return answer;
}

/*
 * Add one value to a MAX HEAP.
 *
 * Movie:
 * put value at END -> compare with parent -> larger value moves UP.
 */
static void max_push(int heap[], int *size, int value)
{
    // The current size is the next empty array position.
    int index = *size;

    // One new value is entering the heap.
    (*size)++;

    // Insert at the END first to keep the tree complete.
    heap[index] = value;

    // The new value may be larger than its parent.
    // If so, keep moving the new value UP.
    while (index > 0)
    {
        // Find the parent of the current position.
        int parent = (index - 1) / 2;

        // MAX-HEAP rule: parent >= child.
        // If this is already true, the value is in the correct place.
        if (heap[parent] >= heap[index])
        {
            break;
        }

        // The child is larger than the parent.
        // Swap them so the larger value moves one level UP.
        swap(&heap[parent], &heap[index]);

        // Continue checking from the new position.
        index = parent;
    }
}

/*
 * Remove and return the MAX-HEAP root.
 * The root is the largest value.
 *
 * Movie:
 * save root -> last value comes to root -> larger child moves UP -> repair DOWN.
 */
static int max_pop(int heap[], int *size)
{
    // Save the root before changing the heap.
    // In a max heap, this is the largest value.
    int answer = heap[0];

    // One value is leaving the heap.
    (*size)--;

    // Move the LAST value to the root.
    // This keeps the binary tree complete.
    heap[0] = heap[*size];

    // The root changed, so start repairing from index 0.
    int index = 0;

    // Move the new root DOWN until the max-heap rule is correct again.
    while (1)
    {
        // Find the left and right child positions.
        int left = (2 * index) + 1;
        int right = (2 * index) + 2;

        // First assume the current value is already the largest.
        int largest = index;

        // If the left child exists and is larger,
        // remember the left child as the best value to move UP.
        if (left < *size && heap[left] > heap[largest])
        {
            largest = left;
        }

        // If the right child exists and is even larger,
        // remember the right child instead.
        if (right < *size && heap[right] > heap[largest])
        {
            largest = right;
        }

        // If the current value is already the largest,
        // the max-heap rule is correct. Stop.
        if (largest == index)
        {
            break;
        }

        // A child is larger than the current value.
        // Move that larger child UP and the current value DOWN.
        swap(&heap[index], &heap[largest]);

        // Continue from the position where our value moved DOWN.
        index = largest;
    }

    // Return the old root: the largest value that we removed.
    return answer;
}

int main()
{
  int h[20];
  int n = 0;
  int a[] = {2, 5, 10, 8};
  for (int i = 0; i < 4; i++)
    min_push(h, &n, a[i]);

  printf("pop=%d\n", min_pop(h, &n));
  for (int i = 0; i < n; i++)
    printf("%d ", h[i]);

}


