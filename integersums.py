""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""
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


def add_it_up():
    n = typing_input("Please enter an integer\n")
    try:
        n = int(n)
        list_zero_to_n = [*range(0, n + 1)]
        return sum(list_zero_to_n)
    except:
        print("Number could not be converted to an integer.")
        n = typing_input("Please enter an integer\n")
        try:
            n = int(n)
            list_zero_to_n = [*range(0, n + 1)]
            return sum(list_zero_to_n)
        except:
            print("Number could not be converted to an integer.")
            print("Terminating script")
            exit()


answer_list = add_it_up()
print(answer_list)
