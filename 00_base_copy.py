import random
play_round = 0

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
    statement_generator("game instruction", "^")
    print()
    return""

prinz_decoration = "*"
played_before = yes_no("Have you played this game before?")
statement_generator(played_before, prinz_decoration)

if played_before =="no":
    instructions()

error = "Please enter a number between 0 and 10"

valid = False
while not valid:
    response = int(input("How much would you like to play with? "))

    if 0 < response <= 10:
        valid = True

    else:
        print(error)

balance = response
play_again = input("press <Enter> to start").lower()
while play_again == "":
    play_round += 1

    statement_generator("Round #{}".format(play_round),"*")

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

    if balance < 1:
        play_again = "xxx"
        print("You have run out of money")

    else:
        play_again = input("Press <Enter> to play again "
                               "or" " 'XXX' to quit")

        out_come = "you have got a {}. your balance is "\
                 "${:.2f}".format(chosen, balance)
    statement_generator(out_come, prinz_decoration)

statement_generator("You have got ${:.2f}".format(balance),"&")
