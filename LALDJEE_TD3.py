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
###EXERCICE 1 : recherche dichotomique dans un tableau trié

def recherche_dico(L:list, x:int)->int:
    """ Argument
        L :liste d'entiers rangés dans l'ordre
        x : entier comparable à L
        renvoie la position """
    f, g = L[0], L[-1]
    mod = 0
    while f-g > 1:
        mod=(f+g)//2
        if L[mod]==x:
            return mod
        elif L[mod]<x:
            g = g//2
        elif L[mod]>x:
            f + g//2
    return mod

test = [x for x in range(2024)]
recherche_dico(test,30)