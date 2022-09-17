#Check if a given string can be derived from another string by circularly rotating it.
# The rotation can be in a clockwise or anti-clockwise rotation.
x = "ABCD"
y = "DABC"

flag = 0
if len(x) != len(y):
    print("Strings are not derivable")

for i in range(len(x)):

    x= x[1:] + x[0]
    if x == y:
        flag = 1
        break


if flag == 1:
    print("String is derivable")
else:
    print("String is not derivable")
