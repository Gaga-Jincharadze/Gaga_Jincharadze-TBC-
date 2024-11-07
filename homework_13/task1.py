import random
numbers = []
for i in range(100):
    numbers.append(random.randint(1, 1000000000))


digit_lengths = list(map(lambda x: len(str(x)), numbers))


shortest_index = digit_lengths.index(min(digit_lengths))
longest_index = digit_lengths.index(max(digit_lengths))


shortest = numbers[shortest_index]
longest = numbers[longest_index]
sortedlist = sorted(numbers)

print("Generated Numbers:", numbers)
print("Shortest Number:", shortest)
print("Longest Number:", longest)
print("Sorted List:", sortedlist)