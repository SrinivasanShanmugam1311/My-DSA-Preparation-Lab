/* BST FROM PREORDER
Use upper bound.
Next value greater than bound -> it belongs to another subtree.
Time O(n).
*/
#include <stdlib.h>
#include <limits.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

Node *newNode(int x){ Node*n=malloc(sizeof(Node));n->data=x;n->left=n->right=NULL;return n; }

Node *build(int pre[],int n,int *i,int bound){
    if(*i==n || pre[*i] > bound) return NULL;
    int value=pre[(*i)++];
    Node *root=newNode(value);
    root->left=build(pre,n,i,value);
    root->right=build(pre,n,i,bound);
    return root;
}
Node *bstFromPreorder(int pre[],int n){
    int i=0;
    return build(pre,n,&i,INT_MAX);
}
