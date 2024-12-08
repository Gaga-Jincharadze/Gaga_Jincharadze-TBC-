import json
import os

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = float(salary)

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average(self):
        if not self.employees:
            return 0
        return sum(emp.salary for emp in self.employees) / len(self.employees)

    def max(self):
        if not self.employees:
            return None
        return max(emp.salary for emp in self.employees)

    def min(self):
        if not self.employees:
            return None
        return min(emp.salary for emp in self.employees)

    def positions(self):
        position_counts = {}
        for emp in self.employees:
            if emp.position in position_counts:
                position_counts[emp.position] += 1
            else:
                position_counts[emp.position] = 1

        return position_counts


def load_json_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    with open(file_path, 'r') as file:
        return json.load(file)


file_path = "homework_1.json"
data = load_json_file(file_path)

if data:
    departments = []
    for dept_key, dept_data in data.items():
        employees = [Employee(emp["name"], emp["position"], emp["salary"]) for emp in dept_data["employees"]]
        department = Department(dept_data["name"], dept_data["description"], employees)
        departments.append(department)

    for dept in departments:
        print(f"\nDepartment: {dept.name}")
        print(f"Average Salary: {dept.average()}")
        print(f"Max Salary: {dept.max()}")
        print(f"Min Salary: {dept.min()}")
        print(f"Positions Count: {dept.positions()}")
