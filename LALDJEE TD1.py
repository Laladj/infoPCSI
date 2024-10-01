#Antoine Laldjee-Deroubaix, HX1. 
#%%===========Exercice 1============================================
#i
def teste_type(arg):
    """Cette fonction prend un argument de classe quelconque et renvoie sa classe parmi quelques unes"""
    if type(arg)== int:
        return "entier"
    elif type(arg)== float:
        return "flottant"
    elif type(arg)== str : 
        return "chaine"
    else:
        return "inconnu"  

print(teste_type(3))
print(teste_type(3.2))
print(teste_type("banane"))
print(teste_type(False))

#%%=============Exercice 2============================================
#i
def moy1(liste : list):
    """Prend comme argument une liste de flottants/entiers et renvoie la moyenne 
    éléments dans la liste """
    count = 0
    for element in liste:
        count += element
    return count/len(liste)
#ii
L = [8.15, 16, 11.5]
moy1(L)
#on trouve bien 11.883, on vérifie le résultat obtenu en calculant print(sum(L)/len(L))

#%%==========iii)
def barycentre(L:list, A:list):
    """la fonction prend deux arguments: 
            En premier la liste des valeurs
             En second les coefficients respectifs de chacune des valeurs """
    count = 0
    for valeur in L:
        for coefficient in A:
            count += (valeur*coefficient)
    return count/sum(A)
#iv
L = [8.5,16,11.5]
A = [5,0.75,11]
print(barycentre(L,A)) #on trouve bien 36.0

#%%==============Exercice 3=======================
#a)
def presence(a:str, ch:str):
    """Recherche la présence de la chaine de caractère a dans la chaine ch. Peu optimisé"""
    for i in ch:
        if i == a:
           return True
        else:
            pass
    return False
    
presence("a","banane")
presence("z","banane")

# Sans utiliser "in"
def presence(a: str, ch:str):
    L = list(ch)
    for i in range(1,len(ch)+1):
        if a == L[i]:
            return True
        else: 
            pass
#%%====a) on essaie de mieux l'optimiser avec les listes
def presence2(a:str, ch:str):
    """Meme usage que présence, seulement en utilisant les listes."""
    liste = []
    for lettre in ch:
        liste.append(lettre)
    if a in liste:
        return True
    else:
        return False
presence2("a","banane")
presence2("z","banane")
    

#%%=======b)
def trouve_indice(L:list,d:int):
    """Cette fonction prend une liste et un entier en paramètres, et renvoie le couple du plus
     petit indice du nombre de la liste divisible par l'entier,
     ainsi que le nombre en question """
    divisibles = []
    for i, entier in enumerate(L):
        if entier%d == 0:
            divisibles.append((i,entier))
        else:
            pass
    if divisibles == []:
        return None
    else: 
        return divisibles[0]

liste = [3, 7, 9, 12, 15, 18, 21, 22, 27]

trouve_indice(liste,4)

#%%=================EXERCICE 4============================
#i
def maxi(L:list):
    """ Cette fonction prend en paramètre une liste composée
    """
    maxi = 0
    if type(L) != list:
        raise TypeError("l'argument de la fonction doit être une liste")
    elif L == []:
        raise ValueError("la liste est vide")
    else:
        for element in L:
            if element >= maxi:
                maxi = element
    return maxi
maxi([5,2, 3, 14, 8])
#%% ii)

def ind_maxi(L:list):
    """Cette fonction prend en paramètre une liste composée d'entiers ou de flottants,
    et renvoie l'indice de la première occurence de son maximum:
    Elle rend la position dans la liste comme on l'entend, c'est à dire que l'élément 0 est l'élément 1"""
    indice, maximum = -1, -1
    for i, nombre in enumerate(L):
        print(i, maximum)
        if nombre > maximum:
            indice, maximum = i, nombre
        else : pass
    return indice 
print(ind_maxi([2, 5, 9, 14, 8, 6, 14, 3,8]))
#%%=======EXERCICE 5=====================
def log_entier2(n:int):
    """Prend comme paramètre un entier, et calcule l'exposant entier p tel que 2**p <= n < 2**p+1"""
    count = 1
    p = 1
    while count <= n:
        count *= 2
        p += 1
    return p-2

log_entier2(16)
log_entier2(20)
#test 
a = []
for i in range(1,11): 
    a.append((i, log_entier2(i)))
print(a)
#%%========EXERCICE 6================

def JO(liste:list):
    """Prend en paramètre une liste, et renvoie le score de chaque pays"""
    count = 0
    for element in liste:
        if element == "o":
            count += 10
        elif element == "a":
            count += 7
        elif element == "b":
            count += 4 
        else:
            pass
    return count 

Paris = ["o","a","b","o"]
print(JO(Paris))

#%% b) 
def medailles(liste:list):
    """Renvoie le nombre de médailles par type de medaille. IMPORTANT: On utilise gold et non or, car or est attribué"""
    gold, silver, bronze = 0,0,0
    for element in liste:
        if element == "o":
            gold +=1
        elif element == "a":
            silver +=1
        elif element == "b":
            bronze +=1 
        else:
            pass
    return [gold, silver, bronze] 
Paris = ["o","a","b","o"]
medailles(Paris)

    



# %%============EXERCICE 7===============

def somMax(L:list, N:int):
    """Renvoie la première sous liste dont la somme des entiers est inférieure strictement à n"""
    liste = []
    element = 0
    while sum(liste) < N:
        liste.append(L[element])
        element += 1
    return liste
somMax([5,2, 3, 14, 8], 11)

#%%=====================Exercice 8==============
#a)
def bissextile(year:int):
    """Renvoie True si l'année est bissextile, False sinon"""
    if (year%4 == 0 and year%100 != 0) or (year%400==0):
        return True
    else:
        return False

bissextile(40)
bissextile(100)
bissextile(17)
bissextile(400)


#%% B. après recherche approfondie, aide d'une recherche internet.
#Sans instructions conditionnelles.
def bissextile2():
    """Renvoie True si l'année est bissextile, False sinon, sans utiliser d'instructions conditionelles"""
    year = int(input("Veuillez rentrer l'année: "))
    booleen = (year % 4 == 0) * (year % 100 != 0) + (year % 400 == 0)
    return bool(booleen)
bissextile2(40)
bissextile2(100)
bissextile2(17)
bissextile2(400)
#%% AVEC la demande à l'utilisateur et le retour par phrase
def bissextile2():
    """Renvoie si l'année est bissextile ou non, à la suite de l'entrée d'une année par l'utilisateur"""
    year = int(input("Veuillez rentrer l'année: "))
    booleen = (year % 4 == 0) * (year % 100 != 0) + (year % 400 == 0)
    if bool(booleen)== True:
        print(f"{year} est une année bissextile.")
    else:
        print(f"{year} n'est pas une année bissextile")
bissextile2(40)
bissextile2(100)
bissextile2(17)
bissextile2(400)

#%%===========Exercice 9===============
def monte_et_descend(T: list):
    """Cette fonction prend en argument une liste et renvoie True si ses valeurs montent puis descendent.
    Elle renvoie False sinon.
    J'ai trouvé de l'aide sur internet"""
    
    if len(T) < 2:  
        return False
    i = 0
    while i < len(T) - 1 and T[i+1] >= T[i]:
        i += 1
    
    if i == 0 or i == len(T) - 1:
        return False
    
    while i < len(T) - 1 and T[i+1] <= T[i]:
        i += 1
    
    return i == len(T) - 1

print(monte_et_descend([1, 1, 2, 2, 3, 3, 2, 2, 1]))
print(monte_et_descend([1, 2, 3, 4, 5]))




#%%================EXERCICE 10===========
def fibonacci(n):
    """renvoie le nième terme de la suite de fibonacci"""
    liste =[0,1]
    for i in range(n):
        liste.append(liste[i]+liste[i+1])
    return liste[-2]

fibonacci(5)
fibonacci(0)
fibonacci(1)

def est_fibonacci(N:int):
    """Renvoie True si il existe a tel que fib(a)= N, False, sinon. """
    for i in range(0,N+2):
         if N == fibonacci(i):
             return True
         else:
             pass
    return False  
est_fibonacci(6765)
est_fibonacci(2)

#%%===========EXERCICE 11=============
#i)
def estPremier(n:int):
    div = []
    """Cette fonction prend pour paramètre un entier positif, et renvoie si il est premier ou non"""
    if n == 0 or n ==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                div.append(i)
            else:
                pass
    return True if div==[] else False
estPremier(12)
estPremier(17)


#%%
def listePremiers(n=100):
    """Renvoie la liste des entiers premiers inférieurs ou égaux à n. Prend comme valeur par défaut 100"""
    liste = []
    for i in range(1,n+1):
        if estPremier(i):
            liste.append(i)
        else:
            pass
    return liste

#%%ii) 
def prochainPremier(n:int):
    """Renvoie le nombre premier qui suit n :
    (Tchebychev 1850) : pour tout entier naturel
     n ≥ 1 il existe un nombre premier compris entre n et 2n strictement."""
    for i in range(n, 2*n+1):
        if estPremier(i):
            return i
        else: pass
        
        
prochainPremier(100)
prochainPremier(200)
prochainPremier(300)
prochainPremier(10**8)

#%%iii)
def estPremier(n:int):
    """Renvoie la liste des entiers premiers inferieurs ou égaux à n
    Usage du crible d'Eratosthène
    Inspiré de Stack Overflow"""
    a = [True] * n                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, n, i):     
                a[n] = False
estPremier(10**6)

#%%=======EXERCICE 12===========
#i) 
def maxi(L:list):
    """Renvoie le plus petit et le plus grand élément de la liste, sous la forme d'un tuple"""
    plusGrand = 0
    plusPetit = int(L[0])
    for i, nombre in enumerate(liste):
        if nombre >= plusGrand:
            plusGrand= nombre
        if nombre <= plusPetit:
            plusPetit = nombre
        else:pass
    return (plusPetit,plusGrand)
        


maxi([1,3,8,12, 7, 4, 12, 8, 2])
#%% ii)

def elementsEgaux(L:list):
    """Vérifie si tous les éléments de la liste sont identiques"""
    for i in range(0, len(L)+1):
        if L[i]== L[i+1]:
            pass
        else: 
            return False
    return True

def maximumListe(L:list):
    """Renvoie le maximum d'une liste, déjà écrit précemment, mais nécéssaire pour le dernier script"""
    plusGrand = 0
    for i, nombre in enumerate(L):
        if nombre >= plusGrand:
            plusGrand= nombre
    return plusGrand

def maxi2(L:list):
    """Renvoie le second plus grand nombre de la liste."""
    if elementsEgaux(L):
        return None
    else: L2 = list(filter(lambda a: a != maximumListe(L), L))
    return maximumListe(L2)

maxi2([3, 3, 8, 12, 7, 4, 12, 9, 2])


#============================ FIN DU DEVOIR========================================