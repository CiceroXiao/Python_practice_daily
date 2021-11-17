"""
Programmer：Cicero
Create Time: 2021-11-11
Environment: Python3.8.8
Description：此程序用于生成“Lucky Stars”的游戏
Rules：
    程序随机生成三颗骰子。
    如果其中有 Star，则 Star 计数加 1，Scores 计数加 1；
    如果其中有 Skull，则 Skull 计数加 1；
    如果骰子是 "?"，则无任何事情发生。
    如果某位玩家获得了三颗 Skull，则此玩家的 Stars 与 Skull 清零。
    谁先拥有 10 颗 Stars，则游戏结束，谁获胜。
    GOLD_DICE，即 Stars，一共有 6 颗；
    SLIVER_DICE：即“？”，一共有 4 颗；
    BRONTE_DICE：即 Skull，一共有 3 颗。
"""


class LuckStars:

    GOLD_DICE_PICTURE = """
                +-----------+
                |     .     |
                |    ,O,    |
                | 'ooOOOoo' |
                |   `OOO`   |
                |   O' 'O   |
                +-----------+
                """

    BRONTE_DICE_PICTURE = r"""
                +-----------+
                |    ___    |
                |   /   \   |
                |  |() ()|  |
                |   \ ^ /   |
                |    VVV    |
                +-----------+
                """

    SLIVER_DICE_PICTURE = """
                +-----------+
                |           |
                |           |
                |     ?     |
                |           |
                |           |
                +-----------+
                    """
    DICES_DICT = {
        1: GOLD_DICE_PICTURE,
        2: SLIVER_DICE_PICTURE,
        3: BRONTE_DICE_PICTURE,
    }

    def __init__(self, name):
        self.user_name = name
        self.user_score = 0
        self.num_of_stars_for_dices = 6
        self.num_of_question_mark_for_dices = 4
        self.num_of_skulls_for_dices = 3
        self.num_of_stars_for_the_user = 0
        self.num_of_skulls_for_the_user = 0

    def roll_dice(self) -> int:
        """
        生成一个随机数，用来掷骰子。返回值在 1~3 之间。
        """
        import random
        stars = [1] * self.num_of_stars_for_dices
        question_mark = [2] * self.num_of_question_mark_for_dices
        skulls = [3] * self.num_of_skulls_for_dices
        dices = stars + question_mark + skulls
        return random.choice(dices)

    def get_dice_picture_by_number(self, dice_number: int) -> str:
        """
        根据骰子的编号，返回骰子的图片。

        dice_number: 骰子的编号，可以是 1, 2, 3。
        """
        return self.DICES_DICT.get(dice_number, "can't get dices")

    def check_dice(self, dice_number: int):
        """
        根据骰子的编号，检查骰子的类型，并增加相应类型的数量。

        dice_number: 骰子的编号，可以是 1, 2, 3。
        """
        if dice_number == 1:
            self.num_of_stars_for_the_user += 1
        if dice_number == 3:
            self.num_of_skulls_for_the_user += 1
        return None

    def set_stars_and_skulls_to_zero(self):
        """
        清零 Stars 和 Skulls。
        """
        self.num_of_stars_for_the_user = 0
        self.num_of_skulls_for_the_user = 0
        return None
