# 2.  Write a program to do the following operations. 
# a.  Create a Binary Search Tree by collecting information from users. 
# b.  Traverse the created trees using  
# i.  Level order 
# c.  Search Element in Binary Search Tree 


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree: 
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_help(self.root,data)

    def insert_help(self, root, data):
        if data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert_help(root.right, data)
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.insert_help(root.left, data)


    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current_root = queue.pop(0)
            print(current_root.data, end=' ')
            if current_root.left:
                queue.append(current_root.left)
            if current_root.right:
                queue.append(current_root.right)

    def search(self, data):
        current_root = self.root
        while current_root:
            if data == current_root.data:
                return True
            elif data < current_root.data:
                current_root = current_root.left
            else:
                current_root = current_root.right
        return False

    
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    n = int(input("Enter the number of roots: "))
    for _ in range(n):
        data = int(input("Enter root value: "))
        bst.insert(data)

    print("Level order traversal:")
    bst.level_order_traversal()

    search_value = int(input("\nEnter value to search: "))
    result = bst.search(search_value)
    if result:
        print(f"Value {search_value} found in the tree.")
    else:
        print(f"Value {search_value} not found in the tree.")

    
