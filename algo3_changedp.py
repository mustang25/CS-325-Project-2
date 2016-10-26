#!/usr/bin/env python3

"""Algorithm that uses dynamic programming to determine the least amount of coins needed to make change.

The following sources were used while developing the algorithm:
http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
https://www.youtube.com/watch?v=rdI94aW6IWw
"""


def changegreedy(denominations, amount):
    """An algorithm that calculates the least amount of coins needed to create the change amount.

    Argument:
        denominations       -- A list of all possible coin denominations.
        amount              -- An integer value for the total amount of change that needs to be made.
    """
    # Three lists are initialized to hold values of the least amount of coins needed, the last value used,
    # and the final count for each denomination used to make the change.
    coin_count = [0]
    last_used = [0]
    final_coin_count = [0 for _ in denominations]

    # Base case to check if amount is 0 or if denominations doesn't contain any values.
    if amount == 0 or denominations is None:
        return final_coin_count, 0

    # For loop that checks calculates change for each amount up to the total amount.
    for total_change in range(1, amount + 1):
        last_coin = denominations[0]
        total_coins = total_change

        # Check to see how many coins are needed for each denomination value. Since the list of
        # denominations is sorted, we can break out of the loop once the denomination > total_change.
        for value in denominations:
            if value > total_change:
                break
            if 1 + coin_count[total_change - value] < total_coins:
                total_coins = 1 + coin_count[total_change - value]
                last_coin = value

        # Append coin_count and last_used to the lists.
        coin_count.append(total_coins)
        last_used.append(last_coin)

    # Calculate the total for each denomination value
    remaining_change = amount

    while remaining_change > 0:
        value = last_used[remaining_change]
        value_index = denominations.index(value)
        final_coin_count[value_index] += 1
        remaining_change -= value

    return final_coin_count, coin_count[amount]


if __name__ == '__main__':
    print(changegreedy([1, 2, 4, 8], 15))
    print(changegreedy([1, 3, 7, 12], 29))
    print(changegreedy([1, 3, 7, 12], 31))
    print(changegreedy([3, 4, 5], 3))
    print(changegreedy([1, 3, 7, 26], 22))
