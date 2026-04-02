# python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter a 1st number: "))
num2 = float(input("Enter a 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        exit()
    result = num1 / num2
else:
    print(f"{operator} is not a valid operator")
    exit()

print(round(result, 3))