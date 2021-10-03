row_first = r"/ \_"
row_second = r"\_/ "

repeat_times_x = 5
repeat_times_y = 3

for y in range(repeat_times_y):
    """
    逐行打印字符
    """
    for x in range(repeat_times_x):
        print(row_first, end="")
    print()
    for x in range(repeat_times_x):
        print(row_second, end="")
    print()
