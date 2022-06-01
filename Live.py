
choose = 0
choose2 = 3




def welcome(name):
    return (f'Hello, {name} and welcome to the World of Game(WOG)')

def load_game():
    choose = 5
    while choose > 3 or choose == 0:
        try:
            choose = int(input("Please choose a game to play : \n"
            "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
            "2. Guess Game - guess a number and see if you chose like the computer \n"
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"))
        except:
            pass



    choose2 = 6
    while choose2<1 or choose2>5:
        try:
            choose2 = int(input("Please choose game difficulty from 1 to 5:"))
        except:
            pass


    if(choose == 1):
        from MemoryGame import play
        play()


    if(choose == 2):
        from GuessGame import play
        play()

    if(choose == 3):
        from CurrencyRouletteGame import play
        play()

















    # print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    # print("2. Guess Game - guess a number and see if you chose like the computer")
    # print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    # input("Please choose game difficulty from 1 to 5:")