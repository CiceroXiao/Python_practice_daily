import random
import sys
import time

LINE_WIDTH = 36

try:
    print("Press Ctrl-C to quit.")
    while True:
        time.sleep(0.5)
        line_done = 0
        while line_done < LINE_WIDTH:
            space_nums = random.randint(0, 5)
            zero_nums = random.randint(0, 1)
            one_nums = random.randint(0, 1)
            print(" " * space_nums, end="")
            print("1" * one_nums, end="")
            print("0" * zero_nums, end="")
            line_done += (space_nums + zero_nums + one_nums)

        print()
except KeyboardInterrupt:
    sys.exit()
