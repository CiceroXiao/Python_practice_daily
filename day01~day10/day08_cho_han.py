class ChoHan:
    def __init__(self, money):
        self.money = money
        self.the_house_take_rate = 0.1

    def cho_or_han(self, num):
        """
        If a number is even, then "CHO" is returned;
        else, "HAN" is returned.
        """
        if num % 2 == 0:
            return "CHO"
        else:
            return "HAN"

    def check_bet(self, user_answer, right_answer):
        """"
        If user bet is correct, then "True" is returned;
        else, "False" is returned.
        """
        if user_answer == right_answer:
            return True
        else:
            return False

    def reward_user(self, user_bet_amounts):
        """
        If the user was right, the user is rewarded with twice the bet.
        However, the house takes away 10%.
        """
        the_house_take_amounts = round(
            user_bet_amounts * 2 * self.the_house_take_rate, 2)
        rewards = round(user_bet_amounts * 2 - the_house_take_amounts, 2)
        self.money += rewards
        print(f"You won! You take {rewards} mon.")
        print(f"The house collects a {the_house_take_amounts} mon fee.")

    def punish_user(self, user_bet_amounts):
        """
        If the user was wrong, the user will lose the bet.
        """
        # minus user's money
        self.money -= user_bet_amounts
        print(f"You lose. You lose {user_bet_amounts} mon.")
