friendships = {}

while True:
    line = input("Enter info about friendship:")

    if line.upper() == "FINISH":
        break

    if " - " in line:
        person1, person2 = line.split(" - ")

        if person1 not in friendships:
            friendships[person1] = set()
        friendships[person1].add(person2)

        if person2 not in friendships:
            friendships[person2] = set()
        friendships[person2].add(person1)

if friendships:
    for person in sorted(friendships.keys()):
        friends_list = ", ".join(sorted(friendships[person]))
        print(f"{person} – {friends_list}")
else:
    print("No friendships.")