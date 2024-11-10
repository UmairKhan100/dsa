class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next: Node = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        print(f'{data} added at the beginning of the list')

    def append(self, data):
        new_node = Node(data)
        last = self.head

        if self.head is None:
            self.head = new_node
        else:
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last

        print(f'{data} added at the end of the list')

    def search(self, data):
        node = self.head
        count = 1
        while node:
            if node.data == data:
                return count
            node = node.next
            count += 1
        return -1

    def delete(self, data):
        if not self.head:
            print('list is empty')
            return False

        node = self.head

        if node.data == data:
            self.head = node.next
            if self.head:
                self.head.prev = None
            print(f'{data} deleted from the list')
            return True

        while node:
            if node.data == data:
                if node.next:
                    node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                print(f'{data} deleted from the list')
                return True
            node = node.next

        print('data not found')
        return False

    def display(self):
        node = self.head
        last: Node = None

        print('traversal in forward direction:', end=" ")
        while node:
            print(node.data, end=" ")
            last = node
            node = node.next
        print()

        print('traversal in backward direction:', end=" ")
        while last:
            print(last.data, end=" ")
            last = last.prev
        print()

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.prepend(10)
    dll.prepend(20)
    dll.append(30)
    dll.display()

    x = 10
    index = dll.search(x)
    if index == -1:
        print(f'data not found')
    else:
        print(f'data {x} found at position {index}')

    dll.delete(x)
    dll.display()