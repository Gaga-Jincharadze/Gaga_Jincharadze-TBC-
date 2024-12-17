class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 40)


print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
print(type(person1.get_info()))
