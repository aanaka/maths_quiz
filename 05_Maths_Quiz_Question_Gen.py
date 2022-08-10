import random

for item in range (1, 4):
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


