def calculator(operation):

    # single responsibility violation: one function does multiple different operations

    if operation == '+':
        # DRY code violation: user input lines are repeated multiple times
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

        # KISS violation: using a while loop for division rather than the '/' operator
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

# main for testing purposes
def main():
    print(calculator('+'))
    print(calculator('-'))
    print(calculator('*'))
    print(calculator('/'))

if __name__ == '__main__':
    main()