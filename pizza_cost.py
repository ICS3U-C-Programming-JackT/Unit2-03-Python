#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 19, 2025

# This program calculates the cost of a pizza and
# rounds it to 2 decimal places


import constants


def main():
    diameter = float(
        input("Enter the diameter of your pizza (inches): ")
    )  # get diameter from user

    # Calculate price of pizza based on diameter
    subtotal = (
        constants.LABOUR_COST
        + constants.RENTAL_COST
        + constants.INGREDIENT_COST * diameter
    )  # subtotal cost
    tax = subtotal * constants.HST  # tax
    total = tax + subtotal  # total cost

    # print out total cost with message
    print("The total cost of your pizza will be {:,.2f}".format(total) + "$")


if __name__ == "__main__":
    main()  # start main function
