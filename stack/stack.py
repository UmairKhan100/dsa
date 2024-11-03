class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, data):
        if self.top < self.size - 1:
            self.stack.append(data)
            self.top += 1
            print(f'{data} pushed to stack')
        else:
            print('stack overflow')

    def pop(self):
        if self.is_empty():
            print('stack underflow')
        else:
            data = self.stack[self.top]
            self.top -= 1
            print(f'{data} popped from stack')
            return data

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
    print(f'top data: {s.peek()}')
    s.push(11)
    s.push(55)
    s.pop()
    s.display()
    s.pop()
    s.pop()
    s.pop()