a = 1
while a <= 9:
    b = 1
    while b <= a:
        product = a*b
        print(f"{a} * {b} = {product}", end="\t")
        b += 1
    a += 1
    print()