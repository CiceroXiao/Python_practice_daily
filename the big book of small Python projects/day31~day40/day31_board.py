class Board:
    def __init__(self):
        self.columns = 7
        self.rows = 6

    def generate_board(self) -> list:
        """
        生成棋盘
        """
        board = [['.' for _ in range(self.columns + 2)]
                 for _ in range(self.rows)]
        for i in board:
            i[0] = i[-1] = "+"
        board_title = list(" 1234567 ")
        board_first_row = board_last_row = list("+-------+")
        board.insert(0, board_title)
        board.insert(1, board_first_row)
        board.append(board_last_row)

        return board

    def print_board(board: list):
        """
        打印棋盘
        """
        for i in board:
            print("".join(i))

        return None

    def update_board(self, column: int, player: str, board: list) -> tuple:
        """
        更新棋盘。

        player： 玩家， 'X' or 'O'；
        column：下棋的列；
        board：棋盘；

        返回值：tuple[0]：棋盘；tuple[1]：是否下棋成功；
        """
        updated_or_not = False
        for _ in range(self.rows + 1, 1, -1):
            if board[_][column] == ".":
                board[_][column] = player
                updated_or_not = True
                break

        return (board, updated_or_not)

    def check_win(self, board: list) -> bool:
        """
        检查是否有获胜者
        board：棋盘；
        获胜情况有三种：
        1. 横向：以某点为中心，向左右两边检查是否有四个相同的棋子；
        2. 纵向；以某点为中心，向上下两边检查是否有四个相同的棋子；
        3. 斜向；以某点为中心，向左上到右下检查是否有四个相同的棋子；
        4. 斜向；以某点为中心，向左下到右上检查是否有四个相同的棋子；

        如果有获胜者，则返回 True；否则返回 False。
        """
        for i in range(2, self.rows + 2):
            for j in range(1, self.columns + 1):
                if board[i][j] == "." or board[i][j] == "-":
                    continue
                # 横向
                if board[i][j] == board[i][j + 1] == board[i][
                        j + 2] == board[i][j + 3]:
                    return True
                # 纵向
                if board[i][j] == board[i + 1][j] == board[
                        i + 2][j] == board[i + 3][j]:
                    return True
                # 斜向
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][
                        j + 2] == board[i + 3][j + 3]:
                    return True
                # 斜向
                if board[i][j] == board[i - 1][j + 1] == board[i - 2][
                        j + 2] == board[i - 3][j + 3]:
                    return True
        return False

    def check_vaild_column(self, board: list, column: int) -> bool:
        """
        检查某列是否有效。
        board：棋盘；
        column：列号；
        """
        for i in range(self.rows + 1, 1, -1):
            if board[i][column] == ".":
                return True

        return False
