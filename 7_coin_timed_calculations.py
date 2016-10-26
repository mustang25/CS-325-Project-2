#!/usr/bin/env python3
import time
from algo3_changedp import changegreedy


with open('coin_timing.txt', 'w') as file_out:

    file_out.write("Timing by number of coins\n")
    for i in range(2, 102):
        change = 10000
        coins = list(range(1, i))
        start_time = time.time()
        result = changegreedy(coins, change)
        execution_time = time.time() - start_time
        file_out.write("{} {}\n".format(len(coins), execution_time))
