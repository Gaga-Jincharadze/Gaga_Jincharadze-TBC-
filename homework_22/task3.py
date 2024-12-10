class Stack:
    def __init__(self):
        self.list = []

    def push(self,element):
        return self.list.append(element)
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list)
    
    def is_empty(self):
        return len(self.list) == 0 # or len(self.list) > 0

    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())    # Output: 30
print(stack.pop())     # Output: 30
print(stack.is_empty())  # Output: False
print(stack.size())    # Output: 2