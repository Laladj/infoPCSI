#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Created By  : Antoine Laldjee--Deroubaix, HX1 
# Created Date: 08/11/2024
# version ='1.0'
# ---------------------------------------------------------------------------
""" TD4: Fonctions récursives"""  
# ---------------------------------------------------------------------------

#exercice 1

def calcul_u1(n):
    if n == 0:
        return 2
    else:
        return (2/3)*(calcul_u1(n-1)+(2/(calcul_u1(n-1)**2)))
#calcul_u1(8)
#calcul_u1(100)

def calcul_u2(n:int)->float:
    """"""
    if n == 0:
        return 2
    else:
        r = calcul_u2(n-1)
        return 2/3 * (r + (2/r**2))
assert calcul_u1(5)== calcul_u2(5)

print(calcul_u2(100))
#il est possible d'afficher calcul_u2(100), mais le temps d'execution
#de calcul_u1(100 ) est trop long

def expo_recursif(x:float,n:int)->int:
    assert type(n) == int and n>= 0, 'n doit être un entier positif'
    if n == 0: return 1
    else:
        r = x
        return r * expo_recursif(x,n-1)
assert expo_recursif(2,4) == 16


def miroir(chaine:str)->str:
    pass

#%%exercice 2: Flocon de van Koch
#%%exercice 2: Flocon de van Koch
import turtle
from turtle import *

def cote(n:int, longueur:float):
    t = Turtle()
    if n == 0:
        t.forward(longueur)
    else:
        longueur /= 3.0
        cote(n-1, longueur)
        t.left(60)
        cote(n-1, longueur)
        t.right(120)
        cote(n-1, longueur)
        t.left(60)
        cote(n-1, longueur)

def flocon_de_van_koch(n:int, longueur:float):
    t = Turtle()
    t.speed(0)
    for _ in range(3):
        cote(n, longueur)
        t.right(120)
    done()

# Exemple d'utilisation:
flocon_de_van_koch(3, 300)



# %% EXERCICE 5

""" Decompositions de 4: on ne prend pas en compte l'ordre des éléments
    [ [1,1, 1, 1], [1,1,2], [2,2] ]"""
    


# %%
