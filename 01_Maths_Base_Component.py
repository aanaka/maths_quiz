import random


# Functions go here

def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")
            print()


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print('''You'll be given a random multiplication question between 1-20 ( * = multiply by ), try answer as many as you
    can .
    Choose either a number of rounds or press <enter> for
    infinite mode.
    - insert number of rounds or ' Enter ' for continuous mode.
    - xxx to quit




    ***good luck!*** ''')
def num_check(question, low, high):

    error = "Please enter an whole number between 1 and 20\n"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response


def int_check(question, low=None, high=None, exit_code=None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here

statement_generator ("welcome to the multiplication maths quiz", "=")
print()

played_before = yes_no("Have you played the game before? ")


if played_before == "no":
    instructions()

play_again = input("Press <Enter> to play").lower()

game_summary = []

rounds_played = 0

rounds_won = 0
rounds_lost = 0


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of the Game Play Loop
    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1 )

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    # Rounds Heading


    integer_1 = random.randint(1,10)
    integer_2 = random.randint(1,10)


    # Generate question
    print("What is {} * {} = ".format(integer_1, integer_2))
    total = integer_1 * integer_2

    # User input

    users_answer = int_check("Answer (or xxx to quit): ", 1, exit_code="xxx")
    if users_answer == "xxx":
        break
    # check users answer

    if users_answer == total:
        statement_generator("Nice, you got it right!", "+")
        rounds_won += 1
    else:
        statement_generator ("Sorry, you got it wrong", "-")
        rounds_lost += 1

        if rounds_played == rounds:
            break

# end game if requested # of questions has been played
    outcome = "Question {}: Right Answers - {}".format(rounds_played + 1, total)

    # Outputs results...
    game_summary.append(outcome)
    # print(statement_generator)

    rounds_played += 1
    # end game if requested # of questions has been played
    if rounds_played == rounds:
        break

questions_won = rounds_played - rounds_lost

print()
print('***** End Game Summary *****')
print("Right: {} \t|\t Wrong: {}".format(rounds_won, rounds_lost ))
print()

# Ask user if they want to see game summary

rounds = input("Please press <enter> to see your game summary.... ")

# **** Calculate Game Stats ******
print()
print("**** Game History *******")
for game in game_summary:
    print(game)

print()

# display game stats with $ values to the nearest whole number
print("******* Game Statistics ********")
print("Wrong: {} \nRight: {}".format(rounds_won, rounds_lost))
print()
statement_generator("Thank You for playing", "!")