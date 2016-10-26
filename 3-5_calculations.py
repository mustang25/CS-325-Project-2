#!/usr/bin/env python3

from algo3_changedp import changedp

test_array = list(range(2010, 2200 + 1, 10))

print(test_array)

with open('calculations.txt', 'w') as file_out:
    coins = [1, 5, 10, 25, 50]
    file_out.write("Coin Values Question 3\n")
    for change in test_array:
        result = changedp(coins, change)
        file_out.write("{}\t{}\n".format(change, result[1]))

    file_out.write("\n")
    coins = [1, 2, 6, 12, 24, 48, 60]
    coins2 = [1, 6, 13, 37, 150]
    test_array = list(range(2000, 2200 + 1, 1))
    file_out.write("Coin Values Question 4 Part 1 & 2\n")
    for change in test_array:
        result = changedp(coins, change)
        result2 = changedp(coins2, change)
        file_out.write("{} {} {}\n".format(change, result[1], result2[1]))

    file_out.write("\n")
    coins = [1] + list(range(2, 31, 2))
    file_out.write("Coin Values Question 5\n")
    for change in test_array:
        result = changedp(coins, change)
        file_out.write("{} {}\n".format(change, result[1]))




