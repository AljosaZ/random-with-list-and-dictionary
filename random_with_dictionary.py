import random
import json
import datetime
from operator import itemgetter

secret = random.randint(1, 30)
attempts = 0
user = input("Please enter your name: ")
{"attempts": attempts, "date": datetime.datetime.now(), "user": user}


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    ordered_score_list = sorted(score_list, key=itemgetter("attempts"))

    for score_dict in ordered_score_list:
        print(f'The user {score_dict["user"]} has needed {score_dict["attempts"]} attempts, date: {score_dict.get("date")}')

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_list.append(
            {"attempts": attempts, "date": str(datetime.datetime.now()), "user": user}
        )

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")