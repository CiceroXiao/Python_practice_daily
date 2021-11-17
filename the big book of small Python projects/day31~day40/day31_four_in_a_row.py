"""
Programmer：Cicero
Create Time: 2021-11-9
Environment: Python3.8.8
Description：此程序用于生成“four in a row”的游戏
Rules：
    获胜规则：如果某一行或者某一列或者某一对角线上的四个棋子都是同一个棋子，则该棋子获胜。
    下棋规则：每次下棋时，玩家可以选择任意一个 column，然后由下到上、在该 column 的第一个空格上放置一个棋子。
"""
from day31_board import Board
import sys


def main():
    """
    主函数
    """
    board = Board()
    game = board.generate_board()
    Board.print_board(game)
    players = ["X", "O"]
    game_over = False
    while not game_over:
        current_player = players[0]
        column = input(
            f"Player {current_player}, enter a column or QUIT:\n > ")
        if column.upper() == "QUIT":
            sys.exit()
        if not column.isdigit():
            print("Please enter a number.")
            continue
        if int(column) > board.columns:
            print(f"Please enter a number between 1 and {board.columns}.")
            continue

        # 核对棋手选择的 column 是否有效后，程序将 column 转换为整数，以便于下面的棋盘操作。
        column = int(column)

        # 程序将棋子放置到棋盘上之前，先检测该 column 是否已经满了。
        # 如果满了，则程序提示用户重新选择 column；否则，程序将棋子放置到棋盘上指定 column 上。
        if board.check_vaild_column(board=game, column=column):
            not_update = True
            while not_update:

                is_update = board.update_board(column=column,
                                               player=current_player,
                                               board=game)[1]
                if is_update:
                    not_update = False

            # 检查当前选手是否获胜，如果获胜则游戏结束；否则切换下一个选手。
            if board.check_win(game):
                print(f"Player {current_player} has won!")
                game_over = True
            else:
                # 棋局更新后，查看棋局情况，以便于棋手选择下一步
                Board.print_board(game)
                players.reverse()
        else:
            print("Column is full, please choose another column.")

    # 展示游戏结束后的棋局，以便于棋手查看棋局的具体情况，避免出现程序判断失误的情况。
    Board.print_board(game)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        print("\n\nGoodbye!😸😸😸")
