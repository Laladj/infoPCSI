#!/usr/bin/python
"""Antoine Laldjee-Deroubaix, HX1 
=================DM 2============="""

import math
import random as rd

#Question 1
#2
# On note que ord("L") != ord("l")
def codage(mot:str)->list:
    """renvoie le code Unicode de chacune des lettres du mot donné
    en argument"""
    L = [ord(x)for x in mot]
    return L
#3
coefficients= codage("AntoineLaldjee")
n = len(coefficients)

#4 
donnees_initiales_brutes = [ord(x) for x in "Lantoine"]
print(donnees_initiales_brutes)
#5
donnees_initiales = [x-85 for x in donnees_initiales_brutes]
print(donnees_initiales)

#================Question 2
def pgcd(a, b) -> int:
    """Renvoie le pgcd des deux entiers"""
    if a == 0 or b == 0:
        return 0
    else:
        while a != b:
            if a < b:
                a, b = b, a
            a, b = b, a - b
    return a

# pgcd(72,32)
# pgcd(0,0)
pgcd(0,3)
#2

def poly_Euclide(L:list)->int: 
	"""Renvoie le plus grand entier qui divise
	tous les entiers de la liste"""
	c = pgcd(L[0],L[1])
	for i in range(2, len(L)):
		c = pgcd(c,L[i])
	return c
L = [12, 24, 27, 30, 36]

poly_Euclide(L) #3

#iii
def modif(L:list)->list:
     """Prend en argument une liste d'entiers,
     et change le dernier element par 1"""
     liste = L
     liste[-1]= 1
     L[:]= liste
L = [x for x in range(0,5)]
modif(L)
print(L) #[0, 1, 2, 3, 1]

#iv
print(poly_Euclide(coefficients)) #on obtient bien 1
#%%
#v
def troncation_a_la_plus_courte(L1,L2)->tuple:
     """renvoie la troncation des deux listes passees 
     en parametre"""
     if len(L1) <= len(L2):
          return (L1, L2[:len(L1)])
     else:
          return (L1[:len(L2)],L2)

L1 = [x for x in range(1,10)]
L2 = [x for x in range(10,20)]
troncation_a_la_plus_courte(L1,L2) #([1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18])

#============Question 3==========

#i
def suite_liste(L1,L2, n):
    """Renvoie la liste n premiers termes de la suite récurrente (de 0 à n-1)
    linéaire, prenant en L1 les coefs des termes, et L2 la suite associée.
    
    Les listes sont tronquées si elle n'ont pas la même taille, """
    L = []
    troncation_a_la_plus_courte(L1,L2)
    for i in range(0,len(L1)):
         L.append(L1[i]*L2[i])
    return L
#on teste la fonction avec une suite géometrique: 
L1 = [2 for i in range(10)]
L2 = [x for x in range(0,10)]
print(L1,L2)
suite_liste(L1,L2,9)

# %%
