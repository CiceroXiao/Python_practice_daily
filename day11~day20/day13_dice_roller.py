import random
import sys
import re

print('''Dice Roller, by Al Sweigart al@inventwithpython.com
Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.
Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program
''')
while True:
    try:
        user_enter = input("> ")

        if user_enter.lower() == "quit":
            sys.exit()
        else:
            # 有些用户可能会输入空格，因此要先去掉用户输入字符中的空格
            user_enter = user_enter.lower().replace(" ", "")

            if user_enter.find("d") == -1:
                raise Exception("Missing the 'd' character.")

            times = user_enter.split("d")[0]
            sides = re.split('[+-]', user_enter.split("d")[1])[0]
            if "-" in user_enter or "+" in user_enter:
                bouns = re.split('[+-]', user_enter.split("d")[1])[1]
            else:
                bouns = ""

            all_dice_values = []
            for i in range(int(times)):
                dice_value = random.randint(1, int(sides))
                all_dice_values.append(dice_value)

            if bouns != "":
                all_dice_values.append(int(bouns))
                if int(bouns) > 0:
                    bouns = "+" + bouns

            sum_corrected_values = sum(all_dice_values)

            print(f"{times}d{sides}{bouns}")
            print(f"> {sum_corrected_values} ", end="")
            print(tuple(all_dice_values))
    except KeyboardInterrupt:
        sys.exit()
