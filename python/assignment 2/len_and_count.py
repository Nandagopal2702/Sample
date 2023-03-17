""" Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]
find the difference between the length of the list and the count of unique elements in the list. """


list_1 = [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]

dict = {}
for i in list_1:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
count = 0
l = []
for i,j in dict.items():
    if j == 1:
        count += 1
        l.append(i)
print(l)
print(count)

