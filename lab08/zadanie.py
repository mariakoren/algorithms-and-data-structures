def lcsLength(x, y):
    m = len(x)
    n = len(y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[" "] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "\\"
            else:
                if c[i - 1][j] > c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "|"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "-"

    return c, b


def printLCS(x, b, i, j):
    if i == 0 or j == 0:
        return ""
    if b[i][j] == "\\":
        return printLCS(x, b, i - 1, j - 1) + x[i - 1]
    elif b[i][j] == "|":
        return printLCS(x, b, i - 1, j)
    else:
        return printLCS(x, b, i, j - 1)

def printArrays(x, y, c, b):
    m = len(c) - 1
    n = len(c[0]) - 1

    print("     ", end=" ")
    for j in range(n):
        print(y[j]+" ", end=" ")
    print()

    for i in range(m + 1):
        if (i>0):
            print(x[i-1]+" ", end =" ")
        else:
            print("  ", end =" ")
        for j in range(n + 1):
            print(str(c[i][j])+b[i][j], end=" ")
        print()

def przyklad_zad1(x, y):
    c, b = lcsLength(x, y)
    lcs = printLCS(x, b, len(x), len(y))
    print("ZADANIE 1")
    print("słowo x: ", x)
    print("słowo y: ", y)
    print("Długość najdłuższego wspólnego podciągu:", c[len(x)][len(y)])
    print("Najdłuższy wspólny podciąg:", lcs)
    printArrays(x, y, c, b)

def lcsLengthW(x, y):
    m = len(x)
    n = len(y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[" "] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "\\"
            else:
                if c[i - 1][j] > c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "|"
                elif c[i][j - 1] > c[i - 1][j]:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "-"
                else:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "|-"

    return c, b


def findLCSW(x, b, i, j):
    if i == 0 or j == 0:
        return set([""])
    if b[i][j] == "\\":
        lcs_set = findLCSW(x, b, i - 1, j - 1)
        return set([lcs + x[i - 1] for lcs in lcs_set])
    elif b[i][j] == "|":
        return findLCSW(x, b, i - 1, j)
    elif b[i][j] == "-":
        return findLCSW(x, b, i, j - 1)
    else:
        lcs_set = set()
        if b[i][j].find("|") != -1:
            lcs_set |= findLCSW(x, b, i - 1, j)
        if b[i][j].find("-") != -1:
            lcs_set |= findLCSW(x, b, i, j - 1)
        return lcs_set


def printArraysW(x, y, c, b):
    m = len(c) - 1
    n = len(c[0]) - 1

    print("      ", end=" ")
    for j in range(n):
        print(y[j] + "  ", end=" ")
    print()

    for i in range(m + 1):
        if (i > 0):
            print(x[i - 1] + " ", end=" ")
        else:
            print("  ", end=" ")
        for j in range(n + 1):
            if(b[i][j]=="|-"):
                print(str(c[i][j]) + b[i][j], end=" ")
            else:
                print(str(c[i][j]) + b[i][j], end="  ")
        print()

def przyklad_zad2(x, y):
    c, b = lcsLengthW(x, y)
    lcs_list = findLCSW(x, b, len(x), len(y))
    print("ZADANIE 2")
    print("Długość najdłuższego wspólnego podciągu:", c[len(x)][len(y)])
    print("Najdłuższe wspólne podciągi:")
    for lcs in lcs_list:
        print(lcs)
    printArraysW(x, y, c, b)

# x="abrakadabra"
# y="labrador"
# nwp = abradr


# x="aabbabacacab"
# y="abababcccaba"
# zad1: ababaccab
#zad2: ababaccab abbabccab aababccab

# x="aababaacc"
# y="abacab"

x="katarakta"
y="traktor"
# zad1: abac
# zad2: abab aaab abaa abac

przyklad_zad1(x, y)
przyklad_zad2(x, y)
