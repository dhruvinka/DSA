from BstNode import Tree


class bstTree:
    def insert(self, root, data):
        if root is None:
            return Tree(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
        
    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def levelOrder(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":
    bst = bstTree()
    root = None
    arr = [64, 34, 25, 12, 22, 11, 90]
    for num in arr:
        root = bst.insert(root, num)
    
    print("Inorder Traversal:")
    bst.inorder(root)
    print("\nPreorder Traversal:")
    bst.preorder(root)
    print("\nPostorder Traversal:")
    bst.postorder(root)
    key = 22
    result = bst.search(root, key)
    if result:
        print(f"\nElement {key} found in the BST.")
    else:
        print(f"\nElement {key} not found in the BST.")

    print("\nLevel-order Traversal:")
    bst.levelOrder(root)