# n= 18
# no of guess = 9
# print no of guess left
# print no of guess he took to finish
# game over



n=18
no_of_guesses = 1
print("no of guess is limited to only 5 times")
while(no_of_guesses<=5):
    guess_no = int(input("Guess the no: \n"))
    if guess_no<18:
        print("you Entered less no: plz enter greater number")
    elif guess_no>18:
        print("you Entered a greater no: enter a less number")
    else:
        print("you won!")
        print(no_of_guesses,"no of guess he took to finish")
        break
    print(5-no_of_guesses,"no. of guesses left")
    no_of_guesses = no_of_guesses + 1

if no_of_guesses>5:
    print("Game Over") 