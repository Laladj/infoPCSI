#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Created By  : Antoine Laldjee--Deroubaix, HX1 
# Created Date: 21/12/2024
# version ='1.0'
# ---------------------------------------------------------------------------
""" DM5 """  
# ---------------------------------------------------------------------------

def maxi_partiel(L: list, i: int) -> int:
    """
    Renvoie le maximum de la sous-liste L[:i] par récursivité
    
    Args:
        L (list[int]): Liste d'entiers naturels.
        i (int): Longueur de la sous-liste à examiner.
        
    Returns:
        int: Le maximum de la sous-liste L[:i].
    """
    if i == 1:
        return L[0]
    m = maxi_partiel(L, i - 1)
    return m if m > L[i - 1] else L[i - 1]

def maxi(L: list) -> int:
    """
    Renvoie le maximum d'une liste non vide d'entiers naturels.
    
    Args:
        L (list[int]): Liste non vide d'entiers naturels.
        
    Returns:
        int: Le maximum de la liste.
        
    
    """
    assert len(L) != 0, "La liste ne peut pas être vide"
    return maxi_partiel(L, len(L))

# Tests
assert maxi([3, 7, 2, 9, 4]) == 9
assert maxi([1]) == 1
assert maxi([10, 5, 8, 10]) == 10
assert maxi([0, 0, 0]) == 0
assert maxi([100, 50, 200, 150]) == 200


#%%EXERCICE 2
import math
import random as rd
#i
def plus_grand_produit_successif_naif(ch:str, p:int):

    plus_grand = math.prod([int(ch[x]) for x in range(p)])
    #on definit le maximum comme le produit des trois premiers entiers
    #adjacents
    for chiffre in range(len(ch)-p+1):
        produit =  math.prod([int(ch[x+ chiffre]) for x in range(p)])
        #print(produit)
        if produit >plus_grand:
            plus_grand = produit
    return plus_grand

assert plus_grand_produit_successif_naif("68570982",3) == 280

print(plus_grand_produit_successif_naif(str(2**10000), 14)) #731398864896

#ii 
"""Dans le pire des cas (celui ou les p derniers entiers de la chaine
répondraient à la condition), 
Supposons que la complexité de la multiplication d'un entier de taille
 n est
de n log n :
Source : https://www.polytechnique.edu/actualites/complexite-de-la-multiplication-joris-van-der-hoeven-recompense


si l'on augmente la taille de la liste de 1 : la fonction effectue un 
produit
de deux entiers entre 1 et 10 et une comparaison en plus : C(n+1)= C(n)+1

En augmentant p de 1, on effectue n-p produits d'entiers 
"""

#j'ai demandé a chatGPT de m'expliquer l'énoncé du problème


def plus_grand_produit_successif(ch, p):
   
    max_produit = 0  # Le plus grand produit trouvé
    produit = 1      # élément neutre du produit
    nb_sans_zeros = 0  # Nombre de chiffres non nuls consécutifs dans 
                        #la fenêtre
    en_construction = True  # Indique si le produit est valide ou doit 
                            #être reconstruit


    for i in range(len(ch)):
        chiffre = int(ch[i])  # Convertit le caractère en entier

        if chiffre == 0:

            en_construction = False
            produit = 1
            nb_sans_zeros = 0
        else:

            produit *= chiffre
            nb_sans_zeros += 1


        if nb_sans_zeros > p:

            produit //= int(ch[i - p]) # division entière avec affectation

        if nb_sans_zeros >= p and en_construction:

            max_produit = max(max_produit, produit)
        elif nb_sans_zeros >= p:

            en_construction = True
            max_produit = max(max_produit, produit)

    return max_produit
assert plus_grand_produit_successif("68570982",3) == 280
#iv
"""On obtient une meilleure complexité que précédemment, due
 a la gestion des 0"""

#v
#Methode naïve
# nombres = ""
# for _ in range(10**6):
#     nombres += str(rd.randrange(0,10))
# print(nombres)

#après recherche sur StackOverflow

nombres = ''.join(rd.choices('0123456789', k=10**6))
print(nombres)
print(plus_grand_produit_successif(nombres, 1000))

# on obtient 0 De fait, dans une chaine de 100 nombres, 
# la loi binomiale nous indique une probabilité
# de ne jamais obtenir 0 est 1 - P(x=0) = 0 (très proche de 0)
nombresSansZero = ''.join(rd.choices('123456789', k=10**6))
#print(nombresSansZero)

print(plus_grand_produit_successif(nombresSansZero, 1000))
#le résultat comporte 656 chiffres. On remarque un grand nombre de zero
# à la fin de l'entier




# %% Problème 1: le système MIU
import random as rd #pour règle3
#question 1
def regle1(mot:str)->str:
    """Args : str->str
        transforme la chaine mot se terminant par I en la chaîne 
        mot + ”U” """
    assert mot != "", 'La chaîne passée en argument doit être non vide'
    #mot =mot.upper() #passe le mot en majuscule
    if mot[-1] == "I":
        mot += "U"
        return mot
    return None
assert  regle1("MI") == "MIU"
assert regle1("MU") == None   
#regle1("") #AssertionError: La chaîne passée en argument doit être 
# non vide

def regle2(mot:str)->str:
    """Args : str -> str
    prend en argument unique une chaîne de caractères tous égaux à
      ”M”, ”I” ou ”U”, représentant
    un mot du système MIU, et qui renvoie le mot produit
    par application unique de la règle no 2 si cette règle est applicable,
    et rien sinon.
    """
    #mot.upper()
    if mot[0] == "M":
        mot += mot[1:]
        return mot
    return None
assert regle2("MIU") == "MIUIU"
assert regle2("IUIUI") == None

def regle3(mot:str)->list:
    #mot = mot.upper()
    output = []
    for i in range(0,len(mot)-2):
       
        if mot[i:i+3] == "III":
            motRegle3 = mot[:i] + "U" + mot[i+3:]
            if motRegle3 not in output:  
                output.append(motRegle3)
    return output if output != [] else None

assert regle3("MIIII") == ['MUI', 'MIU']
assert regle3("MIII") == ['MU']


def regle4(mot:str)->list:
    output =[]
    for lettre in range(0,len(mot)-1):
        if mot[lettre:lettre+2] =="UU":
            motRegle4 = mot[:lettre] + mot[lettre+2:]
            if motRegle4 not in output:  
                output.append(motRegle4)
    return output if output != [] else None

assert regle4("MUUIIUUUI") == ['MIIUUUI', 'MUUIIUI']

#Question 5


def theoremes_MIU(n:int)->list: #version "brute"
    if n<= 1:
        return ['MI']
    else:
        output = ['MI']
        curseur = 0
        while len(output) < n+1:
            compteur_en_formation =len(output)
            
            output.append(regle1(output[curseur]))
            output.append(regle2(output[curseur]))
            output.append(regle3(output[curseur]))
            output.append(regle4(output[curseur]))
            output  = list(filter(lambda x:x is not None, output))
    #https://www.geeksforgeeks.org/python-remove-none-values-from-list/
            
            curseur += 1
    return output
            
print(theoremes_MIU(8))

def est_un_theoreme_MIU(n:int, ch:str)->int:
    """Args : int, str -> int
    prend en argument un entier n et une chaîne de caractères ch du système
    MIU, et qui renvoie le nombre minimal d’étapes nécessaires 
    pour la production de ch à partir de l’unique axiome 
    ”MI”, si la chaîne ch est
    atteignable en moins de n étapes à partir de ”MI”, et rien sinon. """
    r1, r2, r3, r4 = 0,0,0,0
    
            









# %%
