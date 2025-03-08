# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 13:51:37 2025

@author: antoinelaldjee-derou
"""

from collections import deque

liste = deque(['banane', 'poire','ananas'])

print(liste)
print(type(liste))

class _:
    """depiler tant que c'est pas vide, puis rempiler"""
    
def depiler_rempiler(L:list):
    Conteneur = L[:]
    pileAuxiliaire = []
    a = len(L)
    while L != []:
        L.pop()
        a -= 1


        
        