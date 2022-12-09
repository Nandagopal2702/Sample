def Merge_sort(A,left,right):
    if left < right:
        mid = (left+right) // 2
        Merge_sort(A,left,mid)
        Merge_sort(A,mid+1,right)
        Merge(A,left,mid,right)
        

def Merge(A,left,mid,right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right+1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1
    for x in range(left,right+1):
        A[x] = B[x]
    
    # print(A)

A = [5,8,9,6,3,4,8,7,2,1,5,2]
print("Original_list",A)
Merge_sort(A,0,len(A)-1)
print("Sorted_list",A)