def quickSort(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)

def partition(A,p,r):
    x=A[r] # element wyznaczajacy podział
    i=p-1
    for j in range (p, r+1):
        if A[j]<=x :
            i=i+1
            A[i], A[j] = A[j], A[i]
    if i<r :
        return i
    else:
        return i-1

A=[2,8,7,6,2,4,5]
print('tablica początkowa: ', A)
quickSort(A, 0, len(A))
print('tablica posortowana: ', A)