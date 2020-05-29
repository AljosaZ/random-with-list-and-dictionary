import random
import json
import datetime
from operator import itemgetter


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    ordered_score_list = sorted(score_list, key=itemgetter("attempts"))


def get_top_scores():
    for score_dict in ordered_score_list[:3]:
        print(
            f'The user {score_dict.get("user")} has needed {score_dict.get("attempts")} attempts, at level {score_dict.get("level")}. The wrong guesses were {score_dict.get("wrong_guesses")}, the solution was number {score_dict.get("solution")} date: {score_dict.get("date")}'
        )


def play_game(level):
    wrong_guesses_list = []
    attempts = 0
    secret = random.randint(1, 30)

    if level != "easy" and level != "hard":
        print("Please enter valid value.")
    elif level == "easy":
        user = input("Please enter your name: ")
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                print(
                    "You've guessed it - congratulations! It's number "
                    + str(secret)
                    + ", your previoues guesses were "
                    + str(wrong_guesses_list)
                )
                print("Attempts needed: " + str(attempts))

                score_list.append(
                    {
                        "attempts": attempts,
                        "date": str(datetime.datetime.now()),
                        "user": user,
                        "wrong_guesses": wrong_guesses_list,
                        "solution": secret,
                        "level": level,
                    }
                )

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")

            wrong_guesses_list.append(guess)

    else:
        user = input("Please enter your name: ")
        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                print(
                    "You've guessed it - congratulations! It's number "
                    + str(secret)
                    + ", your previoues guesses were "
                    + str(wrong_guesses_list)
                )
                print("Attempts needed: " + str(attempts))

                score_list.append(
                    {
                        "attempts": attempts,
                        "date": str(datetime.datetime.now()),
                        "user": user,
                        "wrong_guesses": wrong_guesses_list,
                        "solution": secret,
                        "level": level,
                    }
                )

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                break
            else:
                print("Your guess is not correct!")

            wrong_guesses_list.append(guess)


while True:
    selection = input(
        'To play the game enter "A", to get top scores enter "B", to quit enter any other character: '
    )

    if selection == "A":
        difficulty = input(
            'To play in easy mode enter "easy". To play in hard mode enter "hard": '
        )
        play_game(difficulty)
    elif selection == "B":
        get_top_scores()
    else:
        break
