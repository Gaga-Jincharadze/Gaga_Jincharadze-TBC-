
#Task 1

V = str(input("Enter True or False: "))

if V == "True":
    print("Whoala")
elif V == "False":
    print("You Entered False.")
else:
    print("Enter 'True' or 'False'.")



# #Task 2

a = float(input("Enter Your Number: "))
b = float(input("Enter Your Number: "))

if b % a == 0:
    print("jeradia")
else:
    print("ar aris jeradi")


#Task 3

A = int(input("Enter Your Number: "))

if A == 1:
    print("1")

if A == 2:
    print("1, 2")

if A == 3:
    print("1, 3")

if A == 4:
    print("1, 2")

if A == 5:
    print("1, 5")

if A == 6:
    print("1, 2, 3")

if A == 7:
    print("1, 7")

if A == 8:
    print("1, 2")

if A == 9:
    print("1, 3")

if A == 10:
    print("1, 2, 5")

else:
    print("You Must Enter Number From 1 To 10: ")


#Task 4

S = float(input("Enter Your Current Speed: "))

if S < 0:
    print("How :D")

elif S < 30:
    print("SLOW")
elif S >= 30 and S <= 60:
    print("MODERATE")
elif S > 60 and S <= 120:
    print("FAST")
else:
    print("VERY FAST")