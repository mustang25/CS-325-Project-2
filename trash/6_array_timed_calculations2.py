#!/usr/bin/env python3
import time
# from algo3_changedp import changedp
from algo2_change_greedy import changegreedy


with open('array_timing.txt', 'w') as file_out:
    test_array = list(range(10000, 10200 + 1))
    coins = [1, 5, 10, 25, 50]
    file_out.write("Timing Question 3\n")
    for change in test_array:
        start_time = time.time()
        result = changegreedy(coins, change)
        execution_time = time.time() - start_time
        file_out.write("{}\t{}\n".format(change, execution_time))

    file_out.write("\n")
    coins = [1, 2, 6, 12, 24, 48, 60]
    coins2 = [1, 6, 13, 37, 150]
    test_array = list(range(10000, 10200 + 1))
    file_out.write("Timing Question 4 Part 1 & 2\n")
    for change in test_array:
        start_time = time.time()
        result = changegreedy(coins, change)
        execution_time = time.time() - start_time
        start_time2 = time.time()
        result2 = changegreedy(coins2, change)
        execution_time2 = time.time() - start_time2
        file_out.write("{}\t{}\t{}\n".format(change, execution_time, execution_time2))

    file_out.write("\n")
    coins = [1] + list(range(2, 31, 2))
    file_out.write("Timing Question 5\n")
    for change in test_array:
        start_time = time.time()
        result = changegreedy(coins, change)
        execution_time = time.time() - start_time
        file_out.write("{}\t{}\n".format(change, execution_time))




