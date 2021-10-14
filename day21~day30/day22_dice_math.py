import random
import sys
import time

DICE_WIDTH = 9
DICE_HEIGHT = 5

dice_dict = {
    1: ['+-------+', '|       |', '|   O   |', '|       |', '+-------+'],
    2: ['+-------+', '|0      |', '|       |', '|      0|', '+-------+'],
    7: ['+-------+', '|      0|', '|       |', '|0      |', '+-------+'],
    3: ['+-------+', '|0      |', '|   O   |', '|      0|', '+-------+'],
    8: ['+-------+', '|      0|', '|   O   |', '|0      |', '+-------+'],
    4: ['+-------+', '|0     0|', '|       |', '|0     0|', '+-------+'],
    5: ['+-------+', '|0     0|', '|   O   |', '|0     0|', '+-------+'],
    6: ['+-------+', '|0     0|', '|0     0|', '|0     0|', '+-------+'],
}


def generate_dice():
    dice_numbers = random.randint(1, 2)
    dice_points_all = []
    for _ in range(dice_numbers):
        dice_points = random.randint(1, 8)
        dice_points_all.append(dice_points)

    return dice_points_all


def generate_asci(number):
    return dice_dict.get(number)


print("""
Add up the sides of all the dice displayed on the screen. You have
30 seconds to answer as many as possible. You get 4 points for each
correct answer and lose 1 point for each incorrect answer.
""")
input("Press Enter to begin...")
user_score = 0
try:
    while True:
        start = time.time()
        dices = generate_dice()

        dices_sum = sum(dices)
        seven_eight_nums = dices.count(7) + dices.count(8)
        dices_sum = dices_sum - 5 * seven_eight_nums

        dices_asci = [generate_asci(i) for i in dices]
        x_distance, y_distance = " ", "\n"

        for i in dices_asci:
            x_nums = random.randint(0, 4) * DICE_WIDTH
            y_nums = random.randint(0, 2) * DICE_HEIGHT

            print(x_distance * x_nums, end="")

            for j in range(len(i)):
                print(i[j])
                print(x_distance * x_nums, end="")

            print(y_distance * y_nums)

        user_answer = input("Enter the sum:\n > ")

        if time.time() - start > 30:
            print("30 seconds done. You lose 1 point.")
            user_score -= 1
        else:
            if not user_answer.isdecimal():
                print("Please enter the positive integer.")
                continue
            elif int(user_answer) == dices_sum:
                print("Congratulations on your correct answer."
                      " You get 4 points.")
                user_score += 4
            else:
                print("Sorry, you wrong. You lose 1 point.")
                user_score -= 1

        print(f"Now, you total score is {user_score}")
        print("Enter Ctrl+C to exit.")
        print()
except KeyboardInterrupt:
    print(f"Your total score is {user_score}")
    sys.exit()
