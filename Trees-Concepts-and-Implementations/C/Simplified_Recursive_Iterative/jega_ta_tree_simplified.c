#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXN 10000

typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

typedef struct TernaryNode {
    int val;
    struct TernaryNode *left;
    struct TernaryNode *middle;
    struct TernaryNode *right;
} TernaryNode;

int max2(int a, int b)
{
    return a > b ? a : b;
}

/* ============================================================
 * Jega 171: DFS Traversals
 * Recursive and iterative
 * ============================================================ */

void preorderRecursive(TreeNode *root)
{
    if (!root) return;
    printf("%d ", root->val);
    preorderRecursive(root->left);
    preorderRecursive(root->right);
}

void inorderRecursive(TreeNode *root)
{
    if (!root) return;
    inorderRecursive(root->left);
    printf("%d ", root->val);
    inorderRecursive(root->right);
}

void postorderRecursive(TreeNode *root)
{
    if (!root) return;
    postorderRecursive(root->left);
    postorderRecursive(root->right);
    printf("%d ", root->val);
}

void preorderIterative(TreeNode *root)
{
    if (!root) return;

    TreeNode *stack[MAXN];
    int top = 0;
    stack[top++] = root;

    while (top > 0) {
        TreeNode *node = stack[--top];
        printf("%d ", node->val);

        if (node->right) stack[top++] = node->right;
        if (node->left) stack[top++] = node->left;
    }
}

void inorderIterative(TreeNode *root)
{
    TreeNode *stack[MAXN];
    int top = 0;
    TreeNode *node = root;

    while (node || top > 0) {
        while (node) {
            stack[top++] = node;
            node = node->left;
        }

        node = stack[--top];
        printf("%d ", node->val);
        node = node->right;
    }
}

void postorderTwoStack(TreeNode *root)
{
    if (!root) return;

    TreeNode *s1[MAXN];
    TreeNode *s2[MAXN];
    int t1 = 0;
    int t2 = 0;

    s1[t1++] = root;

    while (t1 > 0) {
        TreeNode *node = s1[--t1];
        s2[t2++] = node;

        if (node->left) s1[t1++] = node->left;
        if (node->right) s1[t1++] = node->right;
    }

    while (t2 > 0)
        printf("%d ", s2[--t2]->val);
}

/* ============================================================
 * Jega 172: Level order
 * ============================================================ */

void levelOrder(TreeNode *root)
{
    if (!root) return;

    TreeNode *q[MAXN];
    int front = 0;
    int rear = 0;

    q[rear++] = root;

    while (front < rear) {
        int size = rear - front;

        for (int i = 0; i < size; i++) {
            TreeNode *node = q[front++];

            printf("%d ", node->val);

            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }

        printf("\n");
    }
}

/* ============================================================
 * Jega 174: Height
 * ============================================================ */

int heightRecursive(TreeNode *root)
{
    if (!root) return 0;

    int left = heightRecursive(root->left);
    int right = heightRecursive(root->right);

    return 1 + max2(left, right);
}

int heightIterative(TreeNode *root)
{
    if (!root) return 0;

    TreeNode *q[MAXN];
    int front = 0;
    int rear = 0;
    int height = 0;

    q[rear++] = root;

    while (front < rear) {
        int size = rear - front;
        height++;

        for (int i = 0; i < size; i++) {
            TreeNode *node = q[front++];

            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }
    }

    return height;
}

/* ============================================================
 * Jega 176: Diameter
 * Optimized O(n)
 * ============================================================ */

int diameterAnswer;

int heightForDiameter(TreeNode *root)
{
    if (!root) return 0;

    int left = heightForDiameter(root->left);
    int right = heightForDiameter(root->right);

    diameterAnswer = max2(diameterAnswer, left + right);

    return 1 + max2(left, right);
}

int diameter(TreeNode *root)
{
    diameterAnswer = 0;
    heightForDiameter(root);
    return diameterAnswer;
}

/* ============================================================
 * Jega 175: Balanced
 * Optimized O(n)
 * ============================================================ */

int heightForBalanced(TreeNode *root)
{
    if (!root) return 0;

    int left = heightForBalanced(root->left);
    if (left == -1) return -1;

    int right = heightForBalanced(root->right);
    if (right == -1) return -1;

    if (abs(left - right) > 1) return -1;

    return 1 + max2(left, right);
}

int isBalanced(TreeNode *root)
{
    return heightForBalanced(root) != -1;
}

/* ============================================================
 * Jega 181: Same tree
 * ============================================================ */

int isSameTreeRecursive(TreeNode *a, TreeNode *b)
{
    if (!a && !b) return 1;
    if (!a || !b) return 0;
    if (a->val != b->val) return 0;

    return isSameTreeRecursive(a->left, b->left) &&
           isSameTreeRecursive(a->right, b->right);
}

int isSameTreeIterative(TreeNode *a, TreeNode *b)
{
    TreeNode *s1[MAXN];
    TreeNode *s2[MAXN];
    int top = 0;

    s1[top] = a;
    s2[top++] = b;

    while (top > 0) {
        TreeNode *left = s1[--top];
        TreeNode *right = s2[top];

        if (!left && !right)
            continue;

        if (!left || !right)
            return 0;

        if (left->val != right->val)
            return 0;

        s1[top] = left->left;
        s2[top++] = right->left;

        s1[top] = left->right;
        s2[top++] = right->right;
    }

    return 1;
}

/* ============================================================
 * Jega 185: Symmetric
 * ============================================================ */

int mirror(TreeNode *left, TreeNode *right)
{
    if (!left && !right) return 1;
    if (!left || !right) return 0;
    if (left->val != right->val) return 0;

    return mirror(left->left, right->right) &&
           mirror(left->right, right->left);
}

int isSymmetric(TreeNode *root)
{
    if (!root) return 1;
    return mirror(root->left, root->right);
}

/* ============================================================
 * Jega 182/185: Zigzag / Views
 * ============================================================ */

void zigzag(TreeNode *root)
{
    if (!root) return;

    TreeNode *q[MAXN];
    int front = 0;
    int rear = 0;
    int leftToRight = 1;

    q[rear++] = root;

    while (front < rear) {
        int size = rear - front;
        int level[MAXN];

        for (int i = 0; i < size; i++) {
            TreeNode *node = q[front++];
            int index = leftToRight ? i : size - 1 - i;

            level[index] = node->val;

            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }

        for (int i = 0; i < size; i++)
            printf("%d ", level[i]);

        printf("\n");

        leftToRight = !leftToRight;
    }
}

void leftView(TreeNode *root)
{
    if (!root) return;

    TreeNode *q[MAXN];
    int front = 0;
    int rear = 0;

    q[rear++] = root;

    while (front < rear) {
        int size = rear - front;

        for (int i = 0; i < size; i++) {
            TreeNode *node = q[front++];

            if (i == 0)
                printf("%d ", node->val);

            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }
    }
}

void rightView(TreeNode *root)
{
    if (!root) return;

    TreeNode *q[MAXN];
    int front = 0;
    int rear = 0;

    q[rear++] = root;

    while (front < rear) {
        int size = rear - front;

        for (int i = 0; i < size; i++) {
            TreeNode *node = q[front++];

            if (i == size - 1)
                printf("%d ", node->val);

            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }
    }
}

/* ============================================================
 * Jega 184: Top / Bottom / Vertical View
 * ============================================================ */

typedef struct QItem {
    TreeNode *node;
    int hd;
} QItem;

void topView(TreeNode *root)
{
    if (!root) return;

    int seen[2 * MAXN + 1] = {0};
    int value[2 * MAXN + 1] = {0};
    int min = 0;
    int max = 0;

    QItem q[MAXN];
    int front = 0;
    int rear = 0;

    q[rear++] = (QItem){root, 0};

    while (front < rear) {
        QItem item = q[front++];
        int index = item.hd + MAXN;

        if (!seen[index]) {
            seen[index] = 1;
            value[index] = item.node->val;
        }

        if (item.hd < min) min = item.hd;
        if (item.hd > max) max = item.hd;

        if (item.node->left) q[rear++] = (QItem){item.node->left, item.hd - 1};
        if (item.node->right) q[rear++] = (QItem){item.node->right, item.hd + 1};
    }

    for (int hd = min; hd <= max; hd++)
        printf("%d ", value[hd + MAXN]);
}

void bottomView(TreeNode *root)
{
    if (!root) return;

    int value[2 * MAXN + 1] = {0};
    int min = 0;
    int max = 0;

    QItem q[MAXN];
    int front = 0;
    int rear = 0;

    q[rear++] = (QItem){root, 0};

    while (front < rear) {
        QItem item = q[front++];

        value[item.hd + MAXN] = item.node->val;

        if (item.hd < min) min = item.hd;
        if (item.hd > max) max = item.hd;

        if (item.node->left) q[rear++] = (QItem){item.node->left, item.hd - 1};
        if (item.node->right) q[rear++] = (QItem){item.node->right, item.hd + 1};
    }

    for (int hd = min; hd <= max; hd++)
        printf("%d ", value[hd + MAXN]);
}

/* ============================================================
 * Jega 183: Boundary
 * ============================================================ */

int isLeaf(TreeNode *root)
{
    return root && !root->left && !root->right;
}

void printLeaves(TreeNode *root)
{
    if (!root) return;

    if (isLeaf(root)) {
        printf("%d ", root->val);
        return;
    }

    printLeaves(root->left);
    printLeaves(root->right);
}

void boundaryTraversal(TreeNode *root)
{
    if (!root) return;

    if (!isLeaf(root))
        printf("%d ", root->val);

    TreeNode *node = root->left;

    while (node) {
        if (!isLeaf(node))
            printf("%d ", node->val);

        node = node->left ? node->left : node->right;
    }

    printLeaves(root);

    int stack[MAXN];
    int top = 0;

    node = root->right;

    while (node) {
        if (!isLeaf(node))
            stack[top++] = node->val;

        node = node->right ? node->right : node->left;
    }

    while (top > 0)
        printf("%d ", stack[--top]);
}

/* ============================================================
 * Jega 186: Path problems
 * ============================================================ */

void printRootToLeafPaths(TreeNode *root, int path[], int len)
{
    if (!root) return;

    path[len++] = root->val;

    if (!root->left && !root->right) {
        for (int i = 0; i < len; i++)
            printf("%d ", path[i]);
        printf("\n");
        return;
    }

    printRootToLeafPaths(root->left, path, len);
    printRootToLeafPaths(root->right, path, len);
}

int hasPathSum(TreeNode *root, int target)
{
    if (!root) return 0;

    if (!root->left && !root->right)
        return root->val == target;

    return hasPathSum(root->left, target - root->val) ||
           hasPathSum(root->right, target - root->val);
}

/* ============================================================
 * Jega 193: LCA
 * ============================================================ */

TreeNode *lca(TreeNode *root, TreeNode *p, TreeNode *q)
{
    if (!root) return NULL;

    if (root == p || root == q)
        return root;

    TreeNode *left = lca(root->left, p, q);
    TreeNode *right = lca(root->right, p, q);

    if (left && right)
        return root;

    return left ? left : right;
}

/* ============================================================
 * Jega 194: Children Sum
 * ============================================================ */

void changeTreeChildrenSum(TreeNode *root)
{
    if (!root) return;

    int childSum = 0;

    if (root->left) childSum += root->left->val;
    if (root->right) childSum += root->right->val;

    if (childSum >= root->val) {
        root->val = childSum;
    } else {
        if (root->left) root->left->val = root->val;
        if (root->right) root->right->val = root->val;
    }

    changeTreeChildrenSum(root->left);
    changeTreeChildrenSum(root->right);

    int total = 0;

    if (root->left) total += root->left->val;
    if (root->right) total += root->right->val;

    if (root->left || root->right)
        root->val = total;
}

/* ============================================================
 * Jega 196/197: Complete tree count
 * ============================================================ */

int leftHeight(TreeNode *root)
{
    int h = 0;
    while (root) {
        h++;
        root = root->left;
    }
    return h;
}

int rightHeight(TreeNode *root)
{
    int h = 0;
    while (root) {
        h++;
        root = root->right;
    }
    return h;
}

int countCompleteNodes(TreeNode *root)
{
    if (!root) return 0;

    int left = leftHeight(root);
    int right = rightHeight(root);

    if (left == right)
        return (1 << left) - 1;

    return 1 + countCompleteNodes(root->left) +
               countCompleteNodes(root->right);
}

/* ============================================================
 * Jega 198/199/200: Build tree
 * ============================================================ */

TreeNode *newNode(int val)
{
    TreeNode *node = malloc(sizeof(TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int findIndex(int arr[], int left, int right, int val)
{
    for (int i = left; i <= right; i++) {
        if (arr[i] == val)
            return i;
    }
    return -1;
}

TreeNode *buildPreIn(int preorder[],
                     int inorder[],
                     int left,
                     int right,
                     int *index)
{
    if (left > right) return NULL;

    int rootVal = preorder[*index];
    (*index)++;

    TreeNode *root = newNode(rootVal);
    int mid = findIndex(inorder, left, right, rootVal);

    root->left = buildPreIn(preorder, inorder, left, mid - 1, index);
    root->right = buildPreIn(preorder, inorder, mid + 1, right, index);

    return root;
}

/* ============================================================
 * Jega 203: Serialize
 * ============================================================ */

void serializePrint(TreeNode *root)
{
    if (!root) {
        printf("# ");
        return;
    }

    printf("%d ", root->val);

    serializePrint(root->left);
    serializePrint(root->right);
}

/* ============================================================
 * Jega 204/205: Morris
 * ============================================================ */

void morrisInorder(TreeNode *root)
{
    TreeNode *node = root;

    while (node) {
        if (!node->left) {
            printf("%d ", node->val);
            node = node->right;
        } else {
            TreeNode *prev = node->left;

            while (prev->right && prev->right != node)
                prev = prev->right;

            if (!prev->right) {
                prev->right = node;
                node = node->left;
            } else {
                prev->right = NULL;
                printf("%d ", node->val);
                node = node->right;
            }
        }
    }
}

/* ============================================================
 * Jega 206: Invert / Flatten
 * ============================================================ */

TreeNode *invertTree(TreeNode *root)
{
    if (!root) return NULL;

    TreeNode *left = invertTree(root->left);
    TreeNode *right = invertTree(root->right);

    root->left = right;
    root->right = left;

    return root;
}

TreeNode *flattenPrev;

void flattenDfs(TreeNode *root)
{
    if (!root) return;

    flattenDfs(root->right);
    flattenDfs(root->left);

    root->right = flattenPrev;
    root->left = NULL;

    flattenPrev = root;
}

void flatten(TreeNode *root)
{
    flattenPrev = NULL;
    flattenDfs(root);
}

/* ============================================================
 * Jega 207-215: BST Master
 * ============================================================ */

TreeNode *searchBST(TreeNode *root, int val)
{
    while (root) {
        if (root->val == val)
            return root;
        root = val < root->val ? root->left : root->right;
    }

    return NULL;
}

int floorBST(TreeNode *root, int key)
{
    int ans = INT_MIN;

    while (root) {
        if (root->val == key)
            return root->val;

        if (root->val < key) {
            ans = root->val;
            root = root->right;
        } else {
            root = root->left;
        }
    }

    return ans;
}

int ceilBST(TreeNode *root, int key)
{
    int ans = INT_MAX;

    while (root) {
        if (root->val == key)
            return root->val;

        if (root->val > key) {
            ans = root->val;
            root = root->left;
        } else {
            root = root->right;
        }
    }

    return ans;
}

int validateBST(TreeNode *root, long minVal, long maxVal)
{
    if (!root) return 1;

    if (root->val <= minVal || root->val >= maxVal)
        return 0;

    return validateBST(root->left, minVal, root->val) &&
           validateBST(root->right, root->val, maxVal);
}

int isValidBST(TreeNode *root)
{
    return validateBST(root, LONG_MIN, LONG_MAX);
}

TreeNode *lcaBST(TreeNode *root, TreeNode *p, TreeNode *q)
{
    while (root) {
        if (p->val < root->val && q->val < root->val)
            root = root->left;
        else if (p->val > root->val && q->val > root->val)
            root = root->right;
        else
            return root;
    }

    return NULL;
}

/* ============================================================
 * TA 266/267: Ternary DFS
 * ============================================================ */

void ternaryDfsRecursive(TernaryNode *root)
{
    if (!root) return;

    printf("%d ", root->val);

    ternaryDfsRecursive(root->left);
    ternaryDfsRecursive(root->middle);
    ternaryDfsRecursive(root->right);
}
