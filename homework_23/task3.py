class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("Incorrect score")

    def get_average(self):
        if self._scores:
            return sum(self._scores) / len(self._scores)
        return 0

    def get_scores(self):
        return self._scores

    def get_name(self):
        return self._name

students = [
    Student("Gaga"),
    Student("Tiko"),
    Student("Mixeili")
]


students[0].add_score(87)
students[0].add_score(99)

students[1].add_score(65)
students[1].add_score(69)

students[2].add_score(90)


for student in students:
    print(f"{student.get_name()}'s average score: {student.get_average()}")

new_student = Student("Gela")
new_student.add_score(100)
new_student.add_score(105) # prints "incorrect score"
new_student.add_score(85)

print(f"{new_student.get_name()}'s scores: {new_student.get_scores()}")
print(f"{new_student.get_name()}'s average score: {new_student.get_average()}")
