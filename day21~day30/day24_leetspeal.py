# 为了节省时间，每个英语字母只选取前两个 leet 字符
# 资料参考网址：https://zh.wikipedia.org/wiki/Leet
import random

english_letters = list("abcdefghijklnmopqrstuvwxyz")
leetspeak = [
    ["4", "/\\"],
    ["8", "13"],
    ["[", "¢"],
    [")", "|)"],
    ["3", "&"],
    ["|=", "ƒ"],
    ["6", "&"],
    ["#", "/-/"],
    ["1", "!"],
    ["_|", "_/"],
    ["X", "|<"],
    ["1", "£"],
    ["|v|", "[V]"],
    ["^/", "|\\|"],
    ["0", "()"],
    ["|*", "|o"],
    ["(_,)", "()_"],
    ["|`", "|~"],
    ["5", "$"],
    ["7", "+"],
    ["(_)", "|_|"],
    ["\\/", "|/"],
    ["\\/\\/", "vv"],
    ["><", "Ж"],
    ["j", "`/"],
    ["2", "7_"]
]

leetspeak_dict = {}

for key, value in zip(english_letters, leetspeak):
    leetspeak_dict[key] = value


def generate_leet(string):
    if string.lower() in leetspeak_dict.keys() and random.random() > 0.25:
        return random.choice(leetspeak_dict.get(string.lower()))
    else:
        return string


print("Enter your leet message:")
user_enter = input("> ")

user_leet = [generate_leet(item) for item in user_enter]
print("".join(user_leet))
