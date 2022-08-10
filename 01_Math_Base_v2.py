import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("'Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    integer_1 = random.randint(1,10)
    integer_2 = random.randint(1,10)


    # Generate question
    print("What is {} * {} = ".format(integer_1, integer_2))
    total = integer_1 * integer_2

    # User input

    users_answer = int(input("your answer: "))

    # check users answer

    if users_answer == total:
        print("Nice, you got it right! ")
    else:
        print("Sorry, you got it wrong.")