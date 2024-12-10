class Inset:
    def __init__(self):
        self.list = []
    
    def insert(self,element):
        if element not in self.list:
            self.list.append(element)

    def member(self,element):
        return element in self.list
    
    def remove(self,element):
        if element in self.list:
            self.list.remove(element)
        else:
            raise "ვერ ვიპოვნე"
        
    def __str__(self):
        return str(sorted(self.list))

inset = Inset()
inset.insert(10)
inset.insert(20)
inset.insert(10)  # ar daemateba
print(inset)  
print(inset.member(10))  # True
print(inset.member(30))  # False