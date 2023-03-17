# l = [1,2,3,5,1,3,8,6,8] #[1,3,8]
# l1 = []

# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# {1:2, 2:1, 3:2, 5:1, 8:2, 6:1}

# l = [1,2,3,5,1,3,8,6,8]
# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

# import time

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i <= j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for j in range(1,n):
#         if (i+j) <= (n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
        
# start_time = time.time()
# while time.time() - start_time < 7200:
#     pass

# def traffic(a):
#     def signals():
#         print("RED: STOP")
#         a()
#         print("GREEN: GO")
#     return signals

# @traffic
# def yellow():
#     print("YELLOW: SLOW DOWN")

# yellow()

# l = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

# l1 = sorted(l,key=lambda x: x[-1])
# print(l)
# print(l1)


import calendar

# def saturday(month, year):
#     l = []
#     c = calendar.monthcalendar(year, month)
#     for week in c:
#         if week[calendar.SATURDAY] != 0:
#             l.append(week[calendar.SATURDAY])
#     return l

# print(saturday(3,2023))



month = int(input())
year = int(input())

l = []
c = calendar.monthcalendar(year, month)
for week in c:
    if week[calendar.SATURDAY] != 0:
        l.append(week[calendar.SATURDAY])

print(l)
