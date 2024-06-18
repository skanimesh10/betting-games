import random

# simple up and down programme.
# dice = ["up", "down"]
# your_choice = input("What is your choice??Up or Down: ")
# computer_gave = random.choice(dice)
# print(computer_gave)
# if your_choice.lower() == computer_gave:
#     print("You Win")
# else:
#     print("You Lose")

your_bet_amount = int(input("What is your BET amount?: "))
over_or_under = input("What do you want to do? (over or under): ").lower()
your_number = int(input("For over or under choose a number between (2 to 98)?: "))


def for_roll_over():
    global your_bet_amount
    global your_number
    computer_gave = int(random.choice(range(2, 99)))
    if computer_gave >= your_number:
        win_chance_percentage = 100 - your_number
        implied_probability = win_chance_percentage / 100
        initial_multiplier = 1 / implied_probability
        # house edge is 1% of the initial multiplier.
        multiplier_after_house_edge = round((initial_multiplier - (initial_multiplier * 0.01)), 4)
        print(f"Multiplier is {multiplier_after_house_edge}x")
        print(f"Number is {computer_gave}")
        print(f"YOU WIN, you will get {round(your_bet_amount * multiplier_after_house_edge, 2)}")
    else:
        print(f"Number is {computer_gave}")
        print("You loose all the bet amount")


def for_roll_under():
    global your_number
    computer_gave = int(random.choice(range(2, 99)))
    if computer_gave <= your_number:
        implied_probability = your_number / 100
        initial_multiplier = 1 / implied_probability
        # house edge is 1% of the initial multiplier.
        multiplier_after_house_edge = round((initial_multiplier - (initial_multiplier * 0.01)), 4)
        print(f"Multiplier is {multiplier_after_house_edge}x")
        print(f"Number is {computer_gave}")
        print(f"YOU WIN, you will get {round(your_bet_amount * multiplier_after_house_edge, 2)}")
    else:
        print(f"Number is {computer_gave}")
        print("You loose all the bet amount")


if over_or_under == "over":
    for_roll_over()
elif over_or_under == "under":
    for_roll_under()
else:
    print("Choose correct syntax")
