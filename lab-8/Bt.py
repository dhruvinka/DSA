# 1.  Write a program to do the following operations. 
# a.  Create a Binary Tree by collecting information from users. 
# b.  Traverse the created trees using  
# i.  preorder  
# ii.  postorder  
# iii.  inorder

class root:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = root(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = root(data)
            else:
                self._insert_recursive(root.left, data)
        else:
            if root.right is None:
                root.right = root(data)
            else:
                self._insert_recursive(root.right, data)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=' ')

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=' ')
            self.inorder_traversal(root.right)

if __name__ == "__main__":
    tree = BinaryTree()
    n = int(input("Enter the number of roots: "))
    for _ in range(n):
        data = int(input("Enter root value: "))
        tree.insert(data)

    print("Preorder Traversal:")
    tree.preorder_traversal(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)
    print("\nInorder Traversal:")
    tree.inorder_traversal(tree.root)