import math
import random
import sys
from timeit import default_timer as timer
sys.setrecursionlimit(100000000)


def quickSort_normal(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort_normal(A,p,q)
        quickSort_normal(A,q+1,r)

def quickSort_edycja(A, p, r):
    if r-p+1>5:
         q = partition(A,p,r)
         quickSort_edycja(A,p,q)
         quickSort_edycja(A,q+1,r)
    else:
        sortowaniebabelkowe(A, p, r)



def sortowaniebabelkowe(A, poczatek, koniec):
    for i in range (poczatek, koniec+1):
        for j in range(poczatek, koniec+1):
            if A[j]>A[i]:
                A[i], A[j]=A[j], A[i]
    return A

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


def macierzlosowa(rozmiar):
    lista = []
    for _ in range(rozmiar):
        lista.append(random.randint(0, 1000))
    return lista


# A=[2,8,7,6,2,4,5]
# A=[7,4,1,10,6,9,12,5]
# print('tablica początkowa: ', A)

# quickSort_normal(A, 0, len(A)-1)
# sortowaniebabelkowe(A, 0, len(A)-1)

# quickSort_edycja(A, 0, len(A)-1)
# print('tablica posortowana: ', A)

print("porównanie czasu dla danych losowych")
nn=[ 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
for n in nn:
    A=macierzlosowa(n)
    B=A
    start = timer()
    quickSort_normal(A, 0, len(A)-1)
    stop=timer()
    czas_qs=stop-start
    start2=timer()
    quickSort_edycja(B, 0, len(B)-1)
    stop2=timer()
    czas_ed=stop2-start2
    print('dla ', n, 'liczb qs_normalny: ', czas_qs)
    print('dla ', n, 'liczb qs_edytowany: ', czas_ed)




#dla zadania 3.4 c miedzy 5 a 10

