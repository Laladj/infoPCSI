#!/usr/bin/env python3.8.2  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
"""
Created By  : Antoine Laldjee--Deroubaix, HX1 
Created Date: 11/18/2024
version ='1.0'
"""
# ---------------------------------------------------------------------------
""" TD 7 : Algorithmes Gloutons. """  
# ---------------------------------------------------------------------------
#%%exercice 1

#i

collection = {252:71, 1:2103, 12:310, 240: 150}

def nb_pieces(dictionnaire:dict)->int:
    """Args : dict(*int)
        returns : int
        renvoie la somme des elements d'un dictionnaire d'entiers"""
    return sum(collection) # a revoir, 

nb_pieces(collection)

#iii
collection[12] += 2
collection[48] = 2
assert collection[12] == 312 and collection[48] == 2

#iv

def somme(dico:dict)->int:
    """renvoie la valeur faciale de la collection"""
    valeur = 0
    for i,j in dico.items():
        valeur += i*j
    return valeur
somme(collection) #59845

#%%exercice 2 : problème du rendu de monnaie. 
import decimal

def repartition(S:int, pieces:list)->tuple:
    #Sfinale = S #on verifiera si Sfinale == S
    
    i = len(pieces) - 1
    nombrePieces = 0 
    dictionnaire = {}
    while i >= 0:
        if S >= pieces[i]:
            nombrePieces = S//pieces[i]
            S = S % pieces[i]
            dictionnaire[pieces[i]] = nombrePieces
        i -= 1
    return(dictionnaire, S == 0)

    



#testset 
euros_ent  = [1, 2, 5, 10, 20, 50, 100, 200, 500,]

#assert repartition(1240, euros_ent) == ({1000: 1, 200: 1, 20: 2}, True)

eurosSansLesCentimes = [100, 200, 500, 1000, 2000,5000]
repartition(4100, eurosSansLesCentimes) #la solution est optimale.

monnaieImaginaire = [2, 4, 16, 32]

assert repartition(1243, monnaieImaginaire)== ({32: 38, 16: 1, 4: 2, 2: 1}, False)

 #iii 
anglais_simplifie = [1, 3, 4, 6, 12]
assert repartition(8,anglais_simplifie) == ({6: 1, 1: 2}, True)
#on aurait préféré 8 = 4+4. l'algorithme rend donc 3 pièces au lieu de 2,
#il s'agit d'un cas ou la réponse est sous-optimale

#iv

assert repartition(0,euros_ent) == ({}, True)

#4: euros

euro = [0.01,0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100, 200, 500]
# toutes les pièces en fonction de leur valeur faciale en euros. 
repartition(8.95,euro)
#certaines valeurs de pièces de monnaie sont des flottants, ainsi, le nombre
#de pièces de monnaie affiché dans le dictionnaire est converti en flottant.


# Ainsi, lors de l'operation modulo,
#on obtient ces valeurs successives de S :
# =============================================================================
# 3.9499999999999993
# 1.9499999999999993
# 0.9499999999999993
# 0.4499999999999993
# 0.04999999999999927
# 0.009999999999999266
# =============================================================================

#on observe donc que la dernière valeur est inférieure à 5 centimes d'euro,
#donc le script sort de la boucle sans avoir soustrait le dernier centime

#on va donc arrondir la valeur de S a chaque itération

def repartitionBis(S:int, pieces:list)->tuple:
    #Sfinale = S #on verifiera si Sfinale == S
    
    i = len(pieces) - 1
    nombrePieces = 0 
    dictionnaire = {}
    while i >= 0:
        if S >= pieces[i]:
            nombrePieces = S//pieces[i]
            S = S % pieces[i]
            S = round(S,3) #modification
            
            print(S)
            dictionnaire[pieces[i]] = nombrePieces
        i -= 1
    return(dictionnaire, S == 0)
repartitionBis(8.95, euro)

#on obtient finalement : ({5: 1.0, 2: 1.0, 1: 1.0, 0.5: 1.0, 0.2: 
#2.0, 0.05: 1.0}, True)

# =============================================================================
# #5. 
# =============================================================================

def repartition_dyn(S:float,pieces:list)->list:
    """args : S : montant de la monnaie à rendre
         pieces : système monétaire à prendre en compte
         
       returns : chaque element de la liste est associé à la position de
       la pièce de monnaie"""
    pass
       
#%% Exercice 3 : Problème du sac à dos
from itertools import product

def masse(objet:tuple)->float:
    """args : tuple : (nom, masse, valeur)
      returns : float : masse"""
    return objet[1]

def valeur(objet:tuple)->float:
    """args : tuple : (nom, masse, valeur)
      returns : float : valeur"""
    return objet[2]

def rapport_valeur_masse(objet:tuple)->float:
    """args : tuple : (nom, masse, valeur)
      returns : float : valeur/masse"""
    return objet[2]/objet[1]


#2

liste2 = [('tente', 14, 126),('sac_de_couchage',2, 32), ('réchaud', 5, 20),
          ('livre', 1, 5), ('ordinateur', 6,18), ('mini_frigo',8, 80)]
#trier les objets par ordre croissant d'efficacité ? demander au prof
def sac_a_dos_glouton(objets:list, masse_max:float ,critere)->list:
    
    # tri : construction d'un dictionnaire trié en fonction du critère
    
    """
    

    Parameters
    ----------
    objet : list
        DESCRIPTION.
    masse_max : float
        DESCRIPTION.
    critere : TYPE
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    if critere == masse:#on trie la liste de façon croissante, on cherche le
                        #poids le plus léger
        objets_triés = sorted(objets, key=critere, reverse = False)
        
    if critere == valeur or critere == rapport_valeur_masse: #tri décroissant
        objets_triés = sorted(objets, key=critere, reverse = True)
        
    sac, masse_totale, valeur_totale = [], 0, 0
    
    for objet in objets_triés:
        if masse_totale + objet[1] <= masse_max:
            sac.append(objet[0])
            masse_totale += objet[1]
            valeur_totale += objet[2]
    return sac, valeur_totale
    
#sac_a_dos_glouton(liste2, 30, masse)
#(['livre', 'sac_de_couchage', 'réchaud', 'ordinateur', 'mini_frigo'], 155)

sac_a_dos_glouton(liste2, 30, valeur)
#(['tente', 'mini_frigo', 'sac_de_couchage', 'réchaud', 'livre'], 263)

#on retrouve bien les valeurs de l'énoncé

#force brute

#3

# =============================================================================
# pour simplifier les idées, considérons un ensemble à deux elements , A et B. 
# 
# Des lors, il est possible de former 4 parties : [A,B], [A, non B], [Non A, B]
# et enfin [non A, non B]
# 
# dans chaque sous-liste, le booleen à l'index i decrit la présence ou non du
# I eme element de l'ensemble'
# =============================================================================
# =============================================================================
# 
# def ens_des_parties(n:int)->list[list[bool]]:
#     """
# 
# 
#     Parameters
#     ----------
#     n : int
#         nombre de parties d'un ensemble.
# 
#     Returns
#     -------
#     list[list[bool]]
#         ensemble des parties d'un ensemble.
# 
#     """
#     liste_base = [[False]*n]
#     sous_liste_base = [False]*n
#     for i in range(0,n-1):
#         sous_liste_base[i] = True
#         liste_base.append(sous_liste_base)
#     return liste_base
# ens_des_parties(2)
#     
# =============================================================================
    # Je n'ai pas abouti
def ens_des_parties(n:int)->list:
    return list(product([False, True], repeat= n))

ens_des_parties(2)


    
# =============================================================================
# 
# def sac_a_dos_force_brute(objets:tuple,P:float):
#     """
#     
# 
#     Parameters
#     ----------
#     objets : list
#         DESCRIPTION.
#     P : float
#         décrit le poids total du sac à dos.
# 
#     Returns
#     -------
#     list.
# 
#     """
#     #I. fabrication de toutes les listes
#     liste_de_sous_listes_de_tuples = []
#     sous_liste = []
#     meilleur_sac_a_dos = ()
#     #construisons l'ensemble des possibilités
#     toutes_les_possibilites = ens_des_parties(len(objets)) #liste 
#     for element in toutes_les_possibilites:
#         for indice_booleen in range(len(element)):
#             print(indice_booleen)
#             if toutes_les_possibilites[indice_booleen] == True:
#                 sous_liste.append(objets[indice_booleen])
#         liste_de_sous_listes_de_tuples.append(sous_liste)
#         sous_liste = [] #on efface la sous liste
#     print(liste_de_sous_listes_de_tuples)
#     #II. construction de score
#     
#     for liste_objets in liste_de_sous_listes_de_tuples: 
#         if masse(liste_objets)<= P and valeur(liste_objets) >valeur(meilleur_sac_a_dos):
#             meilleur_sac_a_dos = liste_objets
#     return meilleur_sac_a_dos
# 
# sac_a_dos_force_brute(liste2, 30) 
# 
# =============================================================================

        
def sac_a_dos_force_brute(objets: list, P: float):
    """
    

    Parameters
    ----------
    objets : list
        DESCRIPTION.
    P : float
        DESCRIPTION.

    Returns
    -------
    noms_objets : TYPE
        DESCRIPTION.
    TYPE
        DESCRIPTION.

    """
    toutes_les_possibilites = ens_des_parties(len(objets))
    
    meilleur_sac = []
    meilleure_valeur = 0

    for combinaison in toutes_les_possibilites:
        sac = []
        masse_totale = 0
        valeur_totale = 0
        
        for i in range(len(objets)):
            if combinaison[i] == True:  
                sac.append(objets[i])
                masse_totale += masse(objets[i])
                valeur_totale += valeur(objets[i])

        if masse_totale <= P and valeur_totale > meilleure_valeur:
            meilleur_sac = sac
            meilleure_valeur = valeur_totale

    
    noms_objets = []
    for obj in meilleur_sac:
        noms_objets.append(obj[0])

    return noms_objets, meilleure_valeur  # Retourner les noms des objets et la valeur totale


assert sac_a_dos_force_brute(liste2, 30) == (['tente', 'sac_de_couchage', 
                                              'réchaud', 'livre',
                                              'mini_frigo'], 263)

#on observe qu'on obtient 
            
      
      


