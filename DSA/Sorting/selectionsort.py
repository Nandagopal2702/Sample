def selection_sort(A):
    n = len(A)
    for i in range(0,n-1):
        position = i
        for j in range(i+1,n):
            if A[j] < A[position]:     # ('<' = assending order) ('>' = dessending order)
                position = j
            # print(A)
        # temp = A[i]
        # A[i] = A[position]
        # A[position] = temp
        A[i],A[position] = A[position],A[i]

A = [3,5,8,9,6,2]
print("original list : ",A)
S = selection_sort(A)
print("*********************")
print("Sorted list : ",A)