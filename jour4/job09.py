def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3


note1 = float(input("Rentrez la première note : "))
note2 = float(input("Rentrez la deuxième note : "))
note3 = float(input("Rentrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant >= 8:
    print("Élève moyen")
else:
    print("Élève devant faire des efforts")