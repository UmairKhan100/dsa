class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, item):
        if self.top < self.size - 1:
            self.stack.append(item)
            self.top += 1
            print(f'item {item} is pushed into the stack')
        else:
            print('stack overflow')

    def pop(self):
        if self.is_empty():
            print('stack underflow')
        else:
            item = self.stack[self.top]
            self.top -= 1
            print(f'item {item} is popped from the stack')
            return item

    def peek(self):
        if self.is_empty():
            print('stack underflow')
        else:
            return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print('stack underflow')
        else:
            print(f'stack content: {self.stack[:self.top + 1]}')

    def is_empty(self):
        return self.top < 0

if __name__ == '__main__':
    s = Stack(3)
    s.pop()
    s.push(33)
    s.push(22)
    print(f'top item: {s.peek()}')
    s.push(11)
    s.push(55)
    s.pop()
    s.display()
    s.pop()
    s.pop()
    s.pop()