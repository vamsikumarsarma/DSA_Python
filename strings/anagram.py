#An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
str1 = input("Enter string1 \n")
str2 = input("Enter strign2 \n")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

"""
#This requires nlogn...since any comparision based sorting algorith takes nlogn
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("Two strings are Anagrams")
    else:
        print("Two strings are not anagrams")
else:
     print("Two strings are not anagrams")
"""

def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False

    ht =dict()

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

print(is_anagram(str1, str2))