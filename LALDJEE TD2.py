#!/usr/bin/python3

#%%=============EXERCICE 1==========

def positivons(L:list):
    """Prend une liste de réels positifs, et renvoie la valeur absolue des elements de la liste"""
    L = [abs(x) for x in L]
    
L = [x for x in range(-5,10)]
positivons(L)
print(L)
#Revoir la phase de Test

#%%

L = [x-0.1 for x in range(-21,22)]
positivons(L)
print(L)
#%%============EXERCICE 2=============
import random as rd
import time
import statistics as st
from matplotlib import pyplot as plt
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
    """Renvoie le maximum d'une liste, déjà écrit précemment, mais nécéssaire pour le dernier script"""
    plusGrand = 0
    for i, nombre in enumerate(L):
        if nombre >= plusGrand:
            plusGrand= nombre
    return plusGrand

def second_max1(L:list) -> float:
    """Renvoie le second plus grand nombre de la liste."""
    if listeidentique(L):
        return None
    else: L2 = list(filter(lambda a: a != maximumListe(L), L))
    return maximumListe(L2)

second_max1([3, 3, 8, 12, 7, 4, 12, 9, 2])

#ii
def second_max2(L:list) -> float:
    """renvoie le second élément de la liste, 
    en effectuant qu'un seul parcourt de la liste"""
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
print(second_max2([1,1,1,1]))

#iii

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

plt.plot()   
    



# %%
#def plus_proches(L, dist)
    
#%%===========EXERCICE 5============

def isSymetrical(L:list) -> bool:
    """prend une liste, et renvoie si elle est symétrique ou non"""
    for i in range(0, int(len(L)/2)):
        if L[i]==L[-i-1]:
            pass
        else: return False
    return True
print(isSymetrical([2,5,7,7,5,2])) #Nombre pair d'éléments
print(isSymetrical([2,5,7,8,7,5,2]))#Nombre impair d'éléments
print(isSymetrical([2,5,7,8,4,5,2])) #False, nombre impair d'éléments




