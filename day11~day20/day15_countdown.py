# import datetime as dt
import number_to_drawing
import sys
import time

hours = 0
minutes = 0
seconds = 5
seconds_left = hours * 60 * 60 + minutes * 60 + seconds
try:
    while seconds_left > 0:
        # print(f"{hour}:{minute}:{second}")
        hours_left = seconds_left // 60 // 60
        minutes_left = seconds_left // 60
        hour_drawing = number_to_drawing.NumberToDrawing(hours_left, 2)
        minute_drawing = number_to_drawing.NumberToDrawing(minutes_left, 2)
        second_drawing = number_to_drawing.NumberToDrawing(seconds_left, 2)

        top_line = f"{hour_drawing[0]}   {minute_drawing[0]} " \
                   f"  {second_drawing[0]}"
        mid_line = f"{hour_drawing[1]} * {minute_drawing[1]}" \
                   f" * {second_drawing[1]}"
        bottom_line = f"{hour_drawing[2]} * {minute_drawing[2]}" \
                      f" * {second_drawing[2]}"

        print(top_line)
        print(mid_line)
        print(bottom_line)
        print("Press Ctrl-C to quit.")
        time.sleep(1)
        seconds_left -= 1

    print("Countdown.")
except KeyboardInterrupt:
    sys.exit()
