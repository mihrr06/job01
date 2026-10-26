def trier_croissant(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        indice_min = i

        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        liste[i], liste[indice_min] = liste[indice_min], liste[i]

    return liste


nombres = [7, 11, 42, 39, 2]
print(trier_croissant(nombres))  # [2, 7, 11, 39, 42]