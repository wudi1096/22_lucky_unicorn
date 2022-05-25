
balance = 5
play_round = 0

play_again = input("press <Enter> to start").lower()
while play_again == "":
    play_round += 1

    print(play_round)
    balance -= 1
    print("balance:", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("You have run out of money")

    else:
        play_again = input("Press <Enter> to play again "
                               "or" " 'XXX' to quit")

print("total balance {}".format(balance))

