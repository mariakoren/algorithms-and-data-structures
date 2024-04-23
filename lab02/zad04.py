plik_wejscie=open('wejscie.txt', 'r')
plik_wyjscie=open('wyjscie.txt', 'w')
plik_wyjscie_iteracja=open('wyjscie_iteracja.txt', 'w')

def heapify(A, heapSize, i):
      l = 2*i+1 # lewy syn
      r = 2*i+2 # prawy syn
      if l < heapSize and A[l] > A[i]:
          largest = l
      else:
          largest = i
      if r < heapSize and A[r] > A[largest]:
          largest = r
      if largest != i:
          A[i], A[largest] = A[largest], A[i]
          heapify(A, heapSize, largest)
      return A

def buildHeap(A):
      heapSize = len(A)
      k = int((len(A)-2)/2) # ojciec ostatniego
      # węzła
      for i in range(k, -1, -1):
          heapify(A, heapSize, i)
      return A



def heapSort(A):
     A = buildHeap(A)
     heapSize = len(A)
     for i in range(len(A)-1, 0, -1):
          A[0], A[heapSize-1] = A[heapSize-1], A[0]
          heapSize -= 1
          heapify(A,heapSize,0)
     return A


#iteracyjna funkcja heapify
def heapify_iteracja(A, heapSize, i):
    largest = i
    while True:
        l = 2 * i + 1
        r = 2 * i + 2

        if l < heapSize and A[l] > A[largest]:
            largest = l

        if r < heapSize and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break

#funkcja buildHeap wywolująca iteracyjny heapify
def buildHeap_i(A):
    heapSize = len(A)
    k = int((len(A) - 2) / 2)  # ojciec ostatniego
    # węzła
    for i in range(k, -1, -1):
        heapify_iteracja(A, heapSize, i)
    return A


def heapSort_i(A):
    A = buildHeap(A)
    heapSize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[heapSize - 1] = A[heapSize - 1], A[0]
        heapSize -= 1
        heapify_iteracja(A, heapSize, 0)
    return A

tmp=plik_wejscie.read()
lista=tmp.split('\n')

lista_liczb=[]

for element in lista:
    lista_liczb.append(int(element))

print("lista wejscie: ", lista_liczb)

lista_wyjscie=heapSort(lista_liczb)

lista_wyjscie_iteracja=heapSort_i(lista_liczb)

for element in lista_wyjscie:
     plik_wyjscie.write(str(element)+'\n')

for element in lista_wyjscie_iteracja:
    plik_wyjscie_iteracja.write(str(element)+'\n')

print('wyjscie z rekurencyjnym heapify: ', lista_wyjscie)
print('wyjscie z iteracyjnym heapify: ', lista_wyjscie_iteracja)

plik_wejscie.close()
plik_wyjscie.close()


