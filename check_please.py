import math


def split_check(total,number_of_people):
    if number_of_people <= 1:
        raise ValueError("There must be at least 2 people to spilt total")
    return math.ceil(total / number_of_people)


while True:
    try:
        total_due = float(input("What is the total? "))
        if total_due <= 0:
            print("You need to enter a valid amount, Please try again...")
            break
        number_of_people = int(input("How many people? "))
        amount_due = split_check(total_due, number_of_people)
    except ValueError as err:
        print("Please Enter a valid value")
    else:
        print("Each person owes ${}".format(amount_due))
        break

