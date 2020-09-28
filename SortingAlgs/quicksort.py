from random import randint

#Implementation of three-way partioning to handle duplicates
def partition(arr, start, end):
	pivot = arr[start] #Set the pivot value 
	div1 = start #Divide the array to check for elements equal to the pivot value
	for i in range(start+1, end+1): #Group all pivot values to the start of the array
		if arr[i] == pivot:
			div1+=1
			arr[i], arr[div1] = arr[div1], arr[i]
	div2 = div1 #Divide the array to check for elements less than the pivot value
	for i in range(div1+1, end+1): #Group values less than the pivot to the left
		if arr[i] < pivot:
			div2+=1
			arr[i], arr[div2] = arr[div2], arr[i]
	end = (div2-start)//2 #Switch position of values less than the pivot and values equal to the pivot
	for i in range(0 , end+1):
		arr[start+i], arr[div2-i] = arr[div2-i],arr[start+i]
	pivot1 = start + (div2-div1)
	pivot2 = pivot1 + (div1-start)

	return pivot1, pivot2

def quick_sort(arr, start, end):
	if (start < end):
		k = randint(start, end)
		arr[start], arr[k] = arr[k], arr[start]
		pivot1, pivot2 = partition(arr, start, end)
		quick_sort(arr, start, pivot1-1)
		quick_sort(arr, pivot2+1, end)

def sort_array(arr):
	start = 0 
	end = len(arr)-1
	quick_sort(arr,start,end)

intArray = [43,14,75,43,87,3,2,74,31,22,45,32,65,25,45,36,7,436,22,44,44,4,98,54,77,2,66]
sort_array(intArray) 
print(intArray)

