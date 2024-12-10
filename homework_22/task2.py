class Queue:
    def __init__(self):
        self.list = []

    def insert(self,element):
        return self.list.append(element)
    
    def pop(self):
        return self.list.pop(0)
    
list = Queue()
list.insert(4)
list.insert(2)
list.insert(3)
print(list.pop())