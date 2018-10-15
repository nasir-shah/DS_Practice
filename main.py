'''
This is the main file it contains all the imports and calls other modules to compute the result::
'''
import math 
from itertools import permutations , combinations
#from bubble_sort import bubble_sort
from Selection_Sort import selection_sort

###########################################################################################################
''' Reading data raw data from the externael file '''
data = []
with open('data_set.txt','r') as f:
    rawData = [line.strip().split(',') for line in f]
    for datum in rawData:
        data = data + datum

for i in range(data.count('')):
    data.remove('')
    
data = list(map(int , data))
############################################################################################################

print("Data to feed :\n", data)
print("Total values in the data:\n",len(data))

############################################################################################################

# Calling Selection Sort
print("Running Selection Sort")
print(selection_sort(data))

#############################################################################################################
