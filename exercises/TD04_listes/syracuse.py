def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste=[n]

    while n!=1:
        if n%2==0:
            n//=2
            liste.append(n)
        else:
            n=(n*3)+1
            liste.append(n)
    return(liste)


#print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    n=0
    for i in range (1,n_max+1):
        if syracuse(i)[-1]!=1:
            n+=1
    if n==0:
        return True
    else:
        return False

        
#print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    liste=[n]
    Vol=0

    while n!=1:
        if n%2==0:
            n/=2
            liste.append(n)
            Vol+=1
        else:
            n=(n*3)+1
            liste.append(n)
            Vol+=1
    return(Vol)

#print("Le temps de vol de", 2961956, "est", tempsVol(2961956))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    Vols=[]
    for i in range (1,n_max+1):
        Vols.append(tempsVol(i))
    print(Vols)


#print(tempsVolListe(100))

def GrandVol(n):
    Grand=0
    nbGrand=0
    for i in range (1,n+1):
        if tempsVol(i)>Grand:
            Grand=tempsVol(i)
            nbGrand=i
    return (nbGrand,Grand)


#print(GrandVol(10000))


def gValeur(n):
    Grand=0
    ni=n
    while ni!=1:
        if ni>Grand:
            Grand=ni
        if ni%2==0:
            ni/=2
        else:
            ni=(ni*3)+1
    return(n,Grand)

#print(gValeur(9663))

def maxgValeur(n):
    maxGrand=0
    maxn=0
    for i in range (1,n+1):
        if gValeur(i)[1]>maxGrand:
            maxGrand=gValeur(i)[1]
            maxn=gValeur(i)[0]
    return(maxn,maxGrand)

#print(maxgValeur(10000))
