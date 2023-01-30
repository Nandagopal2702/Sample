def Countsort(A):
    n = len(A)
    maxsize = max(A)
    Carray = [0] * (maxsize+1)
    for i in range(n):
        Carray[A[i]] += 1
    i = 0
    j = 0
    while i < maxsize+1:
        if Carray[i] > 0:
            A[j] = i
            j += 1
            Carray[i] -= 1
        else:
            i += 1

A = [3,5,3,8,8,9,6,2]
print("Original list",A)
Countsort(A)
print("Sorted list",A)