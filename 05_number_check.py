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

def instructions():
    print("*** How to play ***")
    print()
    print("game instruction")
    print()
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


played_before = yes_no("Have you played this game before?")

if played_before =="no":
    instructions()

how_much = num_check("How much would you like to play with? ")

print("you have start with {}$".format(how_much))
