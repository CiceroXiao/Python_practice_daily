"""
创建者：Cicero
创建时间：2021-11-18
运行环境：Python 3.8.8
"""

import random
import sys
import pyperclip

first_names = [
    'Baby Oil',
    'Bad News',
    'Big Burps',
    "Bill 'Beenie­Weenie'",
    "Bob 'Stinkbug'",
    'Bowel Noises',
    'Boxelder',
    "Bud 'Lite' ",
    'Butterbean',
    'Buttermilk',
    'Buttocks',
    'Chad',
    'Chesterfield',
    'Chewy',
    'Chigger", "Cinnabuns',
    'Cleet',
    'Cornbread',
    'Crab Meat',
    'Crapps',
    'Dark Skies',
    'Dennis Clawhammer',
    'Dicman',
    'Elphonso',
    'Fancypants',
    'Figgs',
    'Foncy',
    'Gootsy',
    'Greasy Jim',
    'Huckleberry',
    'Huggy',
    'Ignatious',
    'Jimbo',
    "Joe 'Pottin Soil'",
    'Johnny',
    'Lemongrass',
    'Lil Debil',
    'Longbranch',
    '"Lunch Money"',
    'Mergatroid',
    '"Mr Peabody"',
    'Oil­Can',
    'Oinks',
    'Old Scratch',
    'Ovaltine',
    'Pennywhistle',
    'Pitchfork Ben',
    'Potato Bug',
    'Pushmeet',
    'Rock Candy',
    'Schlomo',
    'Scratchensniff',
    'Scut',
    "Sid 'The Squirts'",
    'Skidmark',
    'Slaps',
    'Snakes',
    'Snoobs',
    'Snorki',
    'Soupcan Sam',
    'Spitzitout',
    'Squids',
    'Stinky',
    'Storyboard',
    'Sweet Tea',
    'TeeTee',
    'Wheezy Joe',
    "Winston 'Jazz Hands'",
    'Worms',
]
last_names = [
    'Appleyard',
    'Bigmeat',
    'Bloominshine',
    'Boogerbottom',
    'Breedslovetrout',
    'Butterbaugh',
    'Clovenhoof',
    'Clutterbuck',
    'Cocktoasten',
    'Endicott',
    'Fewhairs',
    'Gooberdapple',
    'Goodensmith',
    'Goodpasture',
    'Guster',
    'Henderson',
    'Hooperbag',
    'Hoosenater',
    'Hootkins',
    'Jefferson',
    'Jenkins',
    'Jingley­Schmidt',
    'Johnson',
    'Kingfish',
    'Listenbee',
    'McFadden',
    'Moonshine',
    'Nettles',
    'Noseworthy',
    'Olivetti',
    'Outerbridge',
    'Overpeck',
    'Overturf',
    'Oxhandler',
    'Pealike',
    'Pennywhistle',
    'Peterson',
    'Pieplow',
    'Pinkerton',
    'Porkins',
    'Putney',
    'Quakenbush',
    'Rainwater',
    'Rosenthal',
    'Rubbins',
    'Sackrider',
    'Snuggleshine',
    'Splern',
    'Stevens',
    'Stroganoff',
    'Sugar­Gold',
    'Swackhamer',
    'Tippins',
    'Turnipseed',
    'Vinaigrette',
    'Walkingstick',
    'Wallbanger',
    'Weewax',
    'Weiners',
    'Whipkey',
    'Wigglesworth',
    'Wimplesnatch',
    'Winterkorn',
    'Woolysocks',
    "M'Bembo",
]


def main():
    """从两个列表中随机组成一个英语姓名，并将其打印在屏幕上"""
    try:
        full_names = []
        program_continue = True
        while program_continue:
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)

            full_name = first_name + ' ' + last_name
            full_names.append(full_name)

            # 输出当前生成的名字之数量，以便于用户确认是否继续生成名字
            print("The current number of generated names is:", end=' ')
            print(str(len(full_names)))

            whether_to_continue = input(
                'Do you want to generate more names? (y/n)\n')
            if whether_to_continue.isalpha() and whether_to_continue.lower(
            ) == 'y':
                program_continue = True
            else:
                program_continue = False
        # 询问用户是否将生成的名字复制到剪贴板
        copy_to_clipboard = input(
            "Do you want to copy the generated"
            "names to your clipboard? (y/n)\n"
        )
        if copy_to_clipboard.isalpha() and copy_to_clipboard.lower() == 'y':
            pyperclip.copy('\n'.join(full_names))
            print('\nThe generated names have been copied to your clipboard.')
        else:
            print(
                "\nThe generated names have not been"
                " copied to your clipboard."
            )

        print("\nThe generated names are: ")
        print('\n'.join(full_names))
    except KeyboardInterrupt:
        print('\n' + 'The program has been terminated by user.')
        sys.exit()

    return None


if __name__ == '__main__':
    main()
