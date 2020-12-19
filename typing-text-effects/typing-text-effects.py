# https://www.101computing.net/python-typing-text-effect/
import time, sys
import os


def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clear_screen():
    os.system("clear")


typing_print("Hello world...\n")
time.sleep(1)
typing_print("You've entered the Matrix!\n")
time.sleep(1)

pillColor = typing_input("Will you take the blue or the red pill? (Type b for blue, r for red)")

if pillColor == "b":
    typing_print("You took the blue pill! ")
    typing_print("You will be stuck in the Matrix forever!\n")
elif pillColor == "r":
    typing_print("You took the red pill! ")
    typing_print("You are leaving the Matrix and going back to the real world!\n")
else:
    typing_print("Invalid answer!")

time.sleep(1)
typing_print("Good bye!\n")
typing_print("This screen will clear itself in 3..")
time.sleep(1)
typing_print("2..")
time.sleep(1)
typing_print("1..")
time.sleep(1)
clear_screen()
