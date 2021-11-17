import random
import sys
import time

DNA_dictionary = {
    "G": "C",
    "C": "G",
    "A": "T",
    "T": "A",
}
try:
    time.sleep(0.5)
    while True:
        text = [random.choice(list(DNA_dictionary.keys())) for i in range(16)]

        print(f"        #{text[0]}-{DNA_dictionary.get(text[0])}#")
        time.sleep(0.5)
        print(f"       #{text[1]}---{DNA_dictionary.get(text[1])}#")
        time.sleep(0.5)
        print(f"      #{text[2]}-----{DNA_dictionary.get(text[2])}#")
        time.sleep(0.5)
        print(f"     #{text[3]}------{DNA_dictionary.get(text[3])}#")
        time.sleep(0.5)
        print(f"    #{text[4]}------{DNA_dictionary.get(text[4])}#")
        time.sleep(0.5)
        print(f"    #{text[5]}-----{DNA_dictionary.get(text[5])}#")
        time.sleep(0.5)
        print(f"     #{text[6]}---{DNA_dictionary.get(text[6])}#")
        time.sleep(0.5)
        print(f"     #{text[7]}-{DNA_dictionary.get(text[7])}#")
        time.sleep(0.5)
        print("      ##")
        time.sleep(0.5)
        print(f"     #{text[8]}-{DNA_dictionary.get(text[8])}#")
        time.sleep(0.5)
        print(f"     #{text[9]}---{DNA_dictionary.get(text[9])}#")
        time.sleep(0.5)
        print(f"    #{text[10]}-----{DNA_dictionary.get(text[10])}#")
        time.sleep(0.5)
        print(f"    #{text[11]}------{DNA_dictionary.get(text[11])}#")
        time.sleep(0.5)
        print(f"     #{text[12]}------{DNA_dictionary.get(text[12])}#")
        time.sleep(0.5)
        print(f"      #{text[13]}-----{DNA_dictionary.get(text[13])}#")
        time.sleep(0.5)
        print(f"       #{text[14]}---{DNA_dictionary.get(text[14])}#")
        time.sleep(0.5)
        print(f"        #{text[15]}-{DNA_dictionary.get(text[15])}#")
        time.sleep(0.5)
        print("         ##")
except KeyboardInterrupt:
    sys.exit()
