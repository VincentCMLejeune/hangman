print("Bienvenue dans le pendu !")
continuer = True

while continuer == True:
    nouv_partie = input("Veux-tu reprendre une nouvelle partie ? (réponds \"oui\" si tu veux continuer, n'importe quoi d'autre pour arrêter :\n> ")
    
    nouv = nouv_partie.lower()
    if nouv != "oui":
        continuer = False
        print("Très bien, merci d'avoir joué !")
    else:
        print("Super, on s'en refait une !")

