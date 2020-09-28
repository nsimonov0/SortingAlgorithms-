def insertion_sort(arr):
	for i in range(1, len(arr)):
		arr_value = arr[i]
		j = i
		
		while j > 0 and arr[j-1] > arr_value:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = arr_value

arr = [14,46,43,27,57,41,45,21,70]
print(arr)
insertion_sort(arr)
print(arr)
