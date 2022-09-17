def leaders_in_array(arr, length):

    l  = []
    l.append(arr[length-1])
    leader = arr[length -1]
    for i in range(length-2,-1,-1):
        if arr[i] > leader:
            leader = arr[i]
            l.append(arr[i])

    return l

arr = [7, 6, 4, 5, 0, 1 ]
l = leaders_in_array(arr,len(arr))
if len(l) == 0:
    print("There are no leaders in array")
else:
    for i in l:
        print(i)


