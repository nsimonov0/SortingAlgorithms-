def counting_sort(arr):
	max_val = max(arr) + 1
	count_arr = [0] * max_val
	for i in arr:
		count_arr[i] +=1
	j = 0
	for i in range(0, max_val):
		temp = count_arr[i]
		count_arr[i] = j
		j += temp
	result = [None] * len(arr)
	for i in arr:
		result[count_arr[i]] = i
		count_arr[i] += 1
	return result



arr = [2,5,2,7,4,7,9,6,326]
print(counting_sort(arr))


