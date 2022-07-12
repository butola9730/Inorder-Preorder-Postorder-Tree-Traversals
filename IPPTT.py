class Node:
    def __init__(self, item):
        self.lef = None
        self.rig = None
        self.val = item


def inorder_traverse(root):

    if root:

        inorder_traverse(root.lef)

        print(str(root.val) + "->", end='')

        inorder_traverse(root.rig)


def postorder_traverse(root):

    if root:

        postorder_traverse(root.lef)

        postorder_traverse(root.rig)

        print(str(root.val) + "->", end='')


def preorder_traverse(root):

    if root:

        print(str(root.val) + "->", end='')

        preorder_traverse(root.lef)

        preorder_traverse(root.rig)


root = Node(1)
root.lef = Node(2)
root.rig = Node(3)
root.lef.lef = Node(4)
root.lef.rig = Node(5)

print("Inorder traversal ")
inorder_traverse(root)

print("\nPreorder traversal ")
preorder_traverse(root)

print("\nPostorder traversal ")
postorder_traverse(root)



