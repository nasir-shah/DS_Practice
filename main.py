def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while(j>0 and arr[j] < arr[j-1]):
            temp=arr[j]
            arr[j]=arr[j-1]
            arr[j-1] = temp
            j-=1

    return(arr)

print(insertion_sort([2,4,3,5,3,56,78,32,56,789,453,33,4,56,0,8,23,45,-1,-22,33,5,465,234,5,67,8,-90]))
print("it is now done")