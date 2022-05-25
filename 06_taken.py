import random

tokens = ["zebra", "horse", "donkey", "unicorn"]
balance = 100

for item in range (0,20):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4

    elif chosen == "donky":
        balance -= 1

    else:
        balance -= 0.5

    print("token is {} , Balance is {}".format(chosen,balance))
