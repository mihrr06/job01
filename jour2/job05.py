
nombre = int(input("Choisissez un nombre entier : "))
i = 1

while i <= nombre:
    print("Table de", i)

    multiplicateur = 1
    while multiplicateur <= 10:
        print(f"{i} x {multiplicateur} = {i * multiplicateur}")
        multiplicateur = multiplicateur + 1

    i = i + 1
