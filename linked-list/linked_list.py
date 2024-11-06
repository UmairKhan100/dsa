class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

class LinkedList:
    def __init__(self):
        self.head: Node = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f'{data} added to the list')

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
            print(f'{data} deleted from the list')
            return True

        while node and node.next:
            if node.next.data == data:
                node.next = node.next.next
                print(f'{data} deleted from the list')
                return True
            node = node.next

        print('data not found')
        return False

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print("None")

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.display()

    x = 20
    index = ll.search(x)
    if index == -1:
        print(f'data not found')
    else:
        print(f'data {x} found at position {index}')

    ll.delete(x)
    ll.display()