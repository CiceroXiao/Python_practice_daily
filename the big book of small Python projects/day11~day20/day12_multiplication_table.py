print("Multiplication Table, by Al Sweigart al@inventwithpython.com")
print("  |  0   1   2   3   4   5   6   7   8   9  10  11  12")
print("--+---------------------------------------------------")

for row in range(0, 13):

    print(f"{str(row).rjust(2)}|", end="")

    for column in range(0, 13):
        multi_result = str(row * column)
        if column < 1:
            print(f"{multi_result.rjust(3)}", end="")
        else:
            print(f"{multi_result.rjust(4)}", end="")

    print()
