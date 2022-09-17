def same_arrays(arr1, arr2):

    if len(arr1) != len(arr2):
        return False
    
    arr = dict()

    for i in arr1:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1
    
    for i in arr2:
        if i not in arr or arr[i] == 0:
            return False
        else:
            arr[i] -= 1

    return True


arr1 = [3, 5, 2, 5, 2]
arr2 = [2, 3, 5, 5, 2]

if same_arrays(arr1, arr2):
    print("Two arrays are same")
else:
    print("Arrays are not same")