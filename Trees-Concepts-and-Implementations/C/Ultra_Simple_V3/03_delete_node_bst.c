/* DELETE BST NODE
Search target.
0 child -> NULL
1 child -> return child
2 children -> copy inorder successor and delete successor.
*/
#include <stdlib.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

Node *minimum(Node *r){ while(r && r->left) r=r->left; return r; }

Node *deleteNode(Node *root,int key){
    if(!root) return NULL;
    if(key < root->data) root->left=deleteNode(root->left,key);
    else if(key > root->data) root->right=deleteNode(root->right,key);
    else {
        if(!root->left){ Node *t=root->right; free(root); return t; }
        if(!root->right){ Node *t=root->left; free(root); return t; }
        Node *s=minimum(root->right);
        root->data=s->data;
        root->right=deleteNode(root->right,s->data);
    }
    return root;
}
