# imports
import random

# functions
def statement_generator(statement, decoration):

    side = decoration * 3

    statement = "{} {} {}".format(side, statement, side)
    top_bottom = decoration * len(statement)\

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""

def yes_no(something):
    valid = False
    while not valid:
        play_game = input(something).lower()

        if play_game == "yes" or play_game == "y":
            return play_game

        elif play_game == "no" or play_game == "n":
            print(" instruction ")
            return play_game

        else:
            print("please enter yes or no")
    return""

def instructions():
    statement_generator(" How to play ", "*")
    print()
    statement_generator("Each team will cost you 1$"
                        "and you have to push Enter to start your game"
                        "if you got unicorn you win 5$ "
                        "if is zebra or horse lose 0.5$"
                        "if is a donkey you lose 1$", "^")
    print()
    statement_generator("When you want to leave your game type XXX", "^")
    return""

def num_check(question):
    error = "Please enter a number between 0 and 10"
    valid = False
    while not valid:
        try:
            response = int(input(question))

            if 0 < response <= 10:
                valid = True
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine
# initalise  variables
play_round = 0

# ask user if played before
played_before = yes_no("Have you played this game before? ")

# if no display instructions
if played_before == "no":
    instructions()

# ask user how much they want to play with
how_much = num_check("How much would you like to play with? ")

balance = how_much

play_again = input("press <Enter> to start").lower()

# tracks rounds played
while play_again == "":
    play_round += 1
    statement_generator("Round #{}".format(play_round),"*")

    # selects token/ calculates balance
    chosen_number = random.randint(1, 100)

    if 1 <= chosen_number <= 10:
        chosen = "unicorn"
        prinz_decoration = "!"
        balance += 4

    elif 11 <= chosen_number <= 38:
        chosen = "donkey"
        prinz_decoration = "D"
        balance -= 1

    else:
        if chosen_number % 2 == 0:
            chosen = "horse"
            prinz_decoration ="H"

        else:
            chosen = "zebra"
            prinz_decoration ="Z"
        balance -= 0.5

    # displays output to user
    outcome = "you have got a {}. your balance is ${:.2f}".format(chosen, balance)
    statement_generator(outcome, prinz_decoration)

    if balance < 1:
        play_again = "xxx"
        statement_generator("You have run out of money", "~")

    else:
        play_again = input("Press <Enter> to play again or 'XXX' to quit")


