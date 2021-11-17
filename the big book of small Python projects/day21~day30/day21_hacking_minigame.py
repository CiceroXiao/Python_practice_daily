import sys

password = "Test"

print("""
Find the password in the computer's memory:
0x1150  $],>@|~~RESOLVE^    0x1250  {>+)<!?CHICKEN,%
0x1160  }@%_-:;/$^(|<|!(    0x1260  .][})?#@#ADDRESS
0x1170  _;)][#?<&~$~+&}}    0x1270  ,#=)>{-;/DESPITE
0x1180  %[!]{REFUGEE@?~,    0x1280  }/.}!-DISPLAY%%/
0x1190  _[^%[@}^<_+{_@$~    0x1290  =>>,:*%?_?@+{%#.
0x11a0  )?~/)+PENALTY?-=    0x12a0  >[,?*#IMPROVE@$/
""")


def check_password(true_password, user_password):
    true_password_length = len(true_password)

    true_password_list = [_ for _ in true_password]
    user_password_list = [_ for _ in user_password]

    true_times = 0

    for _ in range(min(true_password_length, len(user_password))):
        if true_password_list[_] == user_password_list[_]:
            true_times += 1

    return true_times, true_password_length


try:
    try_time = 4
    while try_time > 0:
        print(f"Enter password: ({try_time} tries remaining)")
        user_enter = input("> ")
        result = check_password(password, user_enter)
        if result[0] == result[1]:
            print("A C C E S S   G R A N T E D")
        else:
            print(f"Access Denied ({result[0]}/{result[1]} correct)")

        try_time -= 1
except KeyboardInterrupt:
    sys.exit()
