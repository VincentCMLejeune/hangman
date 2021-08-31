import dessin

print("Welcome to the hangman !")
continuer = True

while continuer == True:

# Ajout du mot à deviner et dissimulation de la console
    mot_a_lowercaser = input("Player 1, type the word to guess :\n> ")
    mot_cache = mot_a_lowercaser.lower()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    

# Initialisation du jeu
    mot_devine = ""
    for i in mot_cache:
        mot_devine += "_"
    compteur = 8
    lettres_ratees = []
    print("Hello Player 2, now it is time to guess the word !")

# Déroulé du jeu
    while compteur != 0 and mot_cache != mot_devine:
        print(dessin.dessine(compteur))
        print("Word to guess : " + mot_devine)
        if lettres_ratees != []:
            message_ratees = ""
            for i in lettres_ratees:
                message_ratees += i.upper()
                message_ratees += " "
            print("Wrong letters : " + message_ratees)

        lettre_a_lower_caser = input("\nWrite a letter \n> ")
        lettre = lettre_a_lower_caser.lower()

        if lettre in lettres_ratees or lettre in mot_devine:
            print("Hm, you already tried this one.")
        
        elif lettre not in "abcdefghijklmnopqrstuvwxyz":
            print("A letter, please.")

        elif len(lettre) > 1:
            print("Just one letter at a time, please.")

        elif lettre in mot_cache:
            print("Good job ! The letter " + lettre.upper() + " is in the word")
            update_devine = ""
            for i in range(len(mot_cache)):
                if mot_cache[i] == lettre:
                    update_devine += lettre
                else:
                    update_devine += mot_devine[i]
            mot_devine = update_devine

        else:
            print("Damn ! The letter " + lettre.upper() + " is not in the word")
            lettres_ratees.append(lettre)
            compteur -= 1

    if compteur == 0:
        print(dessin.dessine(compteur))
        print("\nHe's dead, Mike... the word was " + mot_cache)
    else:
        print("\nVICTORY ! The word was " + mot_cache)
        if compteur > 1:
            print("You were " + str(compteur) + " steps away from death...")
        else:
            print("You were one little step away from death...")

# Nouvelle partie ?
    nouv_partie = input("Do you want to play another game ? (answer \"yes\" if you do, anything else if you don't) \n> ")
    nouv = nouv_partie.lower()
    if nouv != "yes":
        continuer = False
        print("Fair enough, have a nice day !")