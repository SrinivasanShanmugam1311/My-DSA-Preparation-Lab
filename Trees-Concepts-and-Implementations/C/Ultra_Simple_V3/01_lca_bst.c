/* LCA IN BST
If both targets smaller -> LEFT.
If both larger -> RIGHT.
Otherwise current node is split point/LCA.
Time O(h).
*/
#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

Node *newNode(int x) {
    Node *n = malloc(sizeof(Node));
    n->data=x; n->left=n->right=NULL; return n;
}
Node *lca(Node *root, int p, int q) {
    if (!root) return NULL;
    if (p < root->data && q < root->data) return lca(root->left,p,q);
    if (p > root->data && q > root->data) return lca(root->right,p,q);
    return root;
}
int main(void) {
    Node *root=newNode(6);
    root->left=newNode(2); root->right=newNode(8);
    root->left->left=newNode(0); root->left->right=newNode(4);
    Node *ans=lca(root,2,4);
    if(ans) printf("LCA: %d\n",ans->data);
    return 0;
}
