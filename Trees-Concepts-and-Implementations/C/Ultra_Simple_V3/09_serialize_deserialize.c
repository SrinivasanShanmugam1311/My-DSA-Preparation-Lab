/* SERIALIZE / DESERIALIZE
Preorder + # NULL markers preserves exact tree shape.
This study version demonstrates serialization.
*/
#include <stdio.h>
typedef struct Node { int data; struct Node *left,*right; } Node;

void serialize(Node *root,FILE *out){
    if(!root){
        fprintf(out,"# ");
        return;
    }
    fprintf(out,"%d ",root->data);
    serialize(root->left,out);
    serialize(root->right,out);
}

/* Deserialization mental model:
Read one token.
# -> NULL.
number -> create node, then recursively build LEFT and RIGHT.
*/
