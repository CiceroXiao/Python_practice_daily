"""
Programmer：Cicero
Create Time: 2021-11-10
Environment: Python3.8.8
Description：此程序用于生成“Hangman and Guillotine”的游戏
Rules：
    程序随机生成一个单词，用户输入一个字母，程序判断用户输入的字母是否在单词中。
    如果用户输入的字母在单词中，则玩家继续输入字母；如果用户输入的字母不在单词中，则玩家距离绞刑近一步。
    当用户完全猜对单词时，程序结束；当玩家被程序执行到绞刑时，程序结束。
"""


SECRET_WORD = 'python'
TIMES = 7
HANGMAN_PICS = {
    1:
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    2:
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    3:
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    4:
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    5:
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    6:
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    7:
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
}

secret_word = [i.upper() for i in SECRET_WORD]
user_guess = ["_" for _ in SECRET_WORD]
wrong_guess = set()
wrong_times = 0

is_on = True
while is_on:

    # 输出 user_guess，以便用户查看当前猜测情况
    print(user_guess)

    # 输出 wrong_guess，以便用户知道哪些字母已经被猜测过
    if wrong_times is None:
        print("Missed letters: No missed letters yet.")
    else:
        print(f"Missed letters: {sorted(wrong_guess)}")

    print("The category is: Animals")
    user_input = input('please input a word: \n> ')

    # 先判断用户输入的字符是否是字母。如果不是，则提示用户输入错误，并继续循环
    # 这样做，可以不用处理用户输入的其他字符，如数字、空格等
    if user_input.isalpha():
        if user_input.upper() in secret_word:
            # 将用户输入的字母替换为*，以避免重复判断
            index_of_user_input = secret_word.index(user_input.upper())
            secret_word[index_of_user_input] = '*'
            user_guess[index_of_user_input] = user_input.upper()
        else:
            wrong_guess.add(user_input.upper())
            TIMES -= 1
            wrong_times += 1
            print(HANGMAN_PICS.get(wrong_times, 'error'))
    else:
        print('please input a word')

    # 判断玩家是否已猜对 SECRET_WORD。
    # 如果玩家已经猜对，则结束游戏。
    if '_' not in user_guess:
        print('You win!')
        is_on = False
    # 如果猜测次数用完，则结束游戏。
    if TIMES == 0:
        print('You lose!')
        is_on = False
