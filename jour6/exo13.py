liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
sans_doublons = []

for valeur in liste:
    if valeur not in sans_doublons:
        sans_doublons.append(valeur)

print(sans_doublons)
# [10, 20, 30, 50, 60, 40, 80]