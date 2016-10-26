#!/usr/bin/env python3
#John Blakey
#Brute force recursive implementation
#Source: http://pythonfiddle.com/minimum-coin-brute-force/

def changeslow(source_list, value):
    # Call the function containing the brute force recursive algorithm
    answer_array = compute(source_list, value)
    
    # Calculate number of coins to return
    coin_count = 0
    for i in range(0, len(answer_array)):
        coin_count += answer_array[i]
    
    return answer_array, coin_count


def compute(source_list, value):
        temp_answer = [0] * len(source_list)
        temp_answer[0] = value
        
        # Call compute recursively to calculate the minimum 
        for i in [j for j in source_list if j <= value]:
            temp_result = compute(source_list, value - i)
            temp_result[source_list.index(i)] += 1

            temp_answer_sum = 0
            for i in range(0, len(temp_answer)):
                temp_answer_sum += temp_answer[i]

            temp_result_sum = 0
            for i in range(0, len(temp_result)):
                temp_result_sum += temp_result[i]

            # Calculate the best option and copy it to the answer
            if temp_answer_sum > temp_result_sum:
                temp_answer = temp_result

        return temp_answer
    

#print (changeslow([1, 3, 7, 12], 29))