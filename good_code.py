def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an operation(1-4): ")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(first_number, second_number))
elif choice == "2":
    print("Result:", subtract(first_number, second_number))
elif choice == "3":
    print("Result:", multiply(first_number, second_number))
elif choice == "4":
    print("Result:", divide(first_number, second_number))
else:
    print("Invalid choice")