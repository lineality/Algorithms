#!/usr/bin/python

# stock prices

import argparse

# def find_max_profit(prices):


#!/usr/bin/python

# stock prices

# despite the instructions: the goal here is to:
# find the maximum price difference
# between the smallest prior and largest later prices
# and return the largest such price difference

# possible steps
# 1. find the largest price after the first price
# 2. only look before that price
# 3. find the lowest earlier price

# or
# for each price (after the first)
# calculate the difference to all previous prices
# record that difference
# maybe using a dictionary
# find the highest difference
# output only that price difference
# so output the highest value in your differences-list

###########################

# e.g.
# prices = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]

# import library
import argparse

# function to:
# find the maximum price difference
# between the smallest prior and largest later prices
# return the largest such price difference
def find_max_profit(prices):

    # make variable
    # to store price differences
    price_differences_list = []

    # step 1
    # go through price data list
    # starting at second item
    # because first has no prior lower value
    for current_price_index in range(1, len(prices)):
        # print("ticker 1")
        # Step 2
        # append to price list the difference between the current-price
        # and each previous price
        countback_counter = current_price_index - 1
        difference = 0
        # until you reach the beginning of the list
        # print(current_price_index)
        # print(countback_counter)
        while countback_counter >= 0:
            # print("ticker 2")
            # print("current index", current_price_index)
            # print("counter", countback_counter)
            # and get the price difference
            # between the current price and each previous
            difference = prices[current_price_index] - prices[countback_counter]
            # print(difference)
            price_differences_list.append(difference)
            # print(price_differences_list)
            # count back
            countback_counter -= 1

    # return the lar
    return max(price_differences_list)


# find_max_profit(prices)


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )
