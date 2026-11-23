/* MERGE TWO BSTs
Inorder of BST = sorted.
Store both inorder arrays, then merge them.
Time O(n+m).
*/
#include <stdio.h>
#include <stdlib.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

void inorder(Node *r,int *a,int *k){
    if(!r) return;
    inorder(r->left,a,k); a[(*k)++]=r->data; inorder(r->right,a,k);
}
void merge(int *a,int n,int *b,int m){
    int i=0,j=0;
    while(i<n && j<m) {
        if(a[i]<=b[j]) printf("%d ",a[i++]);
        else printf("%d ",b[j++]);
    }
    while(i<n) printf("%d ",a[i++]);
    while(j<m) printf("%d ",b[j++]);
}
