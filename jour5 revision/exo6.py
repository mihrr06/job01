def table(n):
    resultat = ""
    for i in range(1, 11):
        resultat = resultat + f"{n} x {i} = {n * i}\n"
    return resultat

x = table(5)
print("Résultat :", x)
