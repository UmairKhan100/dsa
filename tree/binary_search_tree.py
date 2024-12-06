class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree():
    def __init__(self):
        self.root: Node = None

    def insert(self, data):
        self.root = self.insert_rec(self.root, data)

    def insert_rec(self, root: Node, data):
        if root == None:
            new_node = Node(data)
            root = new_node
        elif data < root.data:
            root.left = self.insert_rec(root.left, data)
        else:
            root.right = self.insert_rec(root.right, data)
        return root

    def display(self, root: Node):
        if root != None:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)

    def find(self, data):
        current = self.root
        while current != None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
        pass

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    bst.display(bst.root)
    print()
    print(bst.find(4))
    bst.delete(5)
    bst.display(bst.root)
