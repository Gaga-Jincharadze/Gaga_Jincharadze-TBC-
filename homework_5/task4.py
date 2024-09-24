n = int(input("Enter Number: "))

level = 0

# after that result will be that "*" on the top of tree

while level == 0:
    print(" " * n + "*") 
    level += 1

# this will add each layer

while level <= n - 1:
    spaces = n - level
    slashes = "/" * level + "|" + "\\" * level
    print(" " * spaces + slashes)
    level += 1
    
print(" " * n + "|")

