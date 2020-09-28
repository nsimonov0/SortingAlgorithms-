def bubblesort(arr):
	for i in range(len(arr)-1):
		for j in range(0, len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1],arr[j]

arr = [1,66,23,7,33,99,80,808,22,4]
print(arr)
bubblesort(arr)
print(arr)