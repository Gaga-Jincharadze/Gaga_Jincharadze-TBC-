import random

list1 = [random.randint(1, 1000) for _ in range(10)]
list2 = [random.randint(1, 1000) for _ in range(10)]
list3 = [random.randint(1, 1000) for _ in range(10)]

result = list(map(lambda x, y, z: x + y + z , list1, list2, list3))

print("Sum Of x&y&z:", result)