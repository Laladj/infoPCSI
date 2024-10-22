#!/usr/bin/python3
#Antoine Laldjee-Deroubaix, HX1, TD2 : Parcours de liste


#%%=============EXERCICE 1==========

def positivons(L:list):
    """Prend une liste de réels positifs, et renvoie la valeur absolue des elements de la liste"""
    L[:] = [abs(x) for x in L]
    
Ltest = [x for x in range(-5,10)]
positivons(Ltest)
#[5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L = [x-0.1 for x in range(-21,22)]
positivons(L)
#[21.1, 20.1, 19.1, 18.1,..., 19.9, 20.9]

#%%============EXERCICE 2=============
import random as rd
import time
import statistics as st
from matplotlib import pyplot as plt
import numpy as np

"""On cherche ici à étudier la complexité algorithmique de deux méthodes
visant à déterminer le second élément d'une liste.
second_max1() parcours deux fois la liste, 
tandis que second_max2() ne la parcours qu'une seule fois.

On obtient finalement dans les deux cas une complexité linéaire O(n),
avec néamoins une exécution plus rapide pour second_max(2). 

Plus de renseignements : 
https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes"""

#1. Reprise du script exo 12 TD1
def listeidentique(L:list) -> bool:
    """renvoie True si la liste est identique"""
    for i in range(len(L)):
        if L[i] != L[0]:
            return False
        else: pass
    return True
listeidentique([1,1,1,1]) #True
listeidentique([1,1,1,7]) #False

def maximumListe(L:list):
    """Renvoie le maximum d'une liste, déjà écrit précemment, mais nécéssaire
      pour le dernier script"""
    plusGrand = float('-inf')
    for i, nombre in enumerate(L):
        if nombre >= plusGrand:
            plusGrand= nombre
    return plusGrand

#methode en utilisant filter
def second_max1Lambda(L:list) -> float:
    """Renvoie le second plus grand nombre de la liste."""
    if listeidentique(L):
        return None
    else: L2 = list(filter(lambda a: a != maximumListe(L), L))
    return maximumListe(L2)

second_max1Lambda([3, 3, 8, 12, 7, 4, 12, 9, 2])

#parcours de liste classique
def second_max1(L:list) -> float:
    """Renvoie le second plus grand nombre de la liste."""
    if listeidentique(L):
        return None
    else:
        L.remove(maximumListe(L))
        return maximumListe(L)
    
second_max1([x for x in range(0,10)]) #8

#ii
def second_max2(L:list) -> float:
    """renvoie le second plus grand élément de la liste, 
    en effectuant qu'un seul parcours de la liste"""
    if listeidentique(L):
        return None
    else : 
        max1 = max2 = float('-inf') # Valeur très petite 
        for nombre in L:
            if nombre > max1:
                max2 = max1
                max1 = nombre
            elif nombre > max2 and nombre != max1 :
                max2 = nombre
    return max2 if max2 != float('-inf') else None
second_max2([3, 3, 8, 12, 7, 4, 12, 9, 2]) #renvoie bien 9
print(second_max2([1,1,1,1])) #None

#iii
#
def tab_aleatoire(n=10000, N=1024) ->list:
    """Renvoie un tableau de n nombres compris entre 0 et N-1"""
    L = [] 
    for i in range(n):
        L.append(rd.randrange(0,N))
    return L

def benchmark(L=[10, 100, 1000, 10000])->list:
    """Renvoie le temps de calcul des deux fonctions
    et le nombre d'element dans la liste"""
    temps = []
    for valeur in L:

        t0 = time.perf_counter()
        second_max1(tab_aleatoire(valeur))
        t1 = time.perf_counter()
        tSecond_max1 = t1- t0

        t0 = time.perf_counter()
        second_max2(tab_aleatoire(valeur))
        t1 = time.perf_counter()
        tSecond_max2 = t1- t0
        temps.append((valeur,tSecond_max1,tSecond_max2))
    return temps
#benchmark()
"""[(10, 5.360000022847089e-05, 2.480000011928496e-05),
 (100, 0.0009003000000120664, 0.00016320000031555537),
 (1000, 0.10783889999993335, 0.0012808000001314213),
 (10000, 8.986405500000274, 0.012891200000012759)]
 
 On observe que second_max2() est beaucoup plus performant"""

def temps_moy(n):
    Temps1, Temps2 = [], []
    """renvoie la moyenne des temps de calcul des deux fonctions
    pour n elements de la liste"""
    for _ in range(int(10**4/n)+1):
        t0 = time.perf_counter()
        second_max1(tab_aleatoire(n))
        t1 = time.perf_counter()
        Temps1.append(t1-t0)

        t0 = time.perf_counter()
        second_max2(tab_aleatoire(n))
        t1 = time.perf_counter()
        Temps2.append(t1-t0)
    return((st.mean(Temps1),st.mean(Temps2))) #plus lisible
temps_moy(1000)
#(0.10627025454546542, 0.0013746272728150705)

#IV
valeursEssayees = [10**i for i in range(1,6)]  # n = 10^1, 10^2, ..., 10^7
temps_second_max1 = []
temps_second_max2 = []

#On essaie de definir une liste contenant les abscisses
#puis une autre contenant les ordonées
# Mesurer les temps moyens

for n in valeursEssayees:
    moy1, moy2 = temps_moy(n)
    temps_second_max1.append(moy1)
    temps_second_max2.append(moy2)

#Mise en forme Pyplot à l'aide de ChatGPT

plt.figure(figsize=(10, 6))
plt.plot(valeursEssayees, temps_second_max1, label='second_max1()', marker='o')
plt.plot(valeursEssayees, temps_second_max2, label='second_max2()', marker='o')

#échelle logarithmique
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Nombre d\'éléments (n)')
plt.ylabel('Temps moyen d\'exécution (s)')
plt.title('Temps moyen d\'exécution pour second_max1() et second_max2()')
plt.legend()
plt.grid()
plt.show()


#%%============EXERCICE 3=============
#i
import random as rd
def plus_proches(L:list, dist) -> tuple:
     """Prend en argument une liste et une fonction,
     et renvoie le couple d'elements 
     dont la valeur prise par la fonction est 
     la plus faible."""
     couple = (L[0],L[1]) 
     for index, a in enumerate(L):
        for b in L[index+1:]:
            if dist(a,b) <= dist(couple[0], couple[1]):
                couple = (a,b)
            else : pass
     return couple

def dist1(x,y) -> float:
     """Renvoie la distance entre x et y, deux reels"""
     return abs(x-y)

#TEST
L = [k-0.11*k**2 for k in range(31)]
#L décrit le tableau de valeurs de f(x)= (k-0.11)*x^2
print(L)
print(plus_proches(L,dist1)) #(2.24, 2.25)
#le résultat est cohérent, dans la mesure ou la dérivée s'annule en 4.5


#TEST 2 
L2 = [x**2 for x in range(-10,10)]
#D'après la parité de la fonction carrée, il existe 10 couples
#pour lesquels la distance est de 0
print(L2)
print(plus_proches(L2,dist1))
#on obtient le couple (1,1), car il est centré par rapport à l'intervalle étudié

#iii

def taux_diff(ch1,ch2)-> float:
     
     """prend en argument deux chaines de caractères, et renvoie 
     le taux de caractères différents entre les deux listes"""
     card, a = 0, 0
     if len(ch1)< len(ch2):
        l, L = ch1, ch2
     else: l, L = ch2, ch1
     while a < len(l):
        if l[a] == L[a]:
            pass
        else :
            card += 1
        a += 1

     return (card + (len(L)-len(l)))/len(l)

#iv 
Ch = ["myrte", "myrrhe", "myriapode", "tétrapode", "tropaire", "entrisme", "tropisme"]
plus_proches(Ch,taux_diff)
#tropaire, tropisme. (cohérent)
#v
ADN = [[rd.choice(['A', 'T', 'C', 'G']) for _ in range(20)] for _ in range(1000)]
#6
plus_proches(ADN, taux_diff)
#on obtient un tuple de deux listes:
#(['G', 'T', 'T', 'T', 'G', 'G', 'C', 'C', 'A', 'G', 'C', 'T', 'T', 'C', 'T', 'C', 'T', 'A', 'C', 'G'], 
# ['G', 'A', 'T', 'T', 'G', 'A', 'C', 'C', 'A', 'G', 'C', 'T', 'T', 'A', 'T', 'C', 'T', 'G', 'A', 'G'])
#On remarque qu'elles sont semblables 


#7

def plus_proches_dist(L,dist):
   """Renvoie la distance la plus courte entre deux elements,
   ainsi le couple des deux elements """
   return plus_proches(L, dist), dist(plus_proches)

#%%8 On vise une complexité meilleure que quadratique: 
# C'est à dire, dans le pire des cas, linéarithimique , ie O(n*log(n))
def plus_proches_flottants(L:list)->tuple:
    """Prend en argument une liste de flottants, et renvoie
    le couple ayant la plus petite distance A,B"""
    L.sort()
    distance = float('+inf')
    couple = ()
    for i in range(0,len(L)-1):
        #la boucle est de complexité O(n), négligeable devant O(nlog(n))
        if abs(L[i]-L[i+1])<distance:
            couple = (L[i],L[i+1])
        else: pass
    return couple

L = [rd.randrange(-40,100) for x in range(100)]
plus_proches_flottants(L)




   
    
#%%===========EXERCICE 4===============
#i
def enleve(L:list, element):
    """prend en paramètre une liste et un élement, 
    et renvoie la liste privée de la première occurence
    de l'élément"""
    if element not in L:
        pass
    else:
        count = 0
        liste = []
        while L[count]!= element:
            liste.append(L[count])
            count += 1
        for i in range(count+1, len(L)):
            liste.append(L[i])
        L[:]=liste

L = [3,5, 6, 2, 8, 9, 4] 
enleve(L,5) # la liste contient l'element
#print(L)
#[3, 6, 2, 8, 9, 4]

enleve(L, "element non contenu")
print(L)

#ii
def dernier(L:list)->list:
    """enleve le dernier argument de la liste en paramètre"""
    liste = []
    for i in range(0,len(L)-1):
        liste.append(L[i])
    L[:]= liste

L = [3,5, 6, 2, 8, 9, 4] 
dernier(L)
print(L)
#[3, 5, 6, 2, 8, 9]

#iii
def miroir(L:list) -> list:
    """Change la liste donnée en argument par son miroir"""
    liste = []
    for i in range(1, len(L)+1):
        liste.append(L[-i])
    L[:]= liste
L_impaire= [3,5, 6, 2, 8, 9, 4] #nombre de termes impairs
miroir(L_impaire)
print(L_impaire)
#[4, 9, 8, 2, 6, 5, 3]
L_pair = [3,5, 6, 2, 8, 9, 4,2]
miroir(L_pair)
print(L_pair)
#[2, 4, 9, 8, 2, 6, 5, 3]


#%%===========EXERCICE 5============

def isSymetrical(L:list) -> bool:
    """prend une liste, et renvoie si elle est symétrique ou non"""
    for i in range(0, int(len(L)/2)):
        if L[i]==L[-i-1]:
            pass
        else: return False
    return True
print(isSymetrical([2,5,7,7,5,2])) #Nombre pair d'éléments True
print(isSymetrical([2,5,7,8,7,5,2]))#Nombre impair d'éléments True
print(isSymetrical([2,5,7,8,4,5,2])) #False, nombre impair d'éléments

#La fonction est de complexité linéaire dans le pire des cas, 
#dans la mesure ou la sortie de la boucle est immédiate à la découverte du 
#terme non symétrique
#%% ==========Exercice 6============
#Je copie des fonction précédentes, car il n'est pas possible d'appeler ces 
#fonctions dans la cellule
#1===========================
def listeidentique(L:list) -> bool:
    """renvoie True si la liste est identique"""
    for i in range(len(L)):
        if L[i] != L[0]:
            return False
        else: pass
    return True

def max_et_min1(L:list)->tuple:
    """Renvoie Le max et min d'une liste sous forme de tuple"""
    if listeidentique(L) or len(L)==1:
        return (L[0], L[0])
    else: 
        plusGrand = float('-inf')
        plusPetit = float('inf')

        for i, nombre in enumerate(L):
            if nombre >= plusGrand:
                plusGrand= nombre
            if nombre <= plusPetit:
                plusPetit = nombre
    return (plusPetit, plusGrand)
    
max_et_min1([3,7,2,5,8,2,7, -12, 18])
#(-12,18)

#===============2

def max_et_min2(L: list) -> tuple:
    """ Prend en argument une liste et renvoie un tuple
    composé d'abord de son min, puis de son max

    Compare les éléments de la liste deux à deux
    """
    if len(L) == 1 or listeidentique(L):
        return (L[0],L[0])

    if L[0] < L[1]:
        minListe, maxListe = L[0], L[1]
    else:
        minListe, maxListe = L[1], L[0]

    for i in range(2, len(L) - 1, 2):
        if L[i] < L[i + 1]:
            minListe = min(minListe, L[i])
            maxListe = max(maxListe, L[i + 1])
        else:
            minListe = min(minListe, L[i + 1])
            maxListe = max(maxListe, L[i])

    # Si la liste a un nombre impair d'éléments, comparer le dernier élément restant
    if len(L) % 2 == 1:
        minListe = min(minListe, L[-1])
        maxListe = max(maxListe, L[-1])

    return (minListe, maxListe)

# Exemple de test
test_liste = [x for x in range(-10, 10)]
resultat = max_et_min2(test_liste)
resultat
#(-10, 9)
#max_et_min2([1])
#(1,1)

#iii


def max_et_min1_comparaisons(n:int)->int:
    """renvoie le nombre de comparaisons effectuées par la fonction 
    max_et_min1() pour une liste de 2**n elements
    """
    L = [rd.randrange(-100,100) for x in range(2**n)]
    count = 0
    if listeidentique(L) or len(L)==1:
        count = 1
        return count
    else: 
        count = len(L)*2
        return(count)
# max_et_min() compare chaque élément avec le plus petit et le plus grand
#element. Il effectue donc 2^n+1 comparaisons
max_et_min1_comparaisons(3)

def max_et_min2_comparaisons(n:int)->int:
    """Renvoie le nombre de comparaisons faites par max_et_min2() pour
    une liste de 2^n éléments
    """
    L = [rd.randrange(-100,100) for x in range(2**n)]
    count = 0
    if len(L) == 1 or listeidentique(L):
        count += 1

    if L[0] < L[1]:
        count +=1
    else:
        count +=1
    for i in range(2, len(L) - 1, 2):
        count +=1
    return count, L
max_et_min2_comparaisons(8)
# on effectue 2^n-1 comparaisons

#IV
#comparons les deux modèles
#la mise en page du graphique est rédigée par ChatGPT
def tab_aleatoire(taille: int) -> list:
    """Génère une liste aléatoire de la taille donnée."""
    return [rd.randint(-1000, 1000) for _ in range(taille)]

def benchmark(fonction1, fonction2, tailles: list) -> tuple:
    """Effectue un benchmark des deux fonctions pour différentes tailles de listes."""
    temps1 = []
    temps2 = []
    
    for taille in tailles:
        liste_test = tab_aleatoire(taille)
        
        # Benchmark max_et_min1
        debut1 = time.perf_counter()
        fonction1(liste_test)
        fin1 = time.perf_counter()
        temps1.append(fin1 - debut1)
        
        # Benchmark max_et_min2
        debut2 = time.perf_counter()
        fonction2(liste_test)
        fin2 = time.perf_counter()
        temps2.append(fin2 - debut2)
    
    return temps1, temps2

# Exécution du benchmark avec des tailles de liste de test
tailles_liste = [10**x for x in range(0, 7)]
temps1, temps2 = benchmark(max_et_min1, max_et_min2, tailles_liste)

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(tailles_liste, temps1, label='max_et_min1()', marker='o')
plt.plot(tailles_liste, temps2, label='max_et_min2()', marker='o')

# Utilisation de l'échelle logarithmique
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Comparaison des temps d\'exécution de max_et_min1() et max_et_min2()')
plt.legend()
plt.grid(True)

# Affichage du graphique
plt.show()
