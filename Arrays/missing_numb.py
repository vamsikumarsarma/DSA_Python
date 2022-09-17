def find_missing(arr):
    n = len(arr)
    total_sum = sum(arr)
    nat_sum = (n+1)*(n+2)/2
    return nat_sum - total_sum
l = [1,2,4,5]
print("Mising number is", int(find_missing(l)))