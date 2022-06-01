import random as rd
from Live import *

difficulty = choose2
secret_number = 0

def generate_number():
    secret_number = rd.randint(1, difficulty*3)
    #print(secret_number)
    return (secret_number)


def get_guess_from_user():
  secret_number = 0
  while secret_number > difficulty*3 or secret_number <= 0 :
      try:
        secret_number = int(input(f"guess number between 1 to {difficulty*3}\n"))
        return (secret_number)
      except:
          print("You need to choose a number")
          pass

def compare_results():
    if generate_number() == get_guess_from_user():
        return (1)
    else:
        return (0)


def play():
    print("#################Welcome to Guess Game#########################")
    if compare_results() == 1:
        print("congratulations you won it's", True)
    else:
        print("Hooo it's wrong!",False)



















