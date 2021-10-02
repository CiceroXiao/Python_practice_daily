import sys
import random
import time

LINE_WIDTH = 78
GAP_WIDTH = 10

left_width = 24
width_changes = random.randint(1, 4)

print("Press Ctrl-C to stop.")

try:
    while True:
        time.sleep(1)
        left_width = left_width + width_changes * random.choice([-1, 1])
        if left_width > 30:
            left_width -= 5
        if left_width < 2:
            left_width += 5
        right_width = LINE_WIDTH - left_width - GAP_WIDTH
        print("#" * left_width, " " * GAP_WIDTH, "#" * right_width)
except KeyboardInterrupt:
    sys.exit()
