# Program to sum up two numbers

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    #num1 = float(input("Enter first number: "))
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    num2 = float(input("Enter second number: "))
    result = sum_two_numbers(num1, num2)
    print("The sum is:", result)