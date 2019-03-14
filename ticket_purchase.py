TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code until tickets run out.


while tickets_remaining >= 1:

    # Output how many tickets are remaining using the tickets_remaining variable

    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable.

    name = input("Hello, What is you'r name? ")

    # Prompt the user by name and ask how many tickets would they like.

    num_tickets = input("How many tickets would you like?, {}?".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Invalid Value, Please Try Again".format(err))
    else:
        # Calculate the price (number of the tickets multiplied by the price ) and then assign it as variable)
        amount_due = calculate_price(num_tickets)
        # Output the price to the screen.
        print("You'r total is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed? Y/N ")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyway {}".format(name))

# Notify user the tickets are sold out

print("Sorry tickets are SOLD OUT!")
