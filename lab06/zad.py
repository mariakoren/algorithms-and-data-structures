def d(slowo):
    wynik_haszowania=ord(slowo[-1])
    for litera in slowo:
        wynik_haszowania=wynik_haszowania*111+ord(litera)
    return wynik_haszowania

def h1(k, m):
    return k%m

def h2(k, m):
    return 1+(k%(m-2))

def h_liniowe(k,i,m):
    return (h1(k, m)+i)%m

def h_kwadratowe(k, i, m):
    return (h1(k, m)+i**2)%m

def h_dwukrotne(k, i, m):
    return(h1(k, m) +i*h2(k, m))%m

def read_primes(file_path):
    with open(file_path, "r") as f:
        primes = f.readlines()
    primes = [int(p) for p in primes[0].split()]
    return primes

primes = read_primes("pierwsze.txt")

plik = open("./nazwiska.txt", "r")

def czytanie(file):
    data=file.readlines()
    array=[]
    for el in data:
        tmp = el.split()
        array.append(make_obj(int(tmp[0]), tmp[1]))
    return array

def make_obj(ilosc, nazwisko):
    obj = {"il": ilosc, "n":nazwisko}
    return  obj

objects = czytanie(plik)

def wstaw_liniowe(tablica, element, m):
    k = d(element['n'])
    i = 0
    while i < m:
        index = h_liniowe(k, i, m)
        if tablica[index] is None:
            tablica[index] = element
            return i + 1  # Zwracamy ilość prób dla wstawienia elementu
        i += 1
    return -1  # Zwracamy -1, jeśli nie udało się wstawić elementu


def wstaw_kwadratowe(tablica, element, m):
    k = d(element['n'])
    i = 0
    while i < m:
        index = h_kwadratowe(k, i, m)
        if tablica[index] is None:
            tablica[index] = element
            return i+1 # Zwracamy ilość prób dla wstawienia elementu
        i += 1
    return -1  # Zwracamy -1, jeśli nie udało się wstawić elementu


def wstaw_dwukrotne(tablica, element, m):
    k = d(element['n'])
    i = 0
    while i < m:
        index = h_dwukrotne(k, i, m)
        if tablica[index] is None:
            tablica[index] = element
            return i+1  # Zwracamy ilość prób dla wstawienia elementu
        i += 1
    return -1  # Zwracamy -1, jeśli nie udało się wstawić elementu


def test(technika, m, zapelnienie, dane):
    tablica = [None] * m
    ilosc_prob = 0
    ilosc_wstawien = 0
    ilosc_elementow = int(m * zapelnienie)

    for element in dane[:ilosc_elementow]:
        ilosc = technika(tablica, element, m)
        ilosc_prob += ilosc
        ilosc_wstawien += 1

    srednia_prob = ilosc_prob /ilosc_wstawien

    if (m==7):
        for line in tablica:
            print(line)


    print(f'Technika haszowania: {technika.__name__}')
    print(f'Wielkość tablicy: {m}')
    print(f'Procent zapełnienia: {zapelnienie}')
    print(f'Średnia ilość prób wstawiania: {srednia_prob}')
    print()


test(wstaw_liniowe, 10000, 0.5, objects)  # Test dla techniki OL i wypełnienia 50%
test(wstaw_liniowe, 10000, 0.7, objects)
test(wstaw_liniowe, 10000, 0.9, objects)


test(wstaw_kwadratowe, 10000, 0.5, objects)  # Test dla techniki OK i wypełnienia 50%
test(wstaw_kwadratowe, 10000, 0.7, objects)
test(wstaw_kwadratowe, 10000, 0.9, objects)


test(wstaw_dwukrotne, 10000, 0.5, objects)  # Test dla techniki OD i wypełnienia 50%
test(wstaw_dwukrotne, 10000, 0.7, objects)
test(wstaw_dwukrotne, 10000, 0.9, objects)


# test(wstaw_liniowe, 7, 0.5, objects)  # Test dla techniki OL i wypełnienia 50%
# test(wstaw_liniowe, 7, 0.7, objects)
# test(wstaw_liniowe, 7, 0.9, objects)
#
#
# test(wstaw_kwadratowe, 7, 0.5, objects)  # Test dla techniki OK i wypełnienia 50%
# test(wstaw_kwadratowe, 7, 0.7, objects)
# test(wstaw_kwadratowe, 7, 0.9, objects)
# #
# #
# test(wstaw_dwukrotne, 7, 0.5, objects)  # Test dla techniki OD i wypełnienia 50%
# test(wstaw_dwukrotne, 7, 0.7, objects)
# test(wstaw_dwukrotne, 7, 0.9, objects)

#WYNIKI:
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.5174
#
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 2.305142857142857
#
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 5.409111111111111
#
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.4276
#
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 1.8424285714285715
#
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 2.813222222222222
#
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.4242
#
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 1.877
#
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 10000
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 5.221222222222222

#najlepiej działa haszowanie kwadratowe. Dla 50% tablicy wyniki lepiej



#dla 7 elementowej:
#
# None
# None
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.3333333333333333
#
# None
# None
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# {'il': 92945, 'n': 'Dabrowski'}
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 1.75
#
# {'il': 89366, 'n': 'Lewandowski'}
# {'il': 88932, 'n': 'Wojcik'}
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# {'il': 92945, 'n': 'Dabrowski'}
# Technika haszowania: wstaw_liniowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 1.6666666666666667
#
# None
# None
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.3333333333333333
#
# None
# {'il': 92945, 'n': 'Dabrowski'}
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 1.75
#
# {'il': 89366, 'n': 'Lewandowski'}
# {'il': 92945, 'n': 'Dabrowski'}
# {'il': 88932, 'n': 'Wojcik'}
# {'il': 220217, 'n': 'Nowak'}
# {'il': 104418, 'n': 'Wisniewski'}
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_kwadratowe
# Wielkość tablicy: 7
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 2.0
#
# None
# {'il': 104418, 'n': 'Wisniewski'}
# None
# {'il': 220217, 'n': 'Nowak'}
# None
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 7
# Procent zapełnienia: 0.5
# Średnia ilość prób wstawiania: 1.3333333333333333
#
# None
# {'il': 104418, 'n': 'Wisniewski'}
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 92945, 'n': 'Dabrowski'}
# {'il': 131940, 'n': 'Kowalski'}
# None
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 7
# Procent zapełnienia: 0.7
# Średnia ilość prób wstawiania: 1.25
#
# {'il': 89366, 'n': 'Lewandowski'}
# {'il': 104418, 'n': 'Wisniewski'}
# None
# {'il': 220217, 'n': 'Nowak'}
# {'il': 92945, 'n': 'Dabrowski'}
# {'il': 131940, 'n': 'Kowalski'}
# {'il': 88932, 'n': 'Wojcik'}
# Technika haszowania: wstaw_dwukrotne
# Wielkość tablicy: 7
# Procent zapełnienia: 0.9
# Średnia ilość prób wstawiania: 1.5





