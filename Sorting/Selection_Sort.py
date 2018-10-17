from time import time
from Sorting import helper_module
            
def selection_sort(arr):
    start = time()
    temp = []
    for i in range(len(arr) - 1):
        num = helper_module.find_smallest(arr[i:])
        tem = helper_module.swap_num(arr[i:],num)
        arr = arr[:i] + tem
    end = time()
    print("Elapsed time = ", end - start)
    return arr