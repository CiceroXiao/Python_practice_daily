"""
创建者：Cicero
创建时间：2021-11-18
运行环境：Python 3.8.8
"""
import sys

VOWEL = list("aoeiu")


def generate_pig_latin_word(word: str) -> str:
    """
    将单词转换为猪拉丁语。
    转换规则：
        如果单词以元音开始，则直接在单词的末尾添加“way”。
        如果单词以辅音开始，则将辅音后移到单词的末尾，并在单词末尾添加“ay”。

    参数：
        word：单词

    返回值：
        str: Pig Latin 化的单词
    """
    # 去除首尾空格，因为用户输入的单词可能有空格
    word = word.strip()

    if word[0].isalpha() is False:
        print("Error: The word should start with a letter.")
        return None

    if word[0] in VOWEL:
        return word + "way"

    if word[-1].isalpha() is False:
        for start in range(len(word)):
            if word[start] in VOWEL:
                return word[start:-1] + word[:start] + "ay" + word[-1]
        return word[:-1] + "ay" + word[-1]
    else:
        for start in range(len(word)):
            if word[start] in VOWEL:
                return word[start:] + word[:start] + "ay"
        return word + "ay"


def generate_pig_latin_sentence(sentence: str) -> str:
    """
    将整个句子转换成猪拉丁语。
    转换规则：
        将单词按照空格分隔，然后依次调用 generate_pig_latin_word() 函数，将结果拼接成一个新句子。

    参数：
        sentence：句子

    返回值：
        str: Pig Latin 化的句子
    """
    # 去除首尾空格，因为用户输入的句子可能有空格
    sentence = sentence.strip()

    words = sentence.split()
    pig_latin_words = []
    for word in words:
        pig_latin_words.append(generate_pig_latin_word(word))

    return " ".join(pig_latin_words)


def main():
    """
    生成猪拉丁语的主函数。
    """
    while True:
        print("\nClick on 'ENTER' to exit.")
        print("or please input a word or a sentence:")
        sentence = input()
        if sentence == "":
            sys.exit(0)
        print(f"\n{sentence}\n ↓ \n{generate_pig_latin_sentence(sentence)}")


if __name__ == '__main__':
    main()
