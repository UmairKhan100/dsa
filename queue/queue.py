class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = 0
        self.rear = -1
    
    def enqueue(self, data):
        if self.rear == self.size - 1:
            print('queue is full')
        else:
            self.rear += 1
            self.queue.append(data)
            print(f'{data} enqueued to queue')

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data = self.queue.pop(self.front)
            self.rear -= 1
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
            print(f'queue content: {self.queue}')

    def is_empty(self):
        return self.rear == -1
        
if __name__ == '__main__':
    q = Queue(3)
    q.dequeue()
    q.enqueue(33)
    q.enqueue(22)
    print(f'front data: {q.peek()}')
    q.enqueue(11)
    q.enqueue(55)
    q.dequeue()
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()