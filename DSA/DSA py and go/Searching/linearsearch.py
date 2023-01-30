def linear_serch(A,key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1

A = [10,11,21,60,50,40,90,85,65,40]
found = linear_serch(A,40)
print("result : ",found)