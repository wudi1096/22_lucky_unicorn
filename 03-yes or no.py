
def yes_no(something):
    valid = False
    while not valid:
        play_game = input(something).lower()

        if play_game == "yes" or play_game == "y":
            print("program runs")
            return play_game

        elif play_game == "no" or play_game == "n":
            print(" instruction ")
            return play_game

        else:
            print("please enter yes or no")


game_answer = yes_no("Have you played this game before? ")
print("your answer is {}.".format(game_answer))
