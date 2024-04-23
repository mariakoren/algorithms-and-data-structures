import random
import math
from timeit import default_timer as timer

# M10 = [[0 for x in range(10)] for y in range(10)]
# for i in range(10):
#     for j in range(10):
#         M10[i][j] = random.randint(0, 1)
#
# M100 = [[0 for x in range(100)] for y in range(100)]
# for i in range(100):
#     for j in range(100):
#         M100[i][j] = random.randint(0, 1)
#
# M1000 = [[0 for x in range(1000)] for y in range(1000)]
# for i in range(100):
#     for j in range(100):
#         M1000[i][j] = random.randint(0, 1)

# M=[[1,0,1,0,1], [1,1,1,1,1], [1,1,1,1,0], [1,0,1,1,0], [1,1,1,1,1,]]
# n=len(M)



def print_macierz(M):
    for x in M:
        print(x)


def f1(M):
    n = len(M)
    maks = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(n - 1, x1 - 1, -1):
                for y2 in range(n - 1, y1 - 1, -1):
                    lokal_maks = 0
                    for x in range(x1, x2 + 1):
                        for y in range(y1, y2 + 1):
                            lokal_maks += M[x][y]
                    if lokal_maks == (x2 - x1 + 1) * (y2 - y1 + 1) and lokal_maks > maks:
                        maks = lokal_maks
    return maks


def f2(M):
    n = len(M)
    maks = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            x2 = x1 #for x2 in range(n - 1, x1 - 1, -1):
            ymaks = n - 1
            while (x2 < n) and (M[x2][y1] == 1):
                y2 = y1 #for x2 in range(n - 1, x1 - 1, -1):
                while (y2 < ymaks + 1) and (M[x2][y2] == 1):
                    y2 += 1
                ymaks = y2 - 1
                lokal_maks = (x2 - x1 + 1) * (ymaks - y1 + 1)
                if lokal_maks > maks:
                    maks = lokal_maks
                x2 += 1
    return maks


def macierz(n):
    M = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = random.randint(1, 1)
    return M


# print("macierz 10*10")
# print_macierz(M10)
# print(f2(M10))
#
# print("macierz 100*100")
# print_macierz(M100)
# print(f2(M100))
#
# print("macierz 1000*1000")
# print_macierz(M1000)
# print(f2(M1000))

nnn = [10,15,20,25,30,35,40]

# print("dla f1: ")
# for n in nnn:
#     M=macierz(n)
#     start = timer()
#     f1(M)
#     stop = timer()
#     Tn=stop-start
#     Fn=n**6
#     print(n, Tn, Fn/Tn)

# wynik:
# dla f1:
# 10 0.006504499935545027 153739720.17976624
# 15 0.05550700007006526 205210603.8089226
# 20 0.28690039995126426 223073930.92122447
# 25 0.8112236000597477 300953553.35078853
# 30 1.9389360999921337 375979383.7470753
# 35 4.657856900012121 394659102.77218187
# 40 10.445456699933857 392132208.0657265


nn = [10]
print("dla f2: ")
for n in nnn:
    M=macierz(n)
    start = timer()
    f2(M)
    stop = timer()
    Tn=stop-start
    Fn=n**4
    print(n, Tn, Fn/Tn)

#wynik:
# dla f2:
# 10 6.480002775788307e-05 1543209.2154904173
# 100 0.005158999934792519 1938360.1718153877
# 1000 0.5447466000914574 1835715.9087034417
