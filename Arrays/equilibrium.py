def equil_mem(l):
    left_sum = l[0]
    total = sum(l)
    right_sum = 0
    for ele in range(1,len(l)):
        right_sum = total - left_sum - l[ele]
        if left_sum == right_sum:
            return l[ele]
        left_sum = left_sum + l[ele] #5

    return -1


l = [1,4,2,3,2]
ele = equil_mem(l)
if ele == -1:
    print("There is no equil point")
else:
    print("equilbrium element is", ele)