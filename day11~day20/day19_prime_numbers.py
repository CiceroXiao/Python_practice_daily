import sys
import time


def is_prime(num):

    factors = []

    if num == 0 or num == 1:
        return False

    i = 1
    while i <= (num // 2):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
            if len(factors) > 2:
                return False
        i += 1
    return True


print("Enter a number to start searching for primes from:"
      "(Try 0 or 1000000000000 (12 zeros) or another number.)")
start_number = input("> ")


if start_number.isdecimal():
    start_number = int(start_number)
else:
    print("Please enter positive integers.")
    sys.exit()
try:
    input("Press Ctrl-C at any time to quit. Press Enter to begin...")
    while True:
        time.sleep(1)
        if is_prime(start_number):
            print(start_number, end=", ")

        start_number += 1
except KeyboardInterrupt:
    sys.exit()
