#from permutation import permutation

def bubble_sort( arr):
    swap_count = 0
    for i in range(1, len(arr)):
        j = 1
        while(arr[j] < arr[j-1]):
            swap_count+=1
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            if(j < len(arr)-1):
                j = j+1
            else:
                break
        
    print("Total no. of swaps: ",swap_count)
    return arr

