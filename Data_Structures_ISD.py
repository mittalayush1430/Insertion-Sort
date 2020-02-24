def insertion_sort(arr) :
    for i in range(1,len(arr)) :
        x = arr[i]
        j = i
        while x > arr[j-1] and j >0 :
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = x
num = int(input("Enter number of elements:"))
arr = []
for i in range(num):
    arr.append(int(input(f"Enter the element[{i+1}] of the array:")))
insertion_sort(arr)
print("Array in ascending order is: " + str(arr))
