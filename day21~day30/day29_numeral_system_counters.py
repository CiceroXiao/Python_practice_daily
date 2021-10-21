import re

start_number = 0
numbers_to_display = 20


def translate(num):
    decimal = num
    binary = re.split("b", bin(num))[1]
    hexadecimal = re.split('x', hex(num))[1]

    return decimal, hexadecimal, binary


for i in range(start_number, start_number + numbers_to_display, 1):
    result = translate(i)
    print(f"DEC: {result[0]}    HEX: {result[1]}    BIN: {result[2]}")
