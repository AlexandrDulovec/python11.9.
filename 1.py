def obrazek(Z):
    if Z % 2 != 1:
        print("Zadejte liché číslo Z.")
        return

    for i in range(1, Z + 1):
        for j in range(1, Z + 1):
            if i == j or i + j == Z + 1:
                print(str(2 * i - 1), end='')
            else:
                print(' ', end='')
        print()

try:
    Z = int(input("Zadejte liché číslo Z: "))
    obrazek(Z)
except ValueError:
    print("Chybný vstup. Zadejte liché číslo Z.")
