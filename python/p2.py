# l = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]
# d = {}

# for i in l:
#     if i % 2 == 0:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1

# print(d)


# def swap_elements(l,a1,a2):
#     if a1 >= len(l) or a2 >= len(l):
#         return "No swap"
#     else:
#         l[a1],l[a2] = l[a2],l[a1]
#     return l

# l = [1,2,3,4,5,6,7,8]
# print(swap_elements(l,4,6))

# match = 'version'
# input = 'Upgraded_image_version_8.0.4.3'
# if match in input:
#    print('YES')
# else:
#    print('NO')

# Match = 'version'
# input = 8
# print(Match + "_" + str(input))

# def number(x):
#     for i in range(x):
#         yield i
      
# range = number(3)
# print(next(range))
# print(next(range))
# print(next(range))


# a = int(input())
# b = int(input())
# mul = 0
# for i in range(b):#abs
#     mul += a
# if (a<0 and b>0) or (a>0 and b<0):
#     print(-mul)
# else:
#     print(mul)


# s = input()
# s1 = ""
# c = {}
# for i in s:
#     if i.isalpha():
#         if i in c:
#             c[i] += 1
#         else:
#             c[i] = 1
# for i in s:
#     if i.isalpha() and i in c:
#         s1 += i + str(c[i])
#         del c[i]
# print(s1)

