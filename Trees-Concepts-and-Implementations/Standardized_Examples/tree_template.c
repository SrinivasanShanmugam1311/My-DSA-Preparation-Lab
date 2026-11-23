#include <stdio.h>
#include <assert.h>
#include <stddef.h>

/* A separate teaching example; not a replacement for original code. */
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

int height(TreeNode *root)
{
    /* Empty subtree has zero height (counting nodes). */
    if (root == NULL)
        return 0;
    int left_height = height(root->left);
    int right_height = height(root->right);
    return 1 + (left_height > right_height ? left_height : right_height);
}

void preorder(TreeNode *root)
{
    if (root == NULL)
        return;
    printf("%d ", root->val);
    preorder(root->left);
    preorder(root->right);
}

TreeNode *search_bst(TreeNode *root, int key)
{
    while (root != NULL && root->val != key) {
        if (key < root->val)
            root = root->left;
        else
            root = root->right;
    }
    return root;
}

/* Caller supplies queue capacity >= maximum pending nodes. Return 0 on overflow. */
int level_order(TreeNode *root, TreeNode **queue, size_t capacity)
{
    size_t front = 0, rear = 0, count = 0;
    if (root == NULL)
        return 1;
    if (capacity == 0)
        return 0;
    queue[rear] = root;
    rear = (rear + 1) % capacity;
    count++;
    while (count > 0) {
        size_t level_size = count;
        for (size_t i = 0; i < level_size; i++) {
            TreeNode *node = queue[front];
            front = (front + 1) % capacity;
            count--;
            printf("%d ", node->val);
            TreeNode *children[] = {node->left, node->right};
            for (size_t j = 0; j < 2; j++) {
                if (children[j] != NULL) {
                    if (count == capacity)
                        return 0;
                    queue[rear] = children[j];
                    rear = (rear + 1) % capacity;
                    count++;
                }
            }
        }
        puts("");
    }
    return 1;
}

int main(void)
{
    TreeNode left = {1, NULL, NULL};
    TreeNode right = {3, NULL, NULL};
    TreeNode root = {2, &left, &right};
    TreeNode *queue[3];
    assert(height(&root) == 2);
    assert(search_bst(&root, 3) == &right);
    assert(search_bst(&root, 4) == NULL);
    preorder(&root);
    puts("");
    assert(level_order(&root, queue, 3));
    return 0;
}
