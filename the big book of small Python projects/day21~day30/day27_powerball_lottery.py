import random
import sys

print("""
Powerball Lottery, by Al Sweigart al@inventwithpython.com

Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.
""")
print("This simulation gives you the thrill of playing without"
      " wasting money.")
try:
    COST = 2

    all_digits = set()

    while len(all_digits) < 5:
        print("Enter 5 different numbers from 1 to 69, with spaces between")
        print("each number. (For example: 5 17 23 42 50 51)")
        first_five_digits = input("> ")
        for _ in first_five_digits.split():
            if _.isdecimal() and 1 <= int(_) <= 69:
                all_digits.add(_)
            else:
                print("Please enter the correct digits.")
                all_digits.clear()

    while len(all_digits) < 6:
        last_digit = input("Enter the powerball number from 1 to 26.\n > ")
        if last_digit.isdecimal() and 1 <= int(last_digit) <= 26 and int(
                last_digit) not in all_digits:
            all_digits.add(last_digit)
        else:
            print("No repeat digits.")
    print("How many times do you want to play? (Max: 1000000)")
    play_times = input("> ")
    if play_times.isdecimal() and 0 < int(play_times) < 1000000:
        total_cost = int(play_times) * COST
        print(f"It costs ${total_cost} to play {play_times} times, "
              "but don't")
        print("worry. I'm sure you'll win it all back.")
        print("Press Enter to start...")
    else:
        print("Too many times. Please enter again.")
        sys.exit()

    input()

    def generate_lucky_digits():

        first_five_lucky_digits = set()
        while len(first_five_lucky_digits) < 5:
            number = random.randint(1, 69)
            first_five_lucky_digits.add(str(number))

        last_lucky_digit = set()
        while len(last_lucky_digit) < 1:
            number = random.randint(1, 26)
            if number not in first_five_lucky_digits:
                last_lucky_digit.add(str(number))

        return first_five_lucky_digits, last_lucky_digit

    def check(x, y):
        if x == y:
            return True
        else:
            return False

    bouns = 0
    play_times = int(play_times)
    while play_times > 0:
        result = set()
        first_five_winning_numbers = generate_lucky_digits()[0]
        last_winning_numbers = generate_lucky_digits()[1]
        result.update(first_five_winning_numbers)
        result.update(last_winning_numbers)

        print(
            f"The winning numbers are: {' '.join(first_five_winning_numbers)}"
            f" and {''.join(last_winning_numbers)}  ",
            end="")

        if check(all_digits, result):
            print("You Win!!")
            bouns = 1.586 * 100000000
            break
        else:
            print("You lost.")

        play_times -= 1

    print(f"You have wasted ${total_cost}", end="")
    if bouns != 0:
        print(f"But, you win {bouns}!!!!")
except KeyboardInterrupt:
    sys.exit()
