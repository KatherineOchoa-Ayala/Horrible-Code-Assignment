def calculator(operation):

    if operation == '+':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        return num1 + num2

    elif operation == '-':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        return num1 - num2

    elif operation == '*':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        return num1 * num2

    elif operation == '/':
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        quotient = 0
        while num1 >= num2:
            num1 -= num2
            quotient += 1
        return quotient

    elif operation == "*":
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = 0
        for i in range(num2):
            result += num1
        return result