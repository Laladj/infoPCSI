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
###EXERCICE 1 : recherche dichotomique dans un tableau trié




def recherche_dico(L,x):
    d,f = 0, len(L)
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
print(recherche_dico(L1,800)) #devrait retourner 800
#a faire : prouver la conservation de l'invariant 

def tab_aleatoire(n:int,N:int)->list:
    """"""
    return [rd.randrange(0,N) for x in range(n)]
tab_aleatoire(10, 10) # tableau de 10 elements entre 0 et 10

#iv
#def temps_moy(n:int,N:int):
 #   """"""
#    for _ in range(math.floor((2*10**5)/n)):
        
