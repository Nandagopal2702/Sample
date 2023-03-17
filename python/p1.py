# def count_distinct_outcomes(x):
#     if x < 1:
#         return 0
#     elif x == 1:
#         return 6
#     else:
#         distinct_outcomes = 6
#         for i in range(1, x):
#             distinct_outcomes *= 6 - (i + 1)
#         return distinct_outcomes

# x = 2
# distinct_outcomes = count_distinct_outcomes(x)
# print(distinct_outcomes)


string = "hello world"
res = ""
for i in string:
    res = i + res
print(res)