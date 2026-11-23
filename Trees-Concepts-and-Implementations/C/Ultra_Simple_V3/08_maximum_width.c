/* MAXIMUM WIDTH
BFS with conceptual array positions.
width = last_index - first_index + 1.
This compact C version uses a fixed demonstration queue.
*/
#include <stddef.h>
typedef struct Node { int data; struct Node *left,*right; } Node;
typedef struct { Node *node; unsigned long long pos; } Item;

unsigned long long maximumWidth(Node *root){
    if(!root) return 0;
    Item q[10000];
    int front=0,rear=0;
    q[rear++]=(Item){root,0};
    unsigned long long best=0;

    while(front<rear){
        int count=rear-front;
        unsigned long long base=q[front].pos, first=0,last=0;
        for(int i=0;i<count;i++){
            Item x=q[front++];
            unsigned long long p=x.pos-base;
            if(i==0) first=p;
            if(i==count-1) last=p;
            if(x.node->left) q[rear++]=(Item){x.node->left,2*p+1};
            if(x.node->right) q[rear++]=(Item){x.node->right,2*p+2};
        }
        unsigned long long width=last-first+1;
        if(width>best) best=width;
    }
    return best;
}
