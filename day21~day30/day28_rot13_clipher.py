import sys

LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")


def encrypt(text, position=0):

    translated_result = ""

    for _ in text:
        if _.isalpha() and _.upper() in LETTERS:
            translated_result += LETTERS[LETTERS.index(_.upper()) + 13] \
                                 .lower()
        else:
            translated_result += _

    return translated_result


try:
    while True:
        print("Choice to encrypt/decrypt (or QUIT):")
        user_choice = input("> ")

        if user_choice.upper == "QUIT":
            sys.exit()

        print("Enter a message to encrypt/decrypt (or QUIT):")
        user_text = input("> ")

        if user_text.upper == "QUIT":
            sys.exit()

        if user_choice.lower() == "decrypt":
            search_position = 26
        else:
            search_position = 0

        result = encrypt(user_text, search_position)

        print(result)

        print()
except KeyboardInterrupt:
    sys.exit()
