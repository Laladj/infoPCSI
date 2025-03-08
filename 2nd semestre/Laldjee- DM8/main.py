#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
"""Antoine Laldjee--Deroubaix, HX1
    TD8 :  Comptage par dictionnaires, diagrammes, analyse quantitative"""
# Created Date: 11/03/2025
# version ='1.0'
#
# ---------------------------------------------------------------------------

#%% exercice 0
""" texte1= open("rougon.txt")
texte2, texte3 = open("a_se_tordre.txt"), open("tristram_shandy.txt")

print(texte1[5]) """
#on utilise une rawstring pour le chemin du fichier :
# https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3

#chemins : 
chemin_texte1 = r"C:\Users\antoinelaldjee-derou\Desktop\python\2nd semestre\Laldjee- DM8\rougon.txt"
chemin_texte2 = r"C:\Users\antoinelaldjee-derou\Desktop\python\2nd semestre\Laldjee- DM8\a_se_tordre.txt"
chemin_texte3 = r"C:\Users\antoinelaldjee-derou\Desktop\python\2nd semestre\Laldjee- DM8\tristram_shandy.txt"
with open(chemin_texte1, 'r') as file:
    texte1 = file.read()

with open(chemin_texte2, 'r') as file:
    texte2 = file.read()
    
with open(chemin_texte3, 'r') as file:
    texte3 = file.read()

Textes = [texte1, texte2, texte3]
# =============================================================================
# Recherche succinte : 
# Texte 1 : Emile Zola, la fortune des Rougons
# Texte 2 : A SE TORDRE
# Histoires chatnoiresques
# APHONSE ALLAIS
# (1891)
# Texte 3: Vie et opinions de Tristram Shandy, Laurence Sterne
# =============================================================================

#%%Exercice 1 : Profils des distributions alphabétiques
from string import ascii_lowercase
import matplotlib.pyplot as plt
#cf table ASCII
from statistics import stdev, mean
from scipy import optimize

def profilage_texte(texte:str)->dict:
    """
    

    Parameters
    ----------
    texte : str
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.

    """
    texte = texte.lower()
    dictionnaire = {}
    for caractere in texte:
        if ord(caractere) >= 97 and ord(caractere)<= 122:
            if caractere in dictionnaire:
                dictionnaire[caractere] += 1
            else:
                dictionnaire[caractere] = 1
                
            
    return dictionnaire
profilage_texte('Toute initiale du monde')

#2. 
profils = [profilage_texte(x) for x in Textes]

#3. 

def max_dico(dictionnaire):
    valeur_max = -1
    cles_max = []

    for cle, valeur in dictionnaire.items():
        if valeur > valeur_max:
            valeur_max = valeur
            cles_max = [cle]
        elif valeur == valeur_max:
            cles_max.append(cle)

    return valeur_max, cles_max

dico={'e': 3, 'f': 2,'g': 3}
max_dico(dico)            
            
lettre_les_plus_communes = [max_dico(dico) for dico in profils]
print(lettre_les_plus_communes)
#[(82731, ['e']), (24638, ['e']), (89579, ['e'])]
#sans grande surprise, le "e" est la lettre la plus présente

#fun fact : le livre "la disparition" de Georges Perec ne comporte pas
#la lettre e

#5

def frequences(dico:dict)->None: 
    """
    

    Parameters
    ----------
    dico : dict
        DESCRIPTION.

    Returns
    -------
    None

    """
    total_valeurs = sum(dico.values())
    for cle, valeurs in dico.items():
        
        dico[cle] = valeurs/total_valeurs
    return dico #je ne parviens pas à faire fonctionner le script sinon
    
#6
def normalisation(dico:dict)->list[tuple]:
    """
    

    Parameters
    ----------
    dico : dict
        DESCRIPTION.

    Returns
    -------
    list[tuple]
        fabrique une liste de tuples (lettre, nombre d'apparition) 
        les lettres sont rangées dans l'ordre alphabétique.

    """
    liste_tuples = []
    for i in range(97, 97+27):
        liste_tuples.append((chr(i),0)) #[("a",0),("b",0)...]
    
         
    for index, couple in enumerate(liste_tuples):
        if couple[0] in dico:
            liste_tuples[index] = (couple[0], dico[couple[0]])
        else:
            liste_tuples[index] = (couple[0], 0)
    return liste_tuples
            
            

#print(normalisation(dico))
# =============================================================================
# #7
# =============================================================================

# =============================================================================
profils = [normalisation(element) for element in profils]
#     
# #formation de trois graphiques
# #cf https://stackoverflow.com/questions/18458734/how-do-i-plot-list-of-tuples
# def graphique(liste_de_points:list):
#     frequences(liste_de_points)
#     plt.bars(*zip(*liste_de_points))
#     plt.ylabel('fréquence d apparition')
#     plt.plot()
# 
# for listes in profils:
#     graphique(listes)
# 
# =============================================================================

#Fait avec ChatGPT (jpp oskour je vais deceder)



def tracer_frequences(profils):
    """
    Affiche trois diagrammes en barres représentant les fréquences des lettres pour chaque profil.

    Parameters
    ----------
    profils : list[list[tuple]]
        Liste contenant trois profils, chaque profil étant une liste de tuples (lettre, fréquence).
    """
    fig, axes = plt.subplots(1, len(profils), figsize=(15, 5))  # Création de sous-graphiques
    frequences = frequences(profils)
    
    for i, profil in enumerate(profils):
        lettres, frequences = zip(*profil)  # Extraction des lettres et de leurs fréquences
        
        # Tracé du diagramme en barres
        axes[i].bar(lettres, frequences, color='skyblue', edgecolor='black')
        axes[i].set_title(f"Texte {i+1}")  # Titre du graphique
        axes[i].set_xlabel("Lettres")
        axes[i].set_ylabel("Nombre d'occurrences")

    plt.tight_layout()  # Ajuste l'affichage
    plt.show()

# Exemple d'utilisation



tracer_frequences(profils)

# =============================================================================
# 8
# =============================================================================

#i

profil_texte1, profil_texte2, profil_texte3 = profils[0], profils[1],profils[2]

#ii
def second_element(couple:tuple):
    return couple[1]

profil_texte1.sort(key = second_element,reverse=True)
profil_texte2.sort(key = second_element,reverse=True)
profil_texte3.sort(key = second_element,reverse=True)

#iii 
# =============================================================================
# pour les deux premiers, e, a et s sont les lettres les plus présentes, tandis
# que pour texte3, Tristram Shandy, il s'agit des lettre e, t et o.'
# En effet, Tristram Shandy est écrit en anglais, et non en français. C'est
# pourquoi les lettres les plus courantes sont differentes
# 
# =============================================================================


#iv

#v

#%% Exercice 3:
    
#1
def dico_mots(chaine:str)->dict:
    '''
    

    Parameters
    ----------
    chaine : str
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    #on suppose que la chaine de caractère est ecrite en francais; 
    #on distingue les mots par les espaces qui les séparent. 
    #on ne prend pas en compte les caractères speciaux
    dictionnaire = {}
    chaine_casse = chaine.lower()
    phrase_liste = chaine_casse.split()
    mot = ""
    for caractere in phrase_liste:
        print(caractere)
        if caractere != " " or caractere != ".":
            mot += caractere
        else:
            if mot in dictionnaire:
                dictionnaire[mot] += 1
            else:
                dictionnaire[mot] = 1
            mot =""
    
    if mot:
           if mot in dictionnaire:
               dictionnaire[mot] += 1
           else:
               dictionnaire[mot] = 1

    return dictionnaire 

print(dico_mots("banane banane"))

