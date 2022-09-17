#string = str(input("Enter any word to check for palindrome\n"))
string = "amma"
print(len(string))
length = len(string)-1

i = 0
flag = 0
while i < len(string)-1:
    if string[i] != string[length]:
        flag = 1
    i += 1
    length -= 1

if flag == 1:
    print("String is not palindrome")
else:
    print("String is palindrome")
