# Function go here

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
    print('''You'll be given a random multiplication question between 1-20 ( * = multiply ), try answer as many as you can within a minute.
    Choose either a number of rounds or press <enter> for
    infinite mode.



    ***good luck!*** ''')

    return""
# Main Routine goes here
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")