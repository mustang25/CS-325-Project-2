#!/usr/bin/env python3
#John Blakey

#Implementation of the second variation of the divide and conquer method 
#described in project 2 

def changeslow(source_list, value):
	answer_list = [0] * len(source_list)
		
	return changeslowHelper(source_list, value, answer_list)
    

def changeslowHelper(source_list, value, answer_list):
	if value == 0:
		#Base case: return value = 0 
		return coins, value, answer_list

	result = value

	#Start with the first coin and recursively call changeslowHelper to find minimum
	#iterate thourgh all the coin values
	for i in range(0, len(coins)):

		#Hold temporary values for answer_list
		temp_list = answer_list[:]

		if coins[i] <= value:
			#Increment the coin location in the answer_array by one
			temp_list[i] += 1
			print('temp_list after adding one', temp_list)
			temp_result = changeslowHelper(coins, value - coins[i], answer_list)
			
			#Test for best results, temp_result[1] is value
			if temp_result[1] + 1 < result:
				result = temp_result[1] + 1
				#Copy values of temp_list to answer_list for current best result
				answer_list = temp_list[:]
				print('answer_list after adding one', answer_list)

	return coins, result, answer_list

#main test

coins = [1, 3, 7, 12]
#coins = [2, 3]


answer = changeslow(coins, 29)

print (answer[2], answer[1])

#Expected result = [0, 1, 2, 1] 4