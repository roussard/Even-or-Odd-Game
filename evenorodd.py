import random

print("This is the Even or Odd game,\n   Instructions:\n    Take turns guessing if the opponent is holding an even or odd amount of marbles.")

your_marbles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cpu_marbles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cpu_guess = ["even", "odd"]
cpu_hand = random.choice(cpu_marbles)
cpu_prediction = random.choice(cpu_guess)

print(cpu_hand)
print(cpu_prediction)

def round_odd():
    print("ROUND START")
    print("Guess:\nOpponent holding Even\nOR\nOpponent holding Odd")
    player_guess = input("Choose: ")
    if player_guess == "even" and cpu_hand == 2:
        print("You Win!")
    elif player_guess == "even" and cpu_hand == 4:
        print("You Win!")
    elif player_guess == "even" and cpu_hand == 6:
        print("You Win!")
    elif player_guess == "even" and cpu_hand == 8:
        print("You Win!")
    elif player_guess == "even" and cpu_hand == 10:
        print("You Win!")
    elif player_guess == "odd" and cpu_hand == 1:
        print("You Win!")
    elif player_guess == "odd" and cpu_hand == 3:
        print("You Win!")
    elif player_guess == "odd" and cpu_hand == 5:
        print("You Win!")
    elif player_guess == "odd" and cpu_hand == 7:
        print("You Win!")
    elif player_guess == "odd" and cpu_hand == 9:
        print("You Win!")
    else:
        print("You Lose!")

def round_even():
    print("Round Start")
    print("Decide how many marbles you will hold")
    player_hand = input("Enter a number from 1 through 10.")
    if player_hand == "1" and cpu_prediction == "odd":
        print("You Lose!")
    elif player_hand == "3" and cpu_prediction == "odd":
        print("You Lose!")
    elif player_hand == "5" and cpu_prediction == "odd":
        print("You Lose!")
    elif player_hand == "7" and cpu_prediction == "odd":
        print("You Lose!")
    elif player_hand == "9" and cpu_prediction == "odd":
        print("You Lose!")
    elif player_hand == "2" and cpu_prediction == "even":
        print("You Lose!")
    elif player_hand == "4" and cpu_prediction == "even":
        print("You Lose!")
    elif player_hand == "6" and cpu_prediction == "even":
        print("You Lose!")
    elif player_hand == "8" and cpu_prediction == "even":
        print("You Lose!")
    elif player_hand == "10" and cpu_prediction == "even":
        print("You Lose!")
    else:
        print("You Win!")

def continuegame():
    cont = input("Would you like to play again?\n(Y/N)")
    if cont == "y":
        game()
    else:
        return print("Thanks for playing.")

def game():
    round_odd()
    round_even()
    continuegame()

game()