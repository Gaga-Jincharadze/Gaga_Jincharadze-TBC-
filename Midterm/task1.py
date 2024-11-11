# 1. (5 ქულა) Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: სახელი, გვარი, ასაკი და ქალაქი. 
# Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში: Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.


name = input("Enter Your Name: ")
last_name = input("Enter Your last Name: ")
age = input("Enter Your Age: ")
city = input("Enter City:")

print(f"Hello, {name} {last_name}.")
print(f"Age: {age}. city: {city}")