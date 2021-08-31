import dessin

print("Bienvenue dans le pendu !")
continuer = True

while continuer == True:

# Ajout du mot à deviner et dissimulation de la console
    mot_a_lowercaser = input("Joueur 1, inscris le mot à deviner :\n> ")
    mot_cache = mot_a_lowercaser.lower()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    

# Initialisation du jeu
    mot_devine = ""
    for i in mot_cache:
        mot_devine += "_"
    compteur = 8
    lettres_ratees = []
    print("Salut joueur 2, maintenant que ton ami a saisi un mot, nous pouvons passer aux choses sérieuses !")

# Déroulé du jeu
    while compteur != 0 and mot_cache != mot_devine:
        print(dessin.dessine(compteur))
        print("Mot à deviner : " + mot_devine)
        if lettres_ratees != []:
            message_ratees = ""
            for i in lettres_ratees:
                message_ratees += i.upper()
                message_ratees += " "
            print("Lettres ratées : " + message_ratees)

        lettre_a_lower_caser = input("\nInscris une lettre \n> ")
        lettre = lettre_a_lower_caser.lower()

        if lettre in lettres_ratees or lettre in mot_devine:
            print("Hm, tu as déja essayé cette lettre.")

        elif lettre in mot_cache:
            print("Bien joué ! La lettre " + lettre.upper() + " est dans le mot")
            update_devine = ""
            for i in range(len(mot_cache)):
                if mot_cache[i] == lettre:
                    update_devine += lettre
                else:
                    update_devine += mot_devine[i]
            mot_devine = update_devine

        else:
            print("Raté ! La lettre " + lettre.upper() + " n'est pas dans le mot")
            lettres_ratees.append(lettre)
            compteur -= 1

    if compteur == 0:
        print(dessin.dessine(compteur))
        print("\nIl est mort, Jim... Le mot à deviner était " + mot_cache)
    else:
        print("\nVICTOIRE ! Le mot à deviner était " + mot_cache)
        print("Tu étais à " + str(compteur) + " erreurs de la mort...")

# Nouvelle partie ?
    nouv_partie = input("Veux-tu reprendre une nouvelle partie ? (réponds \"oui\" si tu veux continuer, n'importe quoi d'autre pour arrêter) \n> ")
    nouv = nouv_partie.lower()
    if nouv != "oui":
        continuer = False
        print("Très bien, merci d'avoir joué !")
    else:
        print("Super, on s'en refait une !")