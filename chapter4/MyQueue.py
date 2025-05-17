class MyQueue:
    def __init__(self):
        self.que = []

    def enqueue(self, value):
        self.que.append(value)

    def dequeue(self):
        return self.que.pop(0)
    
    def __str__(self):
        return str(self.que)

q = MyQueue()
q.enqueue('a')
print(q)
q.enqueue('b')
print(q)
q.enqueue('c')
print(q)

val1 = q.dequeue()
print(q)
val2 = q.dequeue()
print(q)
val3 = q.dequeue()
print(q)

print(val1, val2, val3)