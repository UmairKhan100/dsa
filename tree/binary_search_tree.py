class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree():
    def __init__(self):
        self.root: Node = None

if __name__ == '__main__':
    bst = BinarySearchTree()