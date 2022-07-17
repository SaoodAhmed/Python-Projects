import random
list = ["s", "w", "g"]


chance = 10
no_of_chance = 0
Human_point = 0
computer_point = 0

print("Water, Snake, Gun")
print(" s for snake \n w for water \n g for gun")

while no_of_chance<chance:
    _input = input("snake,water,gun: ")
    _random = random.choice(list)
    if _input == _random:
        print("Tie both 0 point to each\n")
    elif _input == "s" and _random == "w":
        Human_point = Human_point + 1
        print(f"""your guess{_input} and computer guess is {_random} \n""")
        print("you wins 1 point\n")
        print(f"your point is {Human_point} and cpmputer point is {computer_point}")
    elif _input=="w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random}")
        print("computer wins 1 point\n")
        print(f"your point is {Human_point} and computer point is {computer_point}")
    elif _input == "g" and _random == "s":
        Human_point = Human_point + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you wins 1 point \n")
        print(f"your point is {Human_point} and computer point is {computer_point}")
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"your point is {Human_point} and computer point is {_random}")
    elif _input == "w" and _random == "g":
        Human_point = Human_point + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you wins 1 point \n")
        print(f"your point is {Human_point} and computer point is {computer_point}")
    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"your point is {Human_point} and computer point is {_random}")
    else:
        print("you enter a wrong input\n")

    no_of_chance = no_of_chance+1
    print(f"{chance - no_of_chance} is left out of {chance}")
print("Game Over")


if computer_point == Human_point:
    print("Tie")
elif computer_point>Human_point:
    print("comuter win and you loss")
else:
    print("You win and computer loss")