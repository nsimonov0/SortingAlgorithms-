def selection_sort(arr):
	for i in range(len(arr)):
		min_num_index = i
		for j in range(i+1, len(arr)):
			if arr[min_num_index] > arr[j]:
				min_num_index = j
		arr[i], arr[min_num_index] = arr[min_num_index], arr[i]


arr = [1,7,24,68,33,2,99,20]
arr2 = [3, 1, 41, 59, 26, 53, 59]

print(arr2)
selection_sort(arr2)
print(arr2)
