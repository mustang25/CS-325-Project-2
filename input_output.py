#!/usr/bin/env python3
import sys
import re
# algo 1
from algo1_v2 import changeslow
# algo 2
from algo2_change_greedy import changegreedy
# algo 3
from algo3_changedp import changedp


input_list = []

if len(sys.argv) > 1:
    input_name = sys.argv[1]
    output_name = re.search(r'^\w+', input_name).group(0) + "change.txt"
    text_output = open(output_name, 'w')
else:
    input_name = 'Amount.txt'
    text_output = open('OutputChange.txt', 'w')


def write_results(r):
    """A method that writes results to an output file opened with text_output.

    Arguments:
        r   -- This is a tuple that contains a subarray and max sum.
    """
    text_output.writelines(str(r[0]) + '\n')
    text_output.write(str(r[1]) + '\n')

# This is currently set to open the text file given to us and read each line into an array that is
# stored in input_list. This input_list array has alternating elements of "answer" array and count
# integer 
with open(input_name, 'r') as text_input:
    for line in text_input:
        if line == '' or line == '\n':
            continue
        if line[0] == '[':
            line = line.strip('[\n').replace(',', '').replace(']', '')

        if line != '' and line is not None:
            array = [int(n) for n in line.split(' ')]
            input_list.append(array)

        elif line != '' and line is not None and line != '[':
            amount = int(line)
            input_list.append(amount)

# This iterates over the above array that we are testing and calls the appropriate function. The results
# are then written to a file called "Outputchange.txt".

text_output.write("Algorithm changeslow:\n")
for i in range(0, len(input_list), 2): 
    results = changeslow(input_list[i], input_list[i + 1][0])
    write_results(results)
text_output.write("\n")

text_output.write("Algorithm changegreedy:\n")
for i in range(0, len(input_list), 2):
    results = changegreedy(input_list[i], input_list[i + 1][0])
    write_results(results)
text_output.write("\n")

text_output.write("Algorithm changedp:\n")
for i in range(0, len(input_list), 2):
    results = changedp(input_list[i], input_list[i + 1][0])
    write_results(results)
text_output.write("\n")

text_output.close()
