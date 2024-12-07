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
import numpy as np
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
    



#exercice 3

def dicho(f:function, a:float , b:float, epsilon:float)->float:
    """renvoie la solution de l'equation f(x)= 0, pour x appartenant à a,b"""
    
    assert f(a)*f(b)<0, "a et b doivent être de signe differents"
    assert epsilon> 0, "epsilon doit etre strictement positif"
    while b-a>epsilon:
        if np.sign(f((a+b)/2)) != np.sign(f(b)):
            a = (a+b)/2
        else:
            b = (a+b)/2
    pointMillieu = (a+b)/2
    #assert f(a)*f(b)>0 , "Erreur"
    return pointMillieu



# Définition des fonctions
def k1(x: float) -> float:
    return x - np.e * np.sin(x)  # x est un angle en radians

def k2(x: float) -> float:
    return x**2 - 6*x + 8  


# affichage du graphique rendu plus lisible par chatGPT
xListe_f = np.linspace(-10, 10, num=1000)
xListe_k2 = np.linspace(0, 3, num=500)  # Intervalle restreint pour k2
yListe_f = k1(xListe_f)
yListe_k2 = k2(xListe_k2)

# Tracé du graphique
plt.figure(figsize=(10, 7))  # Taille du graphique

# Tracer f(x)
plt.plot(xListe_f, yListe_f, label=r"$f(x) = x - e \sin(x)$", color="blue", linewidth=2)

# Tracer k2(x)
plt.plot(xListe_k2, yListe_k2, label=r"$k_2(x) = x^2 - 6x + 8$", color="red", linestyle="--", linewidth=2)

# Ajouter des éléments au graphique
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Ligne horizontale y=0
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)  # Ligne verticale x=0
plt.title("Représentation des fonctions $f(x)$ et $k_2(x)$", fontsize=14, fontweight='bold')
plt.xlabel("x", fontsize=12)
plt.ylabel("Valeurs des fonctions", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Affichage du graphique
plt.show()

##################

print(dicho(k1,-10,10,10**-3))
print(dicho(k2, 0, 3, 10**-3))

#4 
def dicho_iter(f:function, a:float, b:float, epsilon:float):
    assert f(a)*f(b)<0, "a et b doivent être de signe differents"
    assert epsilon> 0, "epsilon doit etre strictement positif"
    compteur = 0
    while b-a>epsilon:
        compteur += 1
        if np.sign(f((a+b)/2)) != np.sign(f(b)):
            a = (a+b)/2
        else:
            b = (a+b)/2
    pointMillieu = (a+b)/2
    #assert f(a)*f(b)>0 , "Erreur"
    return compteur

#----- 

"""
-3 + 2*sqrt(2) est la plus grande racine du polynome k3 : 
cette dernière vaut environ -0,171

A chaque itération, la taille de l'intervalle [0,1] est dvisié par 2
des lors, on cherche le premier terme de la suite géométrique u(n) = (1/2)^n tel que un<(1/2)
on a n < (12*ln(10))/ln(2), soit n = 40

Verifions l'hypothèse
"""
#construisons k3 à l'aide de lambda : 
#cf : https://www.w3schools.com/python/python_lambda.asp

k3 = lambda x : x**2 + 6*x + 1
print(dicho_iter(k3,-1,0, 10**-12))

h = lambda x: (10**-8)*x**2- (4/5)*x + 10**-8


