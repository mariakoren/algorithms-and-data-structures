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
