M=[[1,1,1,0,1], [1,1,1,1,1], [1,1,1,1,0], [1,0,1,1,0], [1,1,1,1,1,]]
n=len(M)
def print_macierz(M):
    for x in M:
        print(x)

# def f1(n):
#     n=n-1
#     max=0
#     for x1 in range (0,n):
#         for y1 in range (0,n):
#             for x2 in range (n, x1-1, -1):
#                 for y2 in range (n, y1-1, -1):
#                     local_max=0
#                     for x in range (x1-1, x2):
#                         for y in range (y1-1, y2):
#                             local_max+=M[x][y]
#                     if local_max==(x2-x1+1)*(y2-y1+1) and local_max>max:
#                         max=local_max
#     return max

def f1(n, M):
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


def DYNAMICZNY(n, M):
    maks = 0
    #  utworz tablicę kwadratową MM rozmiaru n
    #  i wypełnij ją zerami
    MM = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(0, n):
        for x1 in range(0, n):
            iloczyn = 1
            for x2 in range(x1, n):
                iloczyn *= M[x2][y]
                MM[x1][x2] = iloczyn * (x2 - x1 + 1 + MM[x1][x2])
                if MM[x1][x2] > maks:
                    maks = MM[x1][x2]
    return maks


def CZULY(n, M):
    maks = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            x2 = x1
            ymaks = n - 1
            while (x2 < n) and (M[x2][y1] == 1):
                y2 = y1
                while (y2 < ymaks + 1) and (M[x2][y2] == 1):
                    y2 += 1
                ymaks = y2 - 1
                lokalMaks = (x2 - x1 + 1) * (ymaks - y1 + 1)
                if lokalMaks > maks:
                    maks = lokalMaks
                x2 += 1
    return maks


print_macierz(M)
print(f1(n, M))