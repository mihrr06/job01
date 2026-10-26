nombres = [4, 9, 2, 7]

plus_petit = nombres[0]

for nombre in nombres:
    if nombre < plus_petit:
        plus_petit = nombre

print(plus_petit)
