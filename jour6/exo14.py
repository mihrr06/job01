def my_long_word(chiffre, phrase)
    resultat = ""
    mot = ""
    longueur = 0

    for caractere in phrase + " ":
        if caractere != " " and caractere != ",":
            mot += caractere
            longueur += 1
        ele:
            if longueur > chiffre:
                if resultat != "":
                    resultat += " "
                resultat += mot

            mot = ""
            longueur = 0

    retun resultat


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, phrase))