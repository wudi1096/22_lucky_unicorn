import random

start_balance = 100

balance = start_balance
for item in range(10):
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

    print()
    print("Your you got a {} . "
          "Your balance is ${:.2f}".format(chosen,balance))

