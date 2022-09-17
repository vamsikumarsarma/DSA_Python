string  = "Kubernetes uses Go and Python"
pos = (int(input("enter number"))) -1

new_str = ""

"""
for i in range(len(string)):
    if i!= pos:
        new_str = new_str+string[i]
        
print("new string is", new_str)


"""

#alternate method:

new_str = string[:pos] + string[pos+1:]
print("new string is", new_str)