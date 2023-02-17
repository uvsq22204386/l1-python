carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in range(len(carre)):
        print(carre[i])

afficheCarre(carre_mag)
#afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme=0
    listesomme=[]
    for i in range (len(carre)):
        somme=0
        for o in range(len(carre)):
            somme+=carre[i][o]
        listesomme.append(somme)
    for p in range (1,len(carre)-1):
        if listesomme[0]!=listesomme[p]:
            return(-1)
    return(somme)




# print(testLignesEgales(carre_mag))
# print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    somme=0
    listesomme=[]
    for i in range (len(carre)):
        somme=0
        for o in range(len(carre)):
            somme+=carre[o][i]
        listesomme.append(somme)
    for p in range (1,len(carre)-1):
        if listesomme[0]!=listesomme[p]:
            return(-1)
    return(somme)

# print(testColonnesEgales(carre_mag))
# print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    somme=0
    somme1=0
    listesomme=[]
    for i in range (len(carre)):
        somme+=carre[i][i]
        somme1+=carre[len(carre)-1-i][len(carre)-1-i]
    if somme!=somme1:
        return -1
    return somme
    

# print(testDiagonalesEgales(carre_mag))
# print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre)==testColonnesEgales(carre)==testDiagonalesEgales(carre):
        return True
    else:
        return False 

# print(estCarreMagique(carre_mag))
# print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    listecarre=[]
    for i in range (1,(len(carre))**2 +1):
        listecarre.append(i) 
    for i in range (len(carre)):
        for o in range(len(carre)):
            if carre[i][o] in listecarre:
                listecarre.remove(carre[i][o])
            else:
                return False
    return True

    

            
#print(estNormal(carre_mag))
#print(estNormal(carre_pas_mag))

