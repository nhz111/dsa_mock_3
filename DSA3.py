#implement a stack using a list in python. 
#include the necessary methods such as push, pop and is Empty.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0
 
#example for implementation:

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())          # Output: 3

print(stack.pop())          # Output: 2

print(stack.is_empty())     # Output: False

print(stack.pop())          # Output: 1

print(stack.is_empty())     # Output: True

print(stack.pop())          # Output: Stack is empty. None
        

#question:2

#implement  queue using a list in python. 
#include the necessary method such as enque, dequeue and is empty

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0
        
# example for implimentation    
 
 queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1

print(queue.dequeue())  # Output: 2

print(queue.is_empty())  # Output: False

print(queue.dequeue())  # Output: 3

print(queue.is_empty())  # Output: True

print(queue.dequeue())  # Output: Queue is empty. None

