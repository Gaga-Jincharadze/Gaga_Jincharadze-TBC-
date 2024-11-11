# 3. (12 ქულა) Დაწერეთ თამაში rock, paper, scissor. 
# Დაწერეთ ფუნქცია რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S. 
# Დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S. 
# სიმარტივისთვის შეგიძლიათ უგულებელყოთ ყველა შემოწმება მომხმარებლის ინფუთზე. 
# Შეადარეთ ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო და 
# გამოავლინეთ გამარჯვებული. Წესები: R ამარცხებს S S ამარცხებს P P ამარცხებს R P P, R R, S S არის ფრე იმ შემთხვევაში თუ გვაქვს ფრე,
# უნდა მისცეთ კიდევ ერთი თამაშის საშუალება.

import random

def game():
    game = ["R","P","s"]
    program_choice =  random.choice(game)
    return program_choice

def main():
    player_choice = input("type ""R"", ""P"", or ""S"": ")
    return player_choice

random_choice = game()
my_choice = main()

print("program_choice:", random_choice)
print("Player choice:", my_choice)

if random_choice == my_choice:
    print("draw")
elif random_choice == "R" and my_choice == "S":
    print("You are loser")
elif random_choice == "S" and my_choice == "P":
    print("you are loser")
elif random_choice == "P" and my_choice == "R":
    print("you are loser")
else:
    print("you are winner")





    