
n = int(input("Choisissez un nombre entier : "))

for i in range(1, n + 1):
    print("Table de", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
