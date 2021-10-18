import pyperclip

print("Enter your message:")

text = input("> ")

VOWEL = list("aoeiu")
CONSONANT = list("bcdfghjklnmpqrstvwxyz")


def translate_word(string):
    start = 0

    if string[start].lower() in VOWEL:
        return string.lower() + "yay"

    text = []
    while string[start].lower() not in VOWEL and start < len(string):
        text.append(string[start].lower())
        start += 1
    if string[-1].isalpha():
        return string[start:] + "".join(text) + "ay"
    else:
        return string[start:-1] + "".join(text) + "ay" + string[-1]


text_translated = []

for _ in text.split():
    text_translated.append(translate_word(_))

text_translated_result = " ".join(text_translated).capitalize()
pyperclip.copy(text_translated_result)

print(text_translated_result)
print("(Copied pig latin to clipboard.)")
# result: Isthay isyay ayay eryvay erioussay essagemay.
