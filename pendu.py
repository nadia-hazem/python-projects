from random import randrange
from re import RegexFlag


print("BIENVENUE DANS LE JEU DU PENDU !")

choix = input("Voulez-vous jouer ? o/n : ")
while choix != "o" and choix != "n" :
    print("Veuillez répondre 'o' pour oui ou 'n' pour non ")
    choix = input("Voulez-vous jouer ? o/n : ")
while choix == "o" :

    file = open("dico_france.txt", "r", encoding="iso-8859-1")
    dico = file.read().splitlines()

    mot = dico[randrange(len(dico))]
    solus = "-" * (len(mot)) 
    file.close()

    level = int(input("Choisis un niveau ? 1 = facile 2 = intermédiaire 3 = expert : "))

    while level != 1 and level != 2 and  level != 3 :
        level = input("Choisissez une entrée valide")

    #Niveau 1###############################
    if level == 1 :
        tentatives = 10
        liste = []      #création liste pour stocker les lettres déjà utilisées
        print("Vous avez", tentatives, "essais")
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("Entrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("Vous devez entrer une seule lettre" )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('Vous avez trouvé la lettre', lettre)
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print("La lettre", lettre, "n'est pas dans le mot")
        
            print("Il vous reste", tentatives, "essais")
            print("Lettres utilisées", liste)
            print(solus)

        #vérification de victoire ou echec
        if solus == mot :
            print("BRAVO, vous avez trouvé le mot caché en", len(list), "coups")
            print("Le mot était : ", mot)
        else :
            print("Désolé, Vous avez perdu !")   
            print("Le mot était : ", mot) 

        # fin de boucle

        #Niveau 2#########################
    if level == 2 :
        tentatives = 7
        liste = []      #création liste pour stocker les lettres déjà utilisées
        print("Vous avez", tentatives, "essais")
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("Entrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("Vous devez entrer une seule lettre" )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('Vous avez trouvé la lettre', lettre)
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print("La lettre", lettre, "n'est pas dans le mot")
        
            print("Il vous reste", tentatives, "essais")
            print("Lettres utilisées", liste)
            print(solus)
        
        #vérification de victoire ou echec
        if solus == mot :
            print("BRAVO, vous avez trouvé le mot caché en", len(list), "coups")
            print("Le mot était : ", mot)
        else :
            print("Désolé, Vous avez perdu !")   
            print("Le mot était : ", mot) 

        # fin de boucle

        #Niveau 3###########################
    if level == 3 :
        tentatives = 4
        liste = []      #création liste pour stocker les lettres déjà utilisées
        print("Dans le niveau expert, vous ne verrez pas les lettres déjà utilisées, courage !" )
        print("Vous avez", tentatives, "essais")
        #boucle du jeu
        print(solus)     #affiche mot avec tirets à la place des lettres
        while solus != mot and tentatives > 0 :
            lettre = input("Entrez une lettre : ")
            #vérifie la saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                lettre = input("Vous devez entrer une seule lettre" )
            liste.append(lettre)        #ajout de la nouvelle lettre à la liste
            #vérifie la présence de la lettre dans le mot
            if lettre in mot :
                print('Vous avez trouvé la lettre', lettre)
                # on remplace les lettres trouvées
                for i in range(len(mot)) :
                    if lettre == mot[i] :
                        solus = solus[:i] + lettre + solus[i+1:]   
        # solus[:i] renvoie les lettres du début jusqu'à la lettre d'indice i-1
        # solus[i+1:] renvoie les lettres depuis la lettre d'indice i+1 jusqu'à la fin
            
            else :
                tentatives = tentatives -1 
                print("La lettre", lettre, "n'est pas dans le mot")
        
            print("Il vous reste", tentatives, "essais")
            # print("Lettres utilisées", liste)
            print(solus)
        
        #vérification de victoire ou echec
        if solus == mot :
            print("BRAVO, vous avez trouvé le mot caché en", len(list), "coups")
            print("Le mot était : ", mot)
        else :
            print("Désolé, Vous avez perdu !")   
            print("Le mot était : ", mot)   

        # fin de boucle

    choix = input("Voulez-vous rejouer ? o/n : ")
    while choix != "o" and choix != "n" :
        print("Veuillez répondre 'o' pour oui ou 'n' pour non ")
        choix = input("Voulez-vous rejouer ? o/n : ")

print("A bientot alors !")
