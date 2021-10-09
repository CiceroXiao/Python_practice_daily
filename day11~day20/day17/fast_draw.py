import time
import random
import sys

print("""
Time to test your reflexes and see if you are the fastest
draw in the west!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears.
Press Enter to begin...
It is high noon...
""")
while True:
    try:
        print("Press Enter to begin...")

        user_choice = input("> ")

        if user_choice.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        print("It is high noon...")
        time.sleep(random.random() * 10)
        start = time.time()
        print("DRAW!")

        input()

        end = time.time()
        time_reaction = end - start
        if time_reaction < 0.01:
            speed = "So fast!"
        elif 0.01 <= time_reaction < 0.3:
            speed = "Nomal."
        else:
            speed = "Too slow!"
        print(f"You took {time_reaction} seconds to draw. {speed}")
        print("Enter QUIT to stop, or press Enter to play again.")
    except KeyboardInterrupt:
        print("Thanks for playing!")
        sys.exit()
