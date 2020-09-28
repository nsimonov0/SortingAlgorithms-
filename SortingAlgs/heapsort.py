def get_parent(i):
	return (i-1)//2

def get_left(i):
	return 2*i + 1

def get_right(i):
	return 2*i + 2

def make_heap(arr, n , i):
	#largest = i
	left = get_left(n)
	right = get_right(n)

	if (left < i and arr[left] > arr[n]):
		largest = left
	else:
		largest = n

	if (right < i and arr[right] > arr[largest]):
		largest = right

	if (largest != n):
		arr[largest], arr[n] = arr[n], arr[largest]
		make_heap(arr, largest, i)

def heap_sort(arr):
	start = get_parent(len(arr)-1)
	while start >= 0:
		make_heap(arr, n = start, i = len(arr))
		start = start - 1

	for i in range((len(arr) - 1), 0, -1):
		arr[0],arr[i] = arr[i], arr[0]
		make_heap(arr, n =0, i=i)

arr = [1, 12, 9, 5, 6, 10,88,2,64,54,22,2,79,101,34]
print(arr)
heap_sort(arr)
print(arr)

