from Live import *
import random as rd
from currency_converter import CurrencyConverter

c = CurrencyConverter()
Currency = c.convert(1,'USD', 'ILS')
Currency = round(Currency, 3)
difficulty = choose2

def get_money_interval():
    dollar = rd.randint(100, 500)
    return dollar

def get_guess_from_user():

    try:
       guess = 1
       while guess <= 1:
            guess = int(input(f"Guess how much money you have after currency to {get_money_interval()} USD to Shekels?"))
    except:
         pass
    return guess

def play():
    interval = 8
    interval = interval - difficulty
    result = get_money_interval()*Currency - get_guess_from_user()
    if result <= interval:
        print(True)
    else:
        print(False)












