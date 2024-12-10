class List(list):
    def __init__(self, elements):
        super().__init__(elements)

    def min(self):
        return min(self)

    def max(self):
        return max(self)

list = List([10, 20, 30, 5, 25])
print(f"List: {list}")
print(f"Min: {list.min()}")
print(f"Max: {list.max()}")







