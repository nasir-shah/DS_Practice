arr = [[0,5],[2,5],[3,9],[10,11],[12,15],[15,20],[16,19]]

marker = arr[0]
length = 0
for i in range(1, len(arr)):
    start = arr[i][0]
    end = arr[i][1]
    if(start <= marker[1]):
        if(end > marker[1]):
            marker[1] = end;
            
    else:
        length += marker[1] - marker[0] + 1
        marker[0] = start
        marker[1] = end
length += marker[1] - marker[0] + 1

print("Length : ", length)