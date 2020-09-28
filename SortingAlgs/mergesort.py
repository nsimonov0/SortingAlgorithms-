def mergesort(arr):
	if len(arr)>1: 
		middle = len(arr)//2
		left_half, right_half = arr[:middle], arr[middle:]
		mergesort(left_half)
		mergesort(right_half)
		left_end, right_end = len(left_half), len(right_half)
		i,j,k = 0,0,0
		while (i < left_end and j < right_end):
			if left_half[i] > right_half[j]:
				arr[k] = right_half[j]
				j+=1
			else:
				arr[k] = left_half[i]
				i+=1
			k += 1
		while (i < left_end):
			arr[k] = left_half[i]
			i +=1
			k +=1
		while (j < right_end):
			arr[k] = right_half[j]
			j +=1
			k +=1



myArray = [2,5,2,7,4,7,9,6,326,235,93,64,38,256,35]
print(myArray)
mergesort(myArray)
print(myArray)
