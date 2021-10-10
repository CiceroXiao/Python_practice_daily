import sys


def generate_Fibonacci(n):
    n = int(n)
    first, second = 0, 1
    thrid = first + second
    fibonacci = []
    fibonacci.append(first)

    if n == 0 or str(n).isdecimal() is False:
        print("Please enter positive integers.")
        sys.exit()
    elif n == 1:
        return fibonacci
    else:
        fibonacci.append(second)
        for _ in range(2, n):
            fibonacci.append(thrid)
            first, second = second, thrid
            thrid = first + second
    return fibonacci


while True:
    try:
        print("Enter the Nth Fibonacci number you wish to\n"
              "calculate (such as 5, 50, 1000, 9999), or QUIT to quit:")

        user_enter = input("> ")
        if user_enter.upper() == "QUIT":
            sys.exit()
        result = generate_Fibonacci(user_enter)
        print(result)
        print()
    except KeyboardInterrupt:
        sys.exit()
