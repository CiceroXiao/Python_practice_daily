import datetime as dt
import number_to_drawing
import sys
import time

try:
    while True:
        hour = dt.datetime.now().hour
        minute = dt.datetime.now().minute
        second = dt.datetime.now().second
        print(f"{hour}:{minute}:{second}")

        hour_drawing = number_to_drawing.NumberToDrawing(hour, 2)
        minute_drawing = number_to_drawing.NumberToDrawing(minute, 2)
        second_drawing = number_to_drawing.NumberToDrawing(second, 2)

        top_line = f"{hour_drawing[0]}   {minute_drawing[0]}   {second_drawing[0]}"
        mid_line = f"{hour_drawing[1]} * {minute_drawing[1]} * {second_drawing[1]}"
        bottom_line = f"{hour_drawing[2]} * {minute_drawing[2]} * {second_drawing[2]}"

        print(top_line)
        print(mid_line)
        print(bottom_line)
        print("Press Ctrl-C to quit.")
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
