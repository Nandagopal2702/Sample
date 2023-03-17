""" Write a python function with name reverse_vowel that takes one string as an argument and 
    reverse the order of vowels present in the string. 
    The function should return the string having reversed order of vowels. 
    For example - If the input string which is given as argument is 'Hello' then the output string 
    should be'Holle'. You need to reverse the vowel irrespective of lowercase or uppercase."""


def reverse_vowel(String):
    vowels = 'aeiouAEIOU'
    v = []
    for i in String:
        if i in vowels:
            v.append(i)
    rev = v[::-1]
    result = ''
    i = 0
    for j in String:
        if j in vowels:
            result += rev[i]
            i += 1
        else:
            result += j
    return result

s = input()
a = reverse_vowel(s)
print(a)


# def reverse_vowel(String):
#     idx = []
#     val = []
#     # list_1 = list(String)
#     for i in String:
#         if i in "aeiouAEIOU":
#            val.append(i)
#     val_2 = val[::-1]
#     res = ""
#     i = 0
#     for i in String:
#         if i in "aeiouAEIOU":
#             res += val_2[i]
#             i += 1
#         else:
#             res += i
#     print(res)

# reverse_vowel("Nandu")

# l = [0,1,2,3]
# v = ['a','b','c','d']
# l1 = []
# l1.insert(l[0],v[0])
# l.remove(l[0])
# v.remove(v[0])
# l1.insert(l[0],v[0])

# print(l1)
# s = "Nandu"
# l = list(s)
# l.insert(2,'NN')
# print(l)

# def reverse_vowel(String):
#     value = []
#     for i in String:
#         if i in "aeiouAEIOU":
#             value.append(i)
#     rev = value[::-1]
#     result = ""
#     i = 0
#     for i in String:
#         if i in "aeiouAEIOU":
#             result += rev[i]
#             i += 1
#         else:
#             result += i
#     return result

# a = reverse_vowel("Nandu")
# print(a)
