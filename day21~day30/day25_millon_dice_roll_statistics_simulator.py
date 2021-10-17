import random

ROLL_TIMES = 1000000

print("Enter how many six-sided dice you want to roll:")

dice_numbers = input("> ")

dice_results = {}

print(f"Simulating {ROLL_TIMES} rolls of {dice_numbers} dice...")

for i in range(ROLL_TIMES):

    if i == ROLL_TIMES * 0.362:
        print("36.2% done...")

    if i == ROLL_TIMES * 0.734:
        print("73.4% done...")

    roll_dice = sum([random.randint(1, 6) for i in range(int(dice_numbers))])

    if roll_dice in dice_results.keys():
        dice_results[roll_dice] = dice_results.get(roll_dice) + 1
    else:
        dice_results[roll_dice] = 1

dice_results = dict(sorted(dice_results.items()))

print("TOTAL - ROLLS - PERCENTAGE")

for value, times in dice_results.items():
    print(f"{value} - {times} rolls - {round(times/ROLL_TIMES * 100, 1)}%")
