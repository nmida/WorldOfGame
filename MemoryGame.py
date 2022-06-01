import random
import time
import os



from Live import *

from random import sample

difficulty = choose2
list = [*range(1, 101)]

def generate_sequence():
    generate = sample(list,difficulty)
    print(f"You choose game difficulty {difficulty} now we generate {difficulty} numbers you need remembers to win the game:")
    print(generate)
    time.sleep(0.8)
    os.system('cls')
    return (generate)

def get_list_from_user():
    choose3 = 1
    list1 = []
    while choose3 <= difficulty:
        try:
            user_memory = int(input("write a number you remembers "))
            choose3=choose3+1
            list1.append(user_memory)
        except:
            print("You need to write just numbers, choose again")
            pass

    return (list1)


def is_list_equal():
    if generate_sequence() == get_list_from_user():
        return 1
    else:
        return 2


def play():
    print("################# Welcome to Memory Game #########################")
    if is_list_equal() == 1:
        print("!!!!!!congratulations you won it's!!!!!!", True)
    else:
        print("Hooo it's wrong!", False)




