/* FLATTEN BINARY TREE
Reverse preorder: RIGHT -> LEFT -> ROOT.
Keep previous node.
current.right = previous
current.left = NULL
*/
#include <stddef.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

void flattenHelper(Node *root,Node **previous){
    if(!root) return;

    flattenHelper(root->right,previous);
    flattenHelper(root->left,previous);

    root->right=*previous;
    root->left=NULL;
    *previous=root;
}
void flatten(Node *root){
    Node *previous=NULL;
    flattenHelper(root,&previous);
}
