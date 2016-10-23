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