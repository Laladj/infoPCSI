#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Created By  : Antoine Laldjee--Deroubaix, HX1 
# Created Date: 08/11/2024
# version ='1.0'
# ---------------------------------------------------------------------------
""" TD3 : algorithmes dichotomiques"""  
# ---------------------------------------------------------------------------
from matplotlib import pyplot as plt
import random as rd
import math
import time
from decimal import Decimal
###EXERCICE 1 : recherche dichotomique dans un tableau trié




def recherche_dicho(L,x):
    d,f = 0, len(L)-1
    while f-d >= 0: 
        med = (d+f)//2
        if L[med]<x:
            d = med +1
        elif L[med]==x:
            return med
        else:
            f = med-1
    return None  
    
L1 = [x for x in range(1000)]
print(recherche_dicho(L1,800)) # retourne 800
#a faire : prouver la conservation de l'invariant 

def tab_aleatoire(n:int,N:int)->list:
    """"""
    return [rd.randrange(0,N) for x in range(n)]
tab_aleatoire(10, 10) # tableau de 10 elements entre 0 et 10

#iv
def temps_moy(n:int,N=int(2**20)):
    """"""
    tempsDeCalcul = []
    for _ in range(math.floor((2*10**5)/n)):
        
        x = rd.randrange(N) #nombre aléatoire recherché 
        L1 = tab_aleatoire(n,N)
        L1.sort()

        tempsInit = time.perf_counter()
       
        
        recherche_dicho(L1,x)
        tempsFinal = time.perf_counter()
        
     
        tempsDeCalcul.append(tempsFinal-tempsInit)
        print(tempsDeCalcul)
    return float(sum(tempsDeCalcul)/len(tempsDeCalcul))

abscisses= [int(10**(i/2)) for i in range(1,14)]
ordonnnee= [temps_moy(x, 2**20) for x in abscisses] 



plt.plot(abscisses,ordonnnee)


def expo(k:int, n:int)->int:
    resultat = k
    assert k>=0 and n>=0, "les arguments doivent être positifs"
    for _ in range(n-1):
        resultat *= k
    return resultat
expo(2,3)
"""
2. 
k^50 = k^25*k^25 
or: k^25= k^24 
k^24= k^12*k^12
k^12 = k^6*k^6
k^6= k^3*k^3
k^3 = k^2*k

def expo_rapide(k,n):
    N = n
    tant que k
        

"""
def expo_rapide(k:int,n:int)->int:
    """prend en argument deux entiers, 
    et renvoie k^n en utilisant l'exponentiation rapide"""
    while n>0:
        if n%2==0:
            n = n/2
            k *=k
        if n%2== 1:
            n = n -1
            k *=k
    return k
expo(2,8)

X = [10, 35, 129, 465, 1668, 6000, 21550,77426, 278255, 1000000]
Y1, Y2 =[], []

for element in X:
    tDebut1 = time.perf_counter()
    Y1.append(expo(3,element))
    tFin1 = time.perf_counter()

for element in X:
    tDebut2 = time.perf_counter()
    Y1.append(expo_rapide(3,element))
    tFin2 = time.perf_counter()
print(Y1)
print(Y2)
    
    
    
