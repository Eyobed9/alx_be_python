num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = 0
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = -1
        else:
            result = num1 / num2
    case _:
        result = 0
        
if result == 0:
    print("Invalid operation.")
elif result == -1:
    print("Cannot divide by zero.")
else:
    print(f"The result is {result}.")