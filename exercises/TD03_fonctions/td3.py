# #temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (temps[3] + temps[2] * 60 + temps[1] * 60**2 + temps[0] * (60**2)*24)

# temps = (3,23,1,34)
# print(type(temps))
# print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde//(3600*24)
    heure = (seconde%(3600*24))//3600
    minute = (seconde%3600)//60
    seconde = seconde%60
    return(jour,heure,minute,seconde)


    
# temps = secondeEnTemps(100000)
# print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici
def pluriel(mot):
    return (mot+'s')
    
def afficheTemps(temps):
    if temps[0]!=0:
        if temps[0]>1:
            print(temps[0],pluriel('jour'), end=" ")
        else: 
            print("1 jour", end=" ")
    if temps[1]!=0:
        if temps[1]>1:
            print(temps[1],pluriel('heure') , end=" ")
        else: 
            print("1 heure", end=" ")
    if temps[2]!=0:
        if temps[2]>1:
            print(temps[2],pluriel('minute'), end=" ")
        else: 
            print("1 minute", end=" ")
    if temps[3]!=0:
        if temps[3]>1:
            print(temps[3],pluriel('seconde'), end=" ")
        else: 
            print("1 seconde", end=" ")
        

    
#afficheTemps((1,0,14,23))


# def demandeTemps():
#     jour=int(input("jours"))
#     heure=int(input("heures"))
#     minute=int(input("minutes"))
#     seconde=int(input("secondes"))
#     temps=jour,heure,minute,seconde
#     while heure>24 or minute>60 or seconde>60:
#         jour=int(input("jours"))
#         heure=int(input("heures"))
#         minute=int(input("minutes"))
#         seconde=int(input("secondes"))
#         temps=jour,heure,minute,seconde
#     return temps



# afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    temps = secondeEnTemps(temps1+temps2)
    return afficheTemps (temps)
    

#sommeTemps((2,3,4,25),(5,22,57,1))



def proportionTemps(temps,proportion):
    temps=tempsEnSeconde(temps)
    temps*=proportion
    temps=secondeEnTemps(temps)
    return temps

# afficheTemps(proportionTemps(proportion = 0.2,temps =(2,0,36,0)))


def tempsEnDate(temps):
    année=temps[0]//365 + 1970
    jour=(temps[0]%350)
    date = année,jour,temps[1],temps[2],temps[3]
    return date


    
def afficheDate(date = -1):
    if date!=-1:
        print("\nannée :",date[0],"jour :",date[1],"heure :",date[2], "minute :",date[3],"seconde :",date[4])
    else:
        print("année : 1970",'jour : 1 ',"heure : 0","minute : 0","seconde : 0")
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()


