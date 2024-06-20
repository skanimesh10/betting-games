import random

mines_you_want = int(input("How many mines do you want? between 1 to 24: "))

mines = []
diamonds = []
while True:
    if mines_you_want <= 24:
        mine = random.randint(1, 25)
        if mine not in mines:
            mines.append(mine)

        if len(mines) == mines_you_want:
            break
    else:
        print("Invalid input")
        break

while True:

    want_to_play = input("Want to play? y/n: ").lower()
    if want_to_play == "y":
        your_number = int(input("What is your number? "))
        if your_number not in mines:
            if your_number not in diamonds:
                diamonds.append(your_number)
            else:
                print("Already selected")
        else:
            sorted_mines = sorted(mines)
            sorted_diamonds = sorted(diamonds)
            print("bomb")
            print("you loose")
            print(f"Mines are place in {sorted_mines}, and rest are diamonds.")
            print(f"You have opened diamonds in {sorted_diamonds} places.")
            break
    elif want_to_play == "n":
        sorted_mines = sorted(mines)
        sorted_diamonds = sorted(diamonds)
        print(f"Mines are place in {sorted_mines}")
        print(f"You have opened diamonds in {sorted_diamonds} places.")
        break

    else:
        print("Write correct syntax")