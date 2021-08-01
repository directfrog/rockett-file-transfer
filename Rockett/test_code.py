arr = [['Baked apples', 4, 'randomness'], ['Baked beans', 64, 'randomness'], ['Baked owoes', 21, 'randomness']]
copy_arr = arr.copy()
sorted_arr = []

import random

for x in copy_arr:
	print(arr)
	smallest = arr[0]
	for compare in arr:
		if compare[1] < smallest[1]:
			smallest = compare
	sorted_arr.append(smallest)
	arr.pop(arr.index(smallest))


print('SORTED: ', sorted_arr)

