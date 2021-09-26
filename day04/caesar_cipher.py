import pyperclip

all_letters = list("abcdefghijklmnopqrstuvwxyz".upper() * 2)

code_type = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ").lower()
the_key = eval(input("Please enter the key (0 to 25) to use.\n> "))
the_message = input("Enter the message to encrypt.\n> ").upper()


def caesar_cipher():
    the_message_processed = []
    code_type_model = ""
    for item in list(the_message):
        if item in all_letters:
            if code_type == "e":
                item_after_index = all_letters.index(item) + the_key
                code_type_model += "encrypte"
            if code_type == "d":
                item_after_index = all_letters.index(item) - the_key
                code_type_model += "decrypte"
            the_message_processed.append(all_letters[item_after_index])
        else:
            the_message_processed.append(item)
    the_message_processed_str = "".join(the_message_processed)
    pyperclip.copy(the_message_processed_str)
    print(the_message_processed_str)
    print(f"Full {code_type_model}d text copied to clipboard.")


try:
    if -26 < the_key < 26:
        caesar_cipher()
except ValueError:
    print("ValueError. Please input right value.")
except TypeError:
    print("TypeError. Please input right value.")
