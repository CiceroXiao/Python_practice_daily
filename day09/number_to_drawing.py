def __init__():
    pass


def NumberToDrawing(numbers, number_width=0):
    """
    传入某个数字，并将此数字字符图形化表示。
    """
    numbers = str(numbers).zfill(number_width)
    number_list = ["", "", ""]
    for i, n in enumerate(numbers):
        if n == '0':
            number_list[0] += " __"
            number_list[1] += "|  |"
            number_list[2] += "|__|"
        if n == '1':
            number_list[0] += "    "
            number_list[1] += "   |"
            number_list[2] += "   |"
        elif n == '2':
            number_list[0] += " __ "
            number_list[1] += " __|"
            number_list[2] += "|__ "
        elif n == '3':
            number_list[0] += " __ "
            number_list[1] += " __|"
            number_list[2] += " __|"
        elif n == '4':
            number_list[0] += "    "
            number_list[1] += "|__|"
            number_list[2] += "   |"
        elif n == '5':
            number_list[0] += " __ "
            number_list[1] += "|__ "
            number_list[2] += " __|"
        elif n == '6':
            number_list[0] += " __ "
            number_list[1] += "|__ "
            number_list[2] += "|__|"
        elif n == '7':
            number_list[0] += " __ "
            number_list[1] += "   |"
            number_list[2] += "   |"
        elif n == '8':
            number_list[0] += " __ "
            number_list[1] += "|__|"
            number_list[2] += "|__|"
        elif n == '9':
            number_list[0] += " __ "
            number_list[1] += "|__|"
            number_list[2] += " __|"
    return number_list
