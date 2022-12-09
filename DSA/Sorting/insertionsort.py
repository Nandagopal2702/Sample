def Insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position -= 1
        A[position] = cvalue

A = [3,5,8,9,6,2]
print("original list : ",A)
I = Insertion_sort(A)
print("**********************")
print("Sorted list : ",A)