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