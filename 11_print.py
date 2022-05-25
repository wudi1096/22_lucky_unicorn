def statement_generator(statement, decoration):

    side = decoration * 3

    statement = "{} {} {}".format(side, statement, side)
    top_bottom = decoration * len(statement)\

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""
statement_generator("Welcome to my game","*")
print()
statement_generator("you have got a unicorn","!")
