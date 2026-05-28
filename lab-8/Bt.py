class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Inorder (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Preorder (Root, Left, Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Level Order (BFS)
def level_order(root):
    if root is None:
        return
    
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = None
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nLevel Order Traversal:")
level_order(root)