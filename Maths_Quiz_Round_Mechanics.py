# Function used to check if input is valid


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      " or an integer that is more than 0\n"

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                #start of loop
                if response < 1:
                    print(round_error)
                    continue

                else:
                    return response

            except ValueError:
                print(round_error)

        if response == "":
            return response


# Main routine goes here....

rounds_played = 0
choose_instructions = "You'll be given a random multiplication question between 1-20, ( * = multiply by )" \
                      "try answer as many as you can within a minute."
# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                   "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to "
                   "end: ".format(choose_instructions))

    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of loop / game *****
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# Put end of game content here
print ("Thank You for playing")




