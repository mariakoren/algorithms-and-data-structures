import math
from timeit import default_timer as timer


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


nn = [2000, 4000, 8000, 16000, 32000]

print("f1")
for n in nn:
    start = timer()
    f1(n)
    stop = timer()
    Tn = stop - start
    Fn = n
    print(n, Tn, Fn / Tn)

print("f2")
for n in nn:
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop - start
    Fn = n*n
    print(n, Tn, Fn / Tn)

print("f3")
for n in nn:
    start = timer()
    f3(n)
    stop = timer()
    Tn = stop - start
    Fn=n*n
    print(n, Tn, Fn / Tn)

print("f4")
for n in nn:
    start = timer()
    f4(n)
    stop = timer()
    Tn = stop - start
    Fn=n*math.log(n,2)
    print(n, Tn, Fn / Tn)

print("f5")
for n in nn:
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn=math.log(n,2)
    print(n, Tn, Fn / Tn)

# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n


# wyniki:
# f1
# 2000 0.00011309999999999792 17683465.959328353
# 4000 0.00018519999999999995 21598272.13822895
# 8000 0.0003808000000000006 21008403.361344505
# 16000 0.0008324000000000005 19221528.11148485
# 32000 0.001539299999999997 20788670.1747548
# f2
# 2000 0.1942963 20587113.59917816
# 4000 0.741622 21574333.01601085
# 8000 2.8987318 22078620.726484593
# 16000 11.5493718 22165707.74871063
# 32000 46.1480477 22189454.398089305
# f3
# 2000 0.08948620000000318 44699629.66356665
# 4000 0.3605666999999997 44374591.44174993
# 8000 1.4487567000000041 44175809.50617852
# 16000 5.77074189999999 44361713.69923864
# 32000 23.04617019999999 44432545.23912179
# f4
# 2000 0.0015050000000087493 14572470.81009746
# 4000 0.003293700000000399 14531723.33201037
# 8000 0.007353800000004185 14105125.823008196
# 16000 0.015869199999997363 14080895.606245466
# 32000 0.033783599999992475 14175667.990068953
# f5
# 2000 1.499999996212864e-06 7310522.874898687
# 4000 1.1999999998124622e-06 9971486.905443432
# 8000 1.1999999998124622e-06 10804820.238907
# 16000 1.1000000057492798e-06 12696167.465152971
# 32000 1.1999999998124622e-06 12471486.905834135