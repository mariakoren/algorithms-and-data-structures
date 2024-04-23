import random

class HashTableOL:
    def __init__(self):
        self.size = primes[random.randint(0, len(primes) - 1)]
        self.table = [None] * self.size

    def hash(self, name):
        hash_value = sum([ord(c) for c in name]) % self.size
        return hash_value

    def wstaw(self, name):
        index = self.hash(name)
        i = 0
        while i < self.size:
            if self.table[index] is None or self.table[index][1] == name:
                self.table[index] = [1, name]
                return i + 1
            else:
                i += 1
                index = (index + 1) % self.size
        raise Exception("Table is full")

    def print_table(self):
        for i in range(self.size):
            if self.table[i] is None:
                print("[ ]")
            else:
                print(f"[{self.table[i]['ilosc']}, {self.table[i]['nazwisko']}]")


#otwarte kwadratowe
class HashTableOK:
    def __init__(self):
        self.size = primes[random.randint(0, len(primes) - 1)]
        self.table = [None] * self.size
        self.count = 0

    def hash(self, name):
        hash_value = sum([ord(c) for c in name]) % self.size
        return hash_value


    def wstaw(self, name):
        index = self.hash(name)
        i = 0
        while i < self.size:
            if self.table[index] is None or self.table[index][1] == name:
                self.table[index] = [1, name]
                return i + 1
            else:
                i += 1
                index = (index + i ** 2) % self.size
        raise Exception("Table is full")

    def print_table(self):
        for i in range(self.size):
            if self.table[i] is None:
                print("[ ]")
            else:
                print(f"[{self.table[i]['ilosc']}, {self.table[i]['nazwisko']}]")


#otwarte dwukrotnie
class HashTableOD:
    def __init__(self):
        self.size = primes[random.randint(0, len(primes) - 1)]
        self.table = [None] * self.size
        self.count = 0

    def hash(self, name):
        hash_value = sum([ord(c) for c in name]) % self.size
        return hash_value

    def secondary_hash_function(self, key):
        return 7 - (key % 7)

    def wstaw(self, name):
        index = self.hash(name)
        i = 0
        while i < self.size:
            if self.table[index] is None or self.table[index][1] == name:
                self.table[index] = [1, name]
                return i + 1
            else:
                i += 1
                index = (index + i * self.secondary_hash_function(index)) % self.size
        raise Exception("Table is full")

    def print_table(self):
        for i in range(self.size):
            if self.table[i] is None:
                print("[ ]")
            else:
                print(f"[{self.table[i]['ilosc']}, {self.table[i]['nazwisko']}]")




# Funkcja do wczytania danych z pliku nazwiska.txt
def read_names(file_path):
    with open(file_path, "r") as f:
        names = f.readlines()
    return names

def read_primes(file_path):
    with open(file_path, "r") as f:
        primes = f.readlines()
    primes = [int(p) for p in primes[0].split()]
    return primes

names = read_names("nazwiska.txt")
primes = read_primes("pierwsze.txt")

# Funkcja do testowania operacji WSTAW dla danej techniki rozwiązywania kolizji i wypełnienia tablicy
def test_insertion(technique, fill_percentage):
    table_size = 10000 # Rozmiar tablicy
    filled_size = int(table_size * fill_percentage)  # Ilość elementów do wstawienia
    ht = technique()  # Inicjalizacja tablicy
    ht.size = 10000
    ht.table = [None] * 10000
    target_size = int(ht.size * fill_percentage / 100)
    count_insertion_attempts = 0
    for i in range(target_size):
        name = names[i].split()[1]
        count_insertion_attempts += ht.wstaw(name)
    avg_attempts = count_insertion_attempts / target_size

    # Wydruk wyników
    print(f"Technika: {technique.__name__}")
    print(f"Wypełnienie tablicy: {fill_percentage * 100}%")
    print(f"Ilość wstawionych elementów: {filled_size}")
    print(f"Avg number of attempts per insertion: {avg_attempts:.2f}")
    print()
    print()

# test_insertion(HashTableOL, 0.9)
# Przykładowe wywołanie testu
test_insertion(HashTableOL, 0.5)  # Test dla techniki OL i wypełnienia 50%
test_insertion(HashTableOL,0.7)
test_insertion(HashTableOL, 0.9)


test_insertion(HashTableOK, 0.5)  # Test dla techniki OK i wypełnienia 50%
test_insertion(HashTableOK, 0.7)
test_insertion(HashTableOK, 0.9)


test_insertion(HashTableOD, 0.5)  # Test dla techniki OD i wypełnienia 50%
test_insertion(HashTableOD, 0.7)
test_insertion(HashTableOD, 0.9)

#WYNIKI
# Technika: HashTableOL
# Wypełnienie tablicy: 50.0%
# Ilość wstawionych elementów: 5000
# Avg number of attempts per insertion: 1.04
#
#
# Technika: HashTableOL
# Wypełnienie tablicy: 70.0%
# Ilość wstawionych elementów: 7000
# Avg number of attempts per insertion: 1.10
#
#
# Technika: HashTableOL
# Wypełnienie tablicy: 90.0%
# Ilość wstawionych elementów: 9000
# Avg number of attempts per insertion: 1.13
#
#
# Technika: HashTableOK
# Wypełnienie tablicy: 50.0%
# Ilość wstawionych elementów: 5000
# Avg number of attempts per insertion: 1.04
#
#
# Technika: HashTableOK
# Wypełnienie tablicy: 70.0%
# Ilość wstawionych elementów: 7000
# Avg number of attempts per insertion: 1.11
#
#
# Technika: HashTableOK
# Wypełnienie tablicy: 90.0%
# Ilość wstawionych elementów: 9000
# Avg number of attempts per insertion: 1.17
#
#
# Technika: HashTableOD
# Wypełnienie tablicy: 50.0%
# Ilość wstawionych elementów: 5000
# Avg number of attempts per insertion: 1.04
#
#
# Technika: HashTableOD
# Wypełnienie tablicy: 70.0%
# Ilość wstawionych elementów: 7000
# Avg number of attempts per insertion: 1.11
#
#
# Technika: HashTableOD
# Wypełnienie tablicy: 90.0%
# Ilość wstawionych elementów: 9000
# Avg number of attempts per insertion: 1.19

