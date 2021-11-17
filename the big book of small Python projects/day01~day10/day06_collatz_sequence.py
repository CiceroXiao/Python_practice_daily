game_description = """
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.
"""
print(game_description)

user_enter = eval(
    input("Enter a starting integer number (greater than 0) or QUIT:\n > "))


def collatz_sequence(number):
    if number == 1:
        all_number.append(number)
        return all_number
    elif number % 2 == 0:
        all_number.append(number)
        return collatz_sequence(number // 2)
    elif number % 2 == 1:
        all_number.append(number)
        return collatz_sequence(number * 3 + 1)


try:
    all_number = []
    result = ", ".join(str(i) for i in collatz_sequence(user_enter))
    print(result)
except (ValueError, TypeError):
    print("Please enter the correct number.")
