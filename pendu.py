#from fonctions_pendu import 
from random import randrange

print("\nBIENVENUE DANS LE JEU DU PENDU !\n")
tiret = "_" * 8
choix = input("Voulez-vous jouer ? o/n : \n")

while choix != "o" and choix != "n" :
    print("Veuillez répondre 'o' pour oui ou 'n' pour non ")
    choix = input("Voulez-vous jouer ? o/n : ")

while choix == "o" :
    #ouverture du dico
    file = open("dico_france.txt", "r", encoding="iso-8859-1")
    dico = file.read().splitlines()
    #choix aléatoire du mot
    mot = dico[randrange(len(dico))]
    solus = "-" * (len(mot))
    file.close()

    #choix du niveau de difficulté
    
    level = input("\n- Choisissez un niveau de difficulté -\n\nfacile = 1  intermédiaire = 2  expert = 3\n ")
    
    
    #boucle de vérification d'erreurs de saisie
    while level != "1" and level != "2" and level != "3" :
        print("---Veuillez entrer une saisie valide---")
        level = input("\nfacile = 1  intermédiaire = 2  expert = 3 :  ")
    level = int(level)
    
    ######################### Niveau 1 ###############################
    if level == 1 :
        tentatives = 10
        liste = []      #création liste pour stocker les lettres déjà utilisées
        "\n"
        print(tiret)
        print("NIVEAU 1")
        print("\n|Respectez les accents, et\n|les majuscules de nom propres.\n|Bonne chance !")
        print("\n- Vous disposez de ", tentatives, "tentatives -\n")
        
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("\nEntrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("\n-> Caractère érroné, recommencez ! : " )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('\n\n***** Vous avez trouvé la lettre', lettre, "*****")
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print(liste)
                print("\n-> La lettre", lettre, "n'est pas dans le mot\n")
        
            print("\n- Il vous reste", tentatives, "tentatives -")
            print("\nLettres utilisées", liste, "\n")
            print(solus)

        #vérification de victoire ou echec
        if solus == mot :
            print("-- BRAVO, vous avez trouvé le mot caché en", len(list), "coups --")
            
        else :
            print("\n°°° Désolé, Vous avez perdu °°° !\n")   
            print("- Le mot était : ", mot) 

        # fin de boucle

        #################### Niveau 2 #########################
    if level == 2 :
        tentatives = 7
        liste = []      #création liste pour stocker les lettres déjà utilisées
        "\n"
        print(tiret)
        print("NIVEAU 2")
        print("\n|Respectez les accents, et\n|les majuscules de nom propres.\n|Bonne chance !")
        print("\n- Vous disposez de ", tentatives, "tentatives -\n")
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("\nEntrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("\n-> Caractère érroné, recommencez ! : " )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('\n\n***** Vous avez trouvé la lettre', lettre, "*****")
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print(liste)
                print("\n-> La lettre", lettre, "n'est pas dans le mot\n")
        
            print("\n- Il vous reste", tentatives, "tentatives -")
            print("\nLettres utilisées", liste, "\n")
            print(solus)

        #vérification de victoire ou echec
        if solus == mot :
            print("-- BRAVO, vous avez trouvé le mot caché en", len(list), "coups --")
            
        else :
            print("\n°°° Désolé, Vous avez perdu °°° !\n")   
            print("- Le mot était : ", mot) 

        # fin de boucle

        ####################### Niveau 3 ###########################
    if level == 3 :
        tentatives = 4
        liste = []      #création liste pour stocker les lettres déjà utilisées
        "\n"
        print(tiret)
        print("NIVEAU 3")
        print("\n|Respectez les accents, et\n|les majuscules de nom propres.\n|Bonne chance !")
        print("\n- Vous disposez de ", tentatives, "tentatives -\n")
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("\nEntrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("\n-> Caractère érroné, recommencez ! : " )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('\n\n***** Vous avez trouvé la lettre', lettre, "*****")
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print(liste)
                print("\n-> La lettre", lettre, "n'est pas dans le mot\n")
        
            print("\n- Il vous reste", tentatives, "tentatives -")
            print("\nLettres utilisées", liste, "\n")
            print(solus)

        #vérification de victoire ou echec
        if solus == mot :
            print("-- BRAVO, vous avez trouvé le mot caché en", len(list), "coups --")
            
        else :
            print("\n°°° Désolé, Vous avez perdu °°° !\n")   
            print("- Le mot était : ", mot) 

        # fin de boucle

    choix = input("Voulez-vous rejouer ? o/n : ")
    while choix != "o" and choix != "n" :
        print("Veuillez répondre 'o' pour oui ou 'n' pour non ")
        choix = input("Voulez-vous rejouer ? o/n : ")

print("DAMNED !!!")
