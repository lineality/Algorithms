#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


### GGA

# base case: non positive number:
# - is negative numbers...
# - or zero...
#
# zero is the good base case (stop here)
# and add that to list of solutions
# or just incriment a solutions counter
#
# negative is the bad base case
# no solution here: end process


def recursive_keep_checking(total, minus_denomination, successful_solutions_counter):

    cache_Denomination_1 = {0: 1}
    cache_Denomination_2 = {0: 1}
    cache_Denomination_3 = {0: 1}

    # main operation 1:
    # subtract the denomination from the total
    total = total - minus_denomination

    # there are 3 options:
    # - more than zero
    # - zero
    # - less than zero

    # terminate cycle if number is negative (less than zero)
    if total < 0:
        pass

    # if zero, success!! increment successful_solutions_counter
    elif total == 0:

        # print("new total = 0, new solution was found!")
        successful_solutions_counter += 1

    # if total is positive, try subtracting
    # all possible other denominations
    else:
        n = total
        # 1. subtract denomination 1

        # 1 Cache
        # If answer is in cache:
        # Then get it from cache
        if n in cache_Denomination_1:
            successful_solutions_counter = cache_Denomination_1[n]
        # If not in cache:
        # Then calculate it
        else:
            cache_Denomination_1[
                n
            ] = successful_solutions_counter = recursive_keep_checking(
                total, 1, successful_solutions_counter
            )
            successful_solutions_counter = cache_Denomination_1[n]

        # 2 Cache
        # If answer is in cache:
        # Then get it from cach
        if n in cache_Denomination_2:
            successful_solutions_counter = cache_Denomination_2[n]
        # If not in cache:
        # Then calculate it
        else:
            cache_Denomination_2[
                n
            ] = successful_solutions_counter = recursive_keep_checking(
                total, 2, successful_solutions_counter
            )
            successful_solutions_counter = cache_Denomination_2[n]

        # 3 Cache
        # If answer is in cache:
        # Then get it from cach
        if n in cache_Denomination_3:
            successful_solutions_counter = cache_Denomination_3[n]
        # If not in cache:
        # Then calculate it
        else:
            cache_Denomination_3[
                n
            ] = successful_solutions_counter = recursive_keep_checking(
                total, 3, successful_solutions_counter
            )
            successful_solutions_counter = cache_Denomination_3[n]

    return successful_solutions_counter


def eating_cookies(total_amount, cache=None):

    # start out solutions_counter at zero
    successful_solutions_counter = 0

    # solutions counter gets updated
    # by running recursive_keep_checking() function
    # solutions_list2.append(recursive_keep_checking(total_amount, 0, successful_solutions_counter))
    successful_solutions_counter = recursive_keep_checking(
        total_amount, 0, successful_solutions_counter
    )

    # print("final solutions_list", successful_solutions_counter)
    return successful_solutions_counter


eating_cookies(99)


eating_cookies(10)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")
