import random
import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

def get_money_interval(difficulty):
    response = requests.get(url)
    exchange_rates = response.json()
    exchange_rate = exchange_rates['rates']['ILS']
    money_value = random.randint(1, 100)
    lower_bound = money_value - (5 - difficulty)
    upper_bound = money_value + (5 - difficulty)
    return lower_bound * exchange_rate, upper_bound * exchange_rate

def get_guess_from_user():
    guess: int = int(input("Enter your guess for the value in ILS: "))
    return guess

def play():
    difficulty = 5
    money_interval = get_money_interval(int(difficulty))
    print(f"The value in USD is between {money_interval[0]} and {money_interval[1]}")
    user_guess = get_guess_from_user()

    if money_interval[0] <= user_guess <= money_interval[1]:
        print("You won!")
        return True
    else:
        print("Sorry, you lost!")
        return False

play()