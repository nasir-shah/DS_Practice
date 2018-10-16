''' 
This module contains basic funtions that are used as helpers in other modules
'''
def find_smallest(sub):
    temp = sub[0]
    #temp=min(sub)
    for i in sub[1:]:
        if(temp > i):
            temp = i
    return temp


def swap_num(sub,n):
    i = sub.index(n)
    sub[i] = sub[0]
    sub [0] = n
    return sub