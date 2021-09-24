import random
import datetime as dt

date_num = eval(input("How many birthdays shall I generate? (Max 100)\n"))


def generate_random_date(nums=1):
    start_date = dt.datetime(1900, 1, 1)
    end_date = dt.datetime(1900, 12, 31)
    all_birthday = [
        (start_date +
         (end_date - start_date) * random.random()).strftime("%b %d")
        for i in range(nums)
    ]

    return all_birthday


def detect_same_birthday(data):
    dupicates = set()
    for i in data:
        if data.count(i) > 1:
            dupicates.add(i)
    return dupicates


duplicate_times = 0

try:
    birthday_data = generate_random_date(date_num)
    birthday_data_text = ", ".join(birthday_data)
    print(f"Here are {date_num} birthdays:")
    print(birthday_data_text, "\n")
    duplicate_date = detect_same_birthday(birthday_data)
    if len(duplicate_date) != 0:
        duplicate_date_text = ", ".join(duplicate_date)
        print(f"In this simulation, "
              f"multiple people have a birthday on {duplicate_date_text}")
    else:
        print("In this simulation, no one has the same birthday.")

    generate_time = 100000
    user_choice = input(
        f"Generating 23 random birthdays {generate_time} times...\n"
        "Press Enter to begin...")
    if user_choice == "":
        print("Let's run another 100,000 simulations.")
        for i in range(generate_time):
            if i % (generate_time / 10) == 0:
                print(f"{i} simulations run...")
            birthday_data = generate_random_date(date_num)
            duplicate_date = detect_same_birthday(birthday_data)
            if len(duplicate_date) != 0:
                duplicate_times += 1
        frequency = round((duplicate_times / generate_time) * 100, 4)
        print(f"Out of {generate_time} simulations of {date_num} people, "
              f"there was a matching birthday in that group {duplicate_times}"
              f" times. This means that {date_num} people have a"
              f" {frequency} % chance of having a matching birthday in "
              f"their group. That's probably more than you would think!")
except ValueError:
    print("Please input the right number.")
except SyntaxError:
    print("Please input the right number.")
except NameError:
    print("Please input the right number.")
except TypeError:
    print("Please input the right number.")
