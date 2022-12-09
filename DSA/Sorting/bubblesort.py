def Bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
            # print(A)
            
A = [3,5,8,9,6,2]
print("Original list : ",A)
B = Bubble_sort(A)
print("***********************")
print("Sorted list : ",A)
