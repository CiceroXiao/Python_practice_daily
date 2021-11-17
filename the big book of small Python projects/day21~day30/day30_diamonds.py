"""
Programmer：Cicero
Create Time: 2021-11-8
Environment: Python3.8.8
Description：此程序用于生成棱形的单层钻石图案
"""
import sys

# 思路：根据钻石图案的规律，可以根据钻石图案的空格数，生成矩形的钻石图案
# 空格有两种：一种是每行第一个字符前的空格，一种是每行第一个字符后的空格


def create_diamond(diamond_size: int, diamond_nested_or_not: bool = False):
    """
    根据输入的钻石图案的大小，生成钻石图案。
    dimond_size: 钻石图案的大小，即钻石的层数，只能是大于 0 的整数
    diamond_nested_or_not: 是否为嵌套的钻石图案，默认为 False
    """
    if diamond_size <= 0:
        print("输入的钻石图案的大小不能小于 0，请重新输入！")
        sys.exit(1)
    if diamond_size >= 20:
        print("输入的钻石图案的大小不能大于 20，请重新输入！")
        sys.exit(1)

    def __inite__(self):
        """
        初始化
        """
        self.diamond_size = diamond_size

    BLACK = " " if diamond_nested_or_not is False else ""

    def generate_diamond_upper():
        """
        此部分用于生成钻石图案的上半部分
        """
        number_of_space_before_first_symbol = diamond_size - 1
        number_of_space_after_first_symbol = 0
        number_of_symbols_per_line = 1
        while number_of_space_before_first_symbol >= 0:

            print(" " * number_of_space_before_first_symbol, end="")

            print("/" * number_of_symbols_per_line, end="")
            print(BLACK * number_of_space_after_first_symbol, end="")
            print("\\" * number_of_symbols_per_line)

            number_of_space_before_first_symbol -= 1
            number_of_space_after_first_symbol += 2
            if diamond_nested_or_not is True:
                number_of_symbols_per_line += 1

    def generate_diamond_lower():
        """
        此部分用于生成钻石图案的下半部分
        """
        number_of_space_before_first_symbol = 0
        number_of_space_after_first_symbol = (diamond_size - 1) * 2
        number_of_symbols_per_line = \
            1 if diamond_nested_or_not is False else diamond_size
        while number_of_space_before_first_symbol < diamond_size:

            print(" " * number_of_space_before_first_symbol, end="")

            print("\\" * number_of_symbols_per_line, end="")
            print(BLACK * number_of_space_after_first_symbol, end="")
            print("/" * number_of_symbols_per_line)

            number_of_space_before_first_symbol += 1
            number_of_space_after_first_symbol -= 2
            if diamond_nested_or_not is True:
                number_of_symbols_per_line -= 1

    generate_diamond_upper()
    generate_diamond_lower()


def main(diamond_size: int = 1, diamond_nested_or_not: bool = False):
    """
    主函数
    """
    create_diamond(diamond_size, diamond_nested_or_not)


if __name__ == "__main__":
    try:
        main(diamond_size=12, diamond_nested_or_not=False)
    except TypeError:
        print("输入的钻石图案的大小必须是大于 0 的正整数，请重新输入！")
        sys.exit(1)
    finally:
        print("程序已退出！")
