# Inorder-Preorder-Postorder-Tree-Traversals

#include <stdio.h>
#include <stdlib.h>
#include<queue>
typedef struct node {
  int value;
  struct node* left;
  struct node* right;
}node;
// Inorder traversal
void InOrder(struct node* root) {
  if (root == NULL) return;
  InOrder(root->left);
  printf("%d ", root->value);
  InOrder(root->right);
}
// PreOrder traversal
void PreOrder(struct node* root) {
  if (root == NULL) return;
  printf("%d ", root->value);
  PreOrder(root->left);
  PreOrder(root->right);
}
// PostOrder traversal
void PostOrder(struct node* root) {
  if (root == NULL) return;
  PostOrder(root->left);
  PostOrder(root->right);
  printf("%d ", root->value);
}

}
// Create a new Node
struct node* createNode(int value) {
  struct node* newNode = new node();
  newNode->value = value;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}
int main() {
  struct node* root = createNode(1);
  root->left = createNode(2);
  root->right = createNode(3);
  root->left->left = createNode(4);
  root->left->right = createNode(5);
  root->right->left = createNode(6);
  root->right->right = createNode(7);
  printf("Level Order traversal:\t");
  LevelOrder(root);
  printf("\nInorder traversal:\t");
  InOrder(root);
  printf("\nPreOrder traversal:\t");
  PreOrder(root);
  printf("\nPostOrder traversal:\t");
  PostOrder(root);
}
  
  
  by python
  
  class Node:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x

def Inorder(root):

	if root:

		
		Inorder(root.left)

		
		print(root.val),

		
		Inorder(root.right)



def Postorder(root):

	if root:

		
		Postorder(root.left)

		
		Postorder(root.right)

		
		print(root.val),



def Preorder(root):

	if root:

		print(root.val),

		
		Preorder(root.left)

		
		Preorder(root.right)



root = Node(12)
root.left = Node(13)
root.right = Node(14)
root.left.left = Node(15)
root.left.right = Node(16)
print ("\nPreorder traversal")
Preorder(root)
print ("\nInorder traversal")
Inorder(root)
print ("\nPostorder traversal")
Postorder(root)
