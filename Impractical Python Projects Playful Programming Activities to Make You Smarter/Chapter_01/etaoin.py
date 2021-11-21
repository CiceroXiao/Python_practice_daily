"""
创建者：Cicero
创建时间：2021-11-19
运行环境：Python 3.8.8
"""
import collections


def count_letters(text: str) -> dict:
    """
    输入一段文本，输出其中每个字母的数量，并以字典的形式输出。

    参数：
        text: 输入的字符串。

    返回值：
        count_result: 字典，其中 key 为字母，value 为字母的数量。
    """
    # 将字符串转换为小写，避免大小写问题。
    text = text.lower()

    # 初始化字典，只用于存储字母及各字母的数量，以避免储存其他非字母字符。
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    count_result = collections.defaultdict(list)

    for _ in text:
        if _ in ALPHABET:
            count_result[_].append(_)
    return count_result


def main():
    """
    主函数，返回一个字符型的简单条形图。
    """
    text = input("Please enter a text.\n >")
    count_result = count_letters(text)

    count_result = dict(sorted(count_result.items()))
    print(count_result)


if __name__ == "__main__":
    main()
