def convert_temperature(value, type):
    if type == "C":
        return value * 9/5 + 32
    elif type == "F":
        return (value - 32) * 5/9

def main():

    print("Converting Celsius to Fahrenheit:")
    print("25 ->", convert_temperature(25, "C"))
    print("0 ->", convert_temperature(0, "C"))
    print("-10 ->", convert_temperature(-10, "C"))
    
    print()
    
    print("Converting Fahrenheit to Celsius:")
    print("77 ->", convert_temperature(77, "F"))
    print("32 ->", convert_temperature(32, "F"))
    print("100 ->", convert_temperature(100, "F"))

main()