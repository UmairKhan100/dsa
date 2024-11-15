class CircularQueue():
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.is_full():
            print('queue is full')
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f'{data} enqueued to queue')

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print(f'{data} dequeued from queue')
            return data

    def peek(self):
        if self.is_empty():
            print('queue is empty')
        else:
            return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print('queue is empty')
        else:
            i = self.front
            print(f'queue content:', end=' ')
            while True:
                print(self.queue[i], end=' ')
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

    def is_empty(self):
        return self.front == -1
        
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
        
if __name__ == '__main__':
    cq = CircularQueue(3)
    cq.dequeue()
    cq.enqueue(33)
    cq.enqueue(22)
    print(f'front data: {cq.peek()}')
    cq.enqueue(11)
    cq.enqueue(55)
    cq.dequeue()
    cq.display()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()