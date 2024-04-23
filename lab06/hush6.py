import math
import time
import random

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

class HashTable:
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

    # def search(self, name):
    #     index = self.hash(name)
    #     i = 0
    #     while i < self.size:
    #         if self.table[index] is None:
    #             return False, i + 1
    #         elif self.table[index][1] == name:
    #             return True, i + 1
    #         else:
    #             i += 1
    #             index = (index + 1) % self.size
    #     return False, i + 1
    #
    # def delete(self, name):
    #     index = self.hash(name)
    #     i = 0
    #     while i < self.size:
    #         if self.table[index] is None:
    #             return False
    #         elif self.table[index][1] == name:
    #             self.table[index] = [math.inf, "DEL"]
    #             return True
    #         else:
    #             i += 1
    #             index = (index + 1) % self.size
    #     return False


# [W] Operacja WSTAW. Pomiar: średnia ilość prób wykonanych przy wstawianiu elementu
# (średnia ze wszystkich wstawień) przy różnych wypełnieniach tablicy: 50%, 70% i 90%.

# create hash table with size 10000
ht = HashTable()
ht.size = 10000
ht.table = [None] * 10000

# measure insertions and print results
for fill_percent in [50, 70, 90]:
    print(f"Fill percent: {fill_percent}")
    ht.table = [None] * 10000  # reset the table
    target_size = int(ht.size * fill_percent / 100)
    count_insertion_attempts = 0
    for i in range(target_size):
        name = names[i].split()[1]
        count_insertion_attempts += ht.wstaw(name)
    avg_attempts = count_insertion_attempts / target_size
    print(f"Avg number of attempts per insertion: {avg_attempts:.2f}")
    print()


# [S] Operacje WSTAW i SZUKAJ. Pomiar: wypełnienie tablicy do 80% i wykonanie pewnej ilości operacji szukaj (np. ostatnie 20% elementów) oraz obliczenie średniej ilości prób
# wykonanych przy wstawianiu elementu
# create hash table with size 10000

ht = HashTable()
ht.size = 10000
ht.table = [None] * 10000

# measure insertions and print results for different fill percentages

for fill_percent in [50, 70, 90]:
    print(f"Fill percent: {fill_percent}")
    ht.table = [None] * 10000 # reset the table
    target_size = int(ht.size * fill_percent / 100)
    count_insertion_attempts = 0
    for i in range(target_size):
        name = names[i].split()[1]
        count_insertion_attempts += ht.insert(name)
    avg_attempts = count_insertion_attempts / target_size
    print(f"Avg number of attempts per insertion: {avg_attempts:.2f}")
# measure search operations and print results
search_attempts = []
search_size = int(target_size * 0.2)
for i in range(target_size, target_size + search_size):
    name = names[i].split()[1]
    _, attempts = ht.search(name)
    search_attempts.append(attempts)
avg_search_attempts = sum(search_attempts) / search_size
print(f"Avg number of attempts per search: {avg_search_attempts:.2f}")
print()

# [W+S] Operacje WSTAW i SZUKAJ. Pomiar: średnia ilość prób wykonanych przy wstawianiu elementu
# (średnia ze wszystkich wstawień) oraz średnia ilość prób wykonanych przy operacjach szukaj
# (średnia ze wszystkich operacji) przy różnych wypełnieniach tablicy: 50%, 70% i 90%.
# create hash table with size 10000

ht = HashTable()
ht.size = 10000
ht.table = [None] * 10000

# measure insertions and search operations and print results for different fill percentages
for fill_percent in [50, 70, 90]:
    print(f"Fill percent: {fill_percent}")
    ht.table = [None] * 10000  # reset the table
    target_size = int(ht.size * fill_percent / 100)
    count_insertion_attempts = 0
    for i in range(target_size):
        name = names[i].split()[1]
        count_insertion_attempts += ht.insert(name)
    avg_insert_attempts = count_insertion_attempts / target_size
    print(f"Avg number of attempts per insertion: {avg_insert_attempts:.2f}")


search_attempts = []
search_size = int(target_size * 0.2)
for i in range(target_size, target_size + search_size):
    name = names[i].split()[1]
    _, attempts = ht.search(name)
    search_attempts.append(attempts)
avg_search_attempts = sum(search_attempts) / search_size
print(f"Avg number of attempts per search: {avg_search_attempts:.2f}")
print()