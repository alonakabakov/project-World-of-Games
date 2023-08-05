import os

def POINTS_OF_WINNING(difficulty):
    return (difficulty * 3) + 5

def add_score(difficulty):
    try:
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                current_score = int(file.read())

        points_won = POINTS_OF_WINNING(difficulty)

        current_score += points_won

        with open("scores.txt", "w") as file:
            file.write(str(current_score))

        return current_score

    except Exception as e:
        print(f"Error: {e}")
        return None

difficulty = 5
current_score = add_score(difficulty)
print(f"Your current score is: {current_score}")

add_score(difficulty)