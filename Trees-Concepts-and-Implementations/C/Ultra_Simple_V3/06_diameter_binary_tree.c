/* DIAMETER
Each node receives left/right heights.
Candidate diameter = left height + right height.
Return height upward.
*/
typedef struct Node { int data; struct Node *left,*right; } Node;

int max(int a,int b){return a>b?a:b;}

int height(Node *root,int *diameter){
    if(!root) return 0;
    int l=height(root->left,diameter);
    int r=height(root->right,diameter);
    if(l+r>*diameter) *diameter=l+r;
    return 1+max(l,r);
}
int treeDiameter(Node *root){
    int d=0; height(root,&d); return d;
}
