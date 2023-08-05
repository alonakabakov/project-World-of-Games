import random
import time



def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for x in range(difficulty)]
    return sequence


def get_list_from_user(difficulty):
    user_list = []
    for X in range(difficulty):
        number = int(input("Enter a number: "))
        user_list.append(number)
    return user_list

def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

def play(difficulty):
    difficulty = random.randint(1, 5)
    sequence = generate_sequence(difficulty)
    time.sleep(0.7)
    print("Now try to recall the numbers.")
    user_list = get_list_from_user(difficulty)
    result = is_list_equal(sequence, user_list)
    if result:
        print(" You won!")
    else:
        print("Sorry, you lost.")

def clear_screen():
        print("\033[H\033[J")


clear_screen()
play(1)
