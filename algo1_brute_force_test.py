#!/usr/bin/env python3
#John Blakey

def changeslow(array, amount):
	array_size = len(array) - 1
	coin_count = 0
	answer_array = [0] * len(array)

	for i in range(array_size, -1, -1):
		answer_array[i] = 0
		single_coin_count = amount // array[i]

		if single_coin_count > 0 and amount > 0:
			coin_count += single_coin_count
			amount -= single_coin_count * array[i]
			answer_array[i] = single_coin_count

	return answer_array, coin_count		

#main
amount = int(input('Input integer for amount to test the algorithm: '))

array = [1, 3, 7, 26]	# test array with 22 amount

result = changeslow(array, amount)

print(result[0], result[1])

# expected output in file: Algorithm changeslow

#[1, 2, 5]
#10
#[1, 3, 7, 26]
#22
#Answers
#[0, 0, 2]
#2
#[1, 0, 3, 0]
#4