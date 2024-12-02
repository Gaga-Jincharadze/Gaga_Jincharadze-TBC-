import json
import os

file = 'homework_1.json'

if not os.path.exists(file):
    print(f"Error: The file '{file}' does not exist.")
else:
        with open(file, 'r') as file:
            data = json.load(file)

        average_salaries = {}

        for department_key, department_info in data.items():
            employees = department_info.get("employees", [])
            total_salary = 0
            salaries_count = 0

            for employee in employees:
                try:
                    salary = float(employee["salary"])
                    total_salary += salary
                    salaries_count += 1
                except (ValueError, TypeError):
                    print("ValueError or TypeError")

            average_salary = total_salary / salaries_count if  salaries_count > 0 else 0
            average_salaries[department_info["name"]] = average_salary

        with open("avg_salary.json", 'w') as new_file:
            json.dump(average_salaries, new_file, indent=4)

        print(json.dumps(average_salaries, indent=4))