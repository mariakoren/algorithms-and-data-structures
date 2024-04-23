class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def wstaw(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = wstaw(root.left, key)
    elif key > root.key:
        root.right = wstaw(root.right, key)
    return root


def szukaj(root, key):
    if root is None:
        return f"Element {key} nie istnieje w drzewie."
    if root.key == key:
        return f"Element {key} znaleziony w drzewie."
    if key < root.key:
        return szukaj(root.left, key)
    else:
        return szukaj(root.right, key)

def usun(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = usun(root.left, key)
    elif key > root.key:
        root.right = usun(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min_node = znajdz_minimum(root.right)
        root.key = min_node.key
        root.right = usun(root.right, min_node.key)
    return root

def znajdz_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def drukuj(root, space=0):
    if root is None:
        return
    space += 5
    drukuj(root.right, space)
    print()
    for i in range(5, space):
        print(end=" ")
    print(root.key)
    drukuj(root.left, space)

def drukuj2(root):
    level=0
    if root is not None:
        drukujFragment(root.right, level + 1)
        print("\n" + "\t" * level + "|", end=' ')
        print("wys:" + str(level), end=' ')
        print(str(root.key))
        print("\t" * level + "|", end=' ')
        drukujFragment(root.left, level + 1)
        print()

def drukujFragment(root, level=0, max_level=3):
    if root is not None and level <= max_level:
        drukujFragment(root.right, level + 1, max_level)
        print("\n" + "\t" * level + "|", end=' ')
        print("wys:" + str(level), end=' ')
        print(str(root.key))
        print("\t" * level + "|", end=' ')
        drukujFragment(root.left, level + 1, max_level)
        print()

def obliczWysokosc(root):
    if root is None:
        return 0
    else:
        lewa_wysokosc = obliczWysokosc(root.left)
        prawa_wysokosc = obliczWysokosc(root.right)
        return max(lewa_wysokosc, prawa_wysokosc) + 1

# Wczytanie słów z pliku tekstowego
def wczytajSlowa(plik, ilosc_slow):
    with open(plik, 'r') as file:
        slowa = [next(file).strip().split()[1] for _ in range(ilosc_slow)]
    return slowa

def zadanie4():
    ilosc_slow = [500, 1000, 2000]
    # ilosc_slow = [10]
    plik_tekstowy = 'nazwiska.txt'
    # Plik ze słowami

    for ilosc in ilosc_slow:
        slowa = wczytajSlowa(plik_tekstowy, ilosc)
        root = None
        for i in range(ilosc):
            root=wstaw(root, slowa[i])
        wysokosc = obliczWysokosc(root)
        print(f"Wysokość drzewa po wstawieniu {ilosc} słów: {wysokosc}")
        print("Fragment drzewa:")
        drukujFragment(root, max_level=5)



        print("-------------------------------")

def przykladUzycia():
    root=None
    root=wstaw(root, 18)
    root = wstaw(root, 18)
    # root = wstaw(root, 6)
    # root = wstaw(root, 30)
    # root = wstaw(root, 21)
    # root = wstaw(root, 21)
    # root = wstaw(root, 19)
    # root = wstaw(root, 8)

    # root=wstaw(root, "aba")
    print("drzewo poczatkowe")
    drukuj2(root)
    print(szukaj(root, 21))
    print(szukaj(root, 0))
    # print("drzewo po usunięciu elementa 21 (ma jednego syna)")
    # usun(root, 21)
    # drukuj2(root)
    # print("drzewo po usunięciu elementa 8 (jest liściem)")
    # usun(root, 8)
    # drukuj2(root)
    print("drzewo po usunięciu elementa 18 (ma dwóch synów)")
    usun(root, 18)
    usun(root, 18)
    drukuj2(root)


# przykladUzycia()
zadanie4()


