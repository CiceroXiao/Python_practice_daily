import random
import sys

secret_number = random.randint(0, 100)


def compare_two_numbers(gusee_number, secret_number):
    gusee_number = int(gusee_number)
    if gusee_number == secret_number:
        print("Yay! You guessed my number!")
        return True
    elif gusee_number > secret_number:
        print("Your guess is too high.")
        return False
    else:
        print("Your guess is too low.")
        return False


print("I am thinking of a number between 1 and 100.")

user_guess_time = 10
is_over = False
try:
    while not is_over:
        user_guess_numbers = input(
            f"You have {user_guess_time} guesses left. Take a guess.\n> ")
        is_over = compare_two_numbers(gusee_number=user_guess_numbers,
                                      secret_number=secret_number)
        user_guess_time -= 1
        if user_guess_time < 0:
            is_over = True
            print(
                f"Game over. "
                f"The number I was thinking of was {secret_number}")
except KeyboardInterrupt:
    sys.exit()
except (TypeError, ValueError):
    print("Please enter the correct number.(0~100)")
    sys.exit()
