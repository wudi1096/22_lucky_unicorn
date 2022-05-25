
play_game = "don't know"
while play_game != "yes" or play_game != "y":

    play_game = input("Have you play this game before?").lower()

    if play_game == "yes" or play_game == "y":
        print("program runs")
        break

    elif play_game == "no" or play_game == "n":
        print(" instruction ")
        break

    else:
        print("please enter yes or no")
