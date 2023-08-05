from Score import add_score

def welcome(name) :
   return f"Hello {name} and welcome to the World of Games (WoG).\n" \
        "Here you can find many cool games to play."
print(welcome("guy"))

def load_game() :
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to\n"
          "  guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    choice = input("Please choose a game (1-3): ")

    while True:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        if difficulty and 1 <= int(difficulty) <= 5:
            break
        print("Please choose a number between 1 and 5.")

    if choice == "1":
        from MemoryGame import play
        play(int(difficulty))
    elif choice == "2":
        from GuessGame import play
        play(int(difficulty))
    elif choice == "3":
        from CurrencyRouletteGame import play
        play(int(difficulty))
    else:
        print("Invalid input. Please choose a number between 1 and 3.")


load_game()


#
