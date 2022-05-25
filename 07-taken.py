import random

tokens = ["zebra", "horse", "donkey", "unicorn",
          "zebra", "zebra", "horse", "horse",  "donkey",
          "zebra"]
start_balance = 100

balance = start_balance
for item in range (1000):
    chosen = random.choice(tokens)


    if chosen == "unicorn":
        balance += 4

    elif chosen == "donky":
        balance -= 1

    else:
        balance -= 0.5


print()
print("your start Balance is ${:.2f}".format(start_balance))
print("your final balance is ${:.2f}".format(balance))
