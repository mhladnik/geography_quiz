countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}

def game():
    correct = 0
    wrong = 0
    score_list = list()

    name = input("What is your name?")
    print(f"Okaj {name} lets play simple geography quiz where a you have to guess the capital city of following countries. ")
    for key,value in countries_cities.items():
        guess = input("What is the capital city of " + key + "?")
        if guess.upper() == value.upper():
            print("This is correct!")
            correct += 1
        else:
            print("Sorry, wrong answer.")
            wrong += 1
    score_list.append({"name": name, "correct answers": correct, "wrong answers": wrong})
    print(f"{name} you guessed right for {correct} times and wrong for {wrong} times.")

game()



