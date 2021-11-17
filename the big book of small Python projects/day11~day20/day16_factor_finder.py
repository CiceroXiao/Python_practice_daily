# 创建日期：2021-10-8
import sys


def factor_finder(num):
    if num.upper() == 'QUIT':
        sys.exit()

    if int(num) > 0 and num.isdecimal():
        num = int(num)
        factor_for_compare = [i for i in range(num // 2) if i != 0]

        factors = []

        if num == 1:
            factors.append(1)

        if num == 2 or num == 3:
            factors += [1, num]

        for i in factor_for_compare:
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)

        factors.sort()

        return factors


while True:
    try:
        print('Enter a number to factor (or "QUIT" to quit):')
        nums = input("> ")
        result = factor_finder(nums)
        result_string = []
        for i, factor in enumerate(result):
            result_string.append(str(factor))

        print(", ".join(result_string))
        print()
    except KeyboardInterrupt:
        sys.exit()
