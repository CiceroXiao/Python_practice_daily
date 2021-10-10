import time
import sys

print('(Press Ctrl-C to quit.)')

time.sleep(2)

all_bottles = 5

try:
    while all_bottles > 0:
        time.sleep(2)
        remaider_bottles = all_bottles - 1
        print(f"{all_bottles} bottles of milk on the wall,")
        time.sleep(0.2)
        print(f"{all_bottles} bottles of milk,")
        time.sleep(0.2)
        print("Take one down, pass it around,")
        time.sleep(0.2)
        if remaider_bottles == 0:
            remaider_bottles = "no more"
        print(f"{remaider_bottles} bottles of milk on the wall!")

        all_bottles -= 1

        print()
except KeyboardInterrupt:
    sys.exit()
