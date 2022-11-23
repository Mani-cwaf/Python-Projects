def Calculate(a, b):
    return a - ((a / 100) * b)

while True:
    num1 = float(input("Enter Price: "))
    num2 = float(input("Enter Discount (in percentage): "))
    choice = str(input("Start(yes): "))
    exit = False

    if choice == "yes":
        print(Calculate(num1, num2))
    else:
        print("Invalid Operation")
    exit = str(input("Exit Calculator(true/any): "))
    if exit == "true":
        break
    else:
        continue