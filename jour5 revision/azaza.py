fruits = ["pomme", "poire", "raisin"]

print(fruits)

fruits.append ("orange")

print(fruits)

fruits.insert(1,"Kiwi")

print(fruits)

fruits.remove ("poire")

print(fruits)

fruits.pop()

print(fruits)

fruits.append ("Tomate")
fruits.append ("Fraise")

print (len(fruits))

for fruit in fruits:
    print (fruit)

for fruit in fruits:
    print (fruit.upper())


fruits_majuscules = []

for fruit in fruits:
    fruits_majuscules.append(fruit.upper())

print(fruits_majuscules)

longeur = []

for fruit in fruits:
    longeur.append(len(fruit))

print (longeur)

fruits_courts = []

for fruit in fruits:
    if (len(fruit)) < 6:
        fruits_courts.append(fruit)

print (fruits_courts)

fruits_longs = []

for element in fruits:
    if (len(element)) >= 6:
        fruits_longs.append(element)

print(fruits_longs)