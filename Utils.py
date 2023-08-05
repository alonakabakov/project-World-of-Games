import os

score_file = "Scores.txt"

BAD_RETURN_CODE = -1

def Screen_cleaner():
    if os.name == "nt":
        os.system("cls")
    else:

        os.system("clear")

Screen_cleaner()