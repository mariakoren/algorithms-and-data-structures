plikdanych = open('dane.txt', 'r')
tmp=plikdanych.read()
dane=tmp.split('\n')
# print(dane)

def w(slowo, rozmiar):
    return hash(slowo)%rozmiar

def d(slowo,rozmiar):
    h = ord(slowo[-1])
    for litera in slowo[:-1]:
        h = h * 111 + ord(litera)
    return h%rozmiar

def s(slowo,rozmiar):
    if len(slowo) == 0:
        return 0
    return ord(slowo[0])%rozmiar





def pomiar(m, haszuj):
    T = [[] for _ in range(m)]
    n = 2 * m
    for i in range(n):
        slowo=dane[i]
        h = haszuj(slowo, m)
        T[h].append(slowo)

    if m == 17:
        print(T)

    # obliczenie ilości pustych list, maksymalnej długości listy i średniej długości niepustych list
    puste = sum(1 for x in T if len(x) == 0)
    dlugosc_max = max(len(x) for x in T)
    dlugosc_srednia = sum(len(x) for x in T if len(x) > 0) / (m - puste)

    # print("m = ", m)
    print("liczba pustych list: ",puste)
    print("maksymalna długość listy: ", dlugosc_max)
    print("średnia długość niepustych list: ",dlugosc_srednia,"\n")



# pomiary dla różnych wariantów
print("w17")
pomiar(17, w)
print("d17")
pomiar(17, d)
print("s17")
pomiar(17, s)

print("w1031")
pomiar(1031, w)
print("d1031")
pomiar(1031, d)
print("s1031")
pomiar(1031, s)

print("w1024")
pomiar(1024, w)
print("d1024")
pomiar(1024, d)
print("s1024")
pomiar(1024, s)

# wyniki działania
# w17
# [['options', 'linked'], ['most', 'both'], ['Only', 'accepts', 'which', 'may'], ['project', 'remain', 'mostly'], [], ['here', 'symbolic'], ['and', 'are', 'der', 'links', 'named'], ['below', 'changed'], ['the', 'for'], ['useful', 'see'], ['GCC', 'Apple', 'like'], ['listed'], ['compiler', 'actually'], ['gcc'], ['version'], ['same'], ['GNU']]
# liczba pustych list:  1
# maksymalna długość listy:  5
# średnia długość niepustych list:  2.125
#
# d17
# [['named'], ['gcc', 'see', 'remain', 'der', 'linked'], ['version'], ['GNU', 'mostly', 'changed'], ['most'], ['and', 'are', 'both'], ['links'], ['below'], [], ['useful'], ['project', 'options', 'accepts', 'like'], ['listed'], ['for', 'Apple'], ['GCC', 'compiler', 'Only', 'the', 'actually'], ['here', 'same', 'which'], [], ['symbolic', 'may']]
# liczba pustych list:  2
# maksymalna długość listy:  5
# średnia długość niepustych list:  2.2666666666666666
#
# s17
# [['for', 'which'], ['gcc'], ['here'], ['GCC', 'GNU'], [], [], ['listed', 'links', 'like', 'linked'], ['most', 'mostly', 'may'], ['named'], ['options'], ['project'], ['Only'], ['and', 'are', 'remain', 'accepts', 'actually'], ['see', 'below', 'same', 'both', 'symbolic'], ['compiler', 'the', 'Apple', 'changed'], ['useful', 'der'], ['version']]
# liczba pustych list:  2
# maksymalna długość listy:  5
# średnia długość niepustych list:  2.2666666666666666
#
# w1031
# liczba pustych list:  130
# maksymalna długość listy:  9
# średnia długość niepustych list:  2.2885682574916757
#
# d1031
# liczba pustych list:  135
# maksymalna długość listy:  7
# średnia długość niepustych list:  2.3013392857142856
#
# s1031
# liczba pustych list:  981
# maksymalna długość listy:  183
# średnia długość niepustych list:  41.24
#
# w1024
# liczba pustych list:  138
# maksymalna długość listy:  8
# średnia długość niepustych list:  2.311512415349887
#
# d1024
# liczba pustych list:  151
# maksymalna długość listy:  10
# średnia długość niepustych list:  2.345933562428408
#
# s1024
# liczba pustych list:  974
# maksymalna długość listy:  183
# średnia długość niepustych list:  40.96



# w1031 najlepsza