# Function go here
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


# Main routine goe here
how_much = num_check(" whats the final answer ? ", 0, 20)

print("Program continues")