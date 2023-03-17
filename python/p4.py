# Given a list of first 10 natural numbers, write a program to find the square of all even numbers
# and cube of all odd numbers and store them in another list

# def fun(l):
#     l1 = []
#     for i in l:
#         if i % 2 == 0:
#             a = i**2
#             l1.append(a)
#         else:
#             b = i**3
#             l1.append(b)
#     return l1

# c = [1,2,3,4,5,6,7,8,9,10]
# print(fun(c))


# In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of
# lowercase and uppercase letters.

# s = "MsYs TecHNOlogiEs iS a gREat place To woRk"

# low = 0
# up = 0
# sp = 0
# for i in s:
#     if i.islower():
#         low += 1
#     elif i.isupper():
#         up += 1
#     elif i.isspace():
#         a= "".join(s)

# print(low)
# print(up)
# print(a)

# Given two lists --
# list_1 = [‘Msys’, ‘Tata’, ‘Wells’, ‘Mobinius’]
# list_2 = [‘Technologies’, ‘Power’, ‘Fargo’, ‘Technologies’]
# Write a python code using map and lambda function which will create the list named as my_list
# consisting of the combination of first name and second name from list_1 and list_2 respectively.
    

# list_1 = ['Msys', 'Tata', 'Wells', 'Mobinius']
# list_2 = ['Technologies', 'Power', 'Fargo', 'Technologies']

# my_list = list(map(lambda a,b: a+b, list_1,list_2))

# print(my_list)


# list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
# use the filter() function to find the list of numbers that are multiple of either 2 or 5.

# list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]

# list = list(filter(lambda a: a%2 == 0 or a%5 == 0, list_1))
# print(list)

s = "MsYs TecHNOlogiEs iS a gREat place To woRk"
a = s.replace(" ","")
print(a)


