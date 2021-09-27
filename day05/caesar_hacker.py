all_letters = list("abcdefghijklmnopqrstuvwxyz".upper() * 2)

the_message = input("Enter the message to encrypt.\n> ").upper()


def caesar_cipher(the_key):
    the_message_processed = []
    code_type_model = ""
    for item in list(the_message):
        if item in all_letters:
            item_after_index = all_letters.index(item) - the_key
            code_type_model += "encrypte"
            the_message_processed.append(all_letters[item_after_index])
        else:
            the_message_processed.append(item)

    the_message_processed_str = "".join(the_message_processed)
    print(f"Key #{the_key}: {the_message_processed_str}")


try:
    for the_key in range(26):
        caesar_cipher(the_key)
except (ValueError, TypeError):
    print("Please input right value.")
