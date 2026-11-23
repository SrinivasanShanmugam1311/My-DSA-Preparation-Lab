/* MORRIS INORDER
Temporary thread from predecessor back to current.
No recursion. No explicit stack. Extra space O(1).
*/
#include <stdio.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

void morris(Node *root){
    Node *cur=root;
    while(cur){
        if(!cur->left){
            printf("%d ",cur->data);
            cur=cur->right;
        } else {
            Node *pred=cur->left;
            while(pred->right && pred->right!=cur) pred=pred->right;
            if(!pred->right){
                pred->right=cur;
                cur=cur->left;
            } else {
                pred->right=NULL;
                printf("%d ",cur->data);
                cur=cur->right;
            }
        }
    }
}
