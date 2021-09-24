import random

descripte_game = """
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
"""
print(descripte_game)

secret_num = str(random.randint(100, 999))

guess_times = 0
is_on = True
while is_on:
    cue = ""
    user_input = input(f"Guess #{guess_times+1}\n"
                       "Please input 3 numbers, like 973: \n> ")

    if user_input.lower() == "q":
        break
    elif user_input.lower() == "show me the number":
        print(f"The secret num is {secret_num}")
    else:
        for i in range(len(user_input)):
            if user_input[i] in secret_num:
                if user_input[i] == secret_num[i]:
                    cue += "Fermi "
                else:
                    cue += "Pico "
        guess_times += 1

    if user_input == secret_num or guess_times == 10:
        is_on = False
    else:
        if cue is False:
            cue += "Bagels"
        print(cue)

print(f"The secret number is {secret_num}")
