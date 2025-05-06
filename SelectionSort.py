def selectionSort(arr):
	for i in range(len(arr)):
		min = i+1
        for j in range(min,len(arr)):
            if arr[i]>arr[j]:
            	arr[i],arr[j] = arr[j],arr[i]
    return arr
    
#print(selectionSort([89,56,45,34,65,76]))

num=int(input("Enter Total number used in sorting:"))
for i in range(0,num):
	arr[i]=add(int(input("Enter NO you want Sort:")))
