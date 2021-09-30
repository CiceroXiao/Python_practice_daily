import random
from cho_han import ChoHan
import sys

user_money = 200

is_on = True

while is_on:
    try:
        dices = [random.randint(1, 6) for i in range(2)]
        dices_sum = sum(dices)

        cho_han = ChoHan(user_money)

        dices_sum_type = cho_han.cho_or_han(dices_sum)
        user_bet_amounts = eval(
            input(f"You have {user_money} mon. "
                  f"How much do you bet? (or Ctrl+C to QUIT) \n > "))
        if user_bet_amounts > cho_han.money:
            print("You do not have enough money. Please re-bet.")
        else:
            user_bet = input("CHO (even) or HAN (odd)?\n > ").upper()

            print("The dealer lifts the cup to reveal:")
            print("GO - GO")
            print(f"{dices[0]} - {dices[1]}")

            if cho_han.check_bet(user_bet, dices_sum_type):
                cho_han.reward_user(user_bet_amounts)
            else:
                cho_han.punish_user(user_bet_amounts)

            user_money = cho_han.money

            user_choice = input("Do you want to keep playing? Y / N \n")
            if user_choice.upper() == "Y":
                is_on = False

            if cho_han.money <= 0:
                is_on = False
                print("You are out of money.")

    except KeyboardInterrupt:
        sys.exit()
    except Exception:
        print("Please enter the correct value.")
        pass
