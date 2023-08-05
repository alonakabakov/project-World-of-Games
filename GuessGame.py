import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        guess = int(input(f"Guess a number between 1 and {difficulty}: "))
        if 1 <= guess <= difficulty:
            return guess
        else:
            print(f"Please enter a number between 1 and {difficulty}.")


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(guess, secret_number):
        print(" You guessed the secret number.")
        return True
    else:
        print("Sorry, you didn't guess the secret number.")
        return False


play(5)
