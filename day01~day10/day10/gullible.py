import sys

is_on = True
while is_on:
    try:
        user_choice = input(
            "Do you want to know how to keep a "
            "gullible person busy for hours? Y/N"
            "\n> "
        )

        if user_choice.upper() in ["Y", "YES"]:
            continue
        elif user_choice.upper() in ["N", "No"]:
            print("Thank you. Have a nice day!")
            is_on = False
        else:
            print(f"{user_choice} is not a valid yes/no response.")
    except KeyboardInterrupt:
        sys.exit()
