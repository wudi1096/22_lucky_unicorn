import random

balance = 5
play_round = 0

play_again = input("press <Enter> to start").lower()
while play_again == "":
    play_round += 1

    print("*** Round #{} ***".format(play_round))

    chosen_number = random.randint(1, 100)

    if 1 <= chosen_number <= 10:
        chosen = "unicorn"
        balance += 4

    elif 11 <= chosen_number <= 38:
        chosen = "donky"
        balance -= 1

    else:
        if chosen_number % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    if balance < 1:
        play_again = "xxx"
        print("You have run out of money")

    else:
        print("you have got a {} "
              "you balance ${:.2f}".format(chosen, balance))
        play_again = input("Press <Enter> to play again "
                               "or" " 'XXX' to quit")

print("total balance {}".format(balance))

