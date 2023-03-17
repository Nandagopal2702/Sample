""" Write a program to replace duplicate adjacent alphabets from given string with '_'.
For Example -- input given string : 'abcdaa hssbbye' and output : 'abcda_ hs_b_ye' """

# String = input()
# String_2 = list(String)
# for i in String_2:
#     if String_2.count(i) > 1:
#         i.replace(i,"_")
# print(String_2)
    
String_1 = input()
res = []
str = ""
for i in String_1:
    if i == str:
        res.append("_")
    else:
        res.append(i)
        str = i
    new_str = " ".join(res)

print(new_str)



    
        

