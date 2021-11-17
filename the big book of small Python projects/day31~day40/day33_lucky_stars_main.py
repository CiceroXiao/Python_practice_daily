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

import day33_lucky_stars

WIN_SCORE = 2
NUM_OF_STARS_TO_ADD_SCORE = 3
NUM_OF_SKULLS_TO_CLEAR_SCORE = 3

jack = day33_lucky_stars.LuckStars("Jack")
jill = day33_lucky_stars.LuckStars("Jill")
user_list = [jack, jill]

is_on = True
while is_on:
    # 输出各位玩家的分数，以便于玩家了解游戏进展
    for user in user_list:
        print(f"{user.user_name}: {str(user.user_score)}", end="\t")

    current_player = user_list[0]
    print(f"It is {current_player.user_name}'s turn.")

    dices_number = [current_player.roll_dice() for _ in range(3)]

    # 输出骰子的结果
    for _ in dices_number:
        print(current_player.get_dice_picture_by_number(_))

    # 检测骰子的类型，并根据类型计数
    is_be_zero = False
    for dice in dices_number:
        current_player.check_dice(dice)

        if current_player.num_of_stars_for_the_user == NUM_OF_STARS_TO_ADD_SCORE:
            current_player.user_score += 1
            break

        if current_player.num_of_skulls_for_the_user == NUM_OF_SKULLS_TO_CLEAR_SCORE:
            is_be_zero = True
            current_player.set_stars_and_skulls_to_zero()
            print("Your number of skulls reaches three.")
            print("Your number of stars and skulls will be 0.")
            print("Don't be discouraged. Please start over.")

    # 判断是否获胜
    if current_player.user_score == WIN_SCORE:
        print(f"Congratulations, {current_player.user_name}! You win!")
        is_on = False

    # 如果当前玩家 Stars 未被程序清零，则询问当前玩家是否继续游戏
    # 如果当前玩家 Stars 被程序清零，则自动切换到下一个玩家
    if is_be_zero:
        user_list.reverse()
    else:
        # 检测玩家是否继续游戏
        choice_is_right = False
        while not choice_is_right:
            user_choice = input("Do you want to roll again? Y/N")
            if user_choice.lower() == "y":
                choice_is_right = True
            elif user_choice.lower() == "n":
                choice_is_right = True
                user_list.reverse()
            else:
                print("Please enter Y or N.")
