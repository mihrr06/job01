temp = int(input("Quel est la température de l'eau ? "))

if temp < 0:
    print ("Gel")
elif temp <=15:
    print ("Froid")
elif temp <=25:
    print ("Doux")
elif temp > 25:
    print ("Chaud")

