#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:55:49 2021

@author: Jérôme Levie
"""

import matplotlib.pyplot as plt
from copy import deepcopy



# %% ============================= Partie I =================================


def ecrire_pbm(mat: list, nom: str):
    """prend en arguments une liste de listes de même taille, dont les éléments
    sont des 0 et des 1 (entiers, ou caractères), et une chaîne de caractères nom. 
    Ne renvoie rien. Crée, dans le répertoire de travail, le fichier bpm 
    correspondant aux pixels indiqués par la matrice, en le nommant nom.pbm."""
    h = len(mat)
    l = len(mat[0])
    nom = nom + '.pbm'
    f = open(nom, 'w')
    f.write('P1' + str(l) + ' ' + str(h) + '\n')
    for i in range(h):
        for j in range(l):
            bit = str(mat[i][j])
            f.write(bit + ' ')
        f.write('\n')
    f.close()


# %% ============================= Partie II ================================


image1 = plt.imread("ecureuil.jpg").tolist()
copie1 = deepcopy(image1)
plt.imshow(image1)
plt.show()


# %% ==================== Exercice 0 ======================


def inverse_nb(image):
    """Prend en argument une matrice représentant une image, de type non spécifié
    (liste de listes, ou tableau numpy bi-dimensionnel), chaque pixel étant
    codé par trois entiers de 0 à 255, et renvoie la matrice représentant le
    négatif de l'image"""
    h, L = len(image), len(image[0])
    for i in range(h):
        for j in range(L):
            for k in range(3):
                image[i][j][k] = 255 - image[i][j][k]


image_travail = plt.imread("ecureuil_leger.jpg").tolist()
copie_travail = deepcopy(image_travail)
plt.imshow(copie_travail)
plt.show()

inverse_nb(copie_travail)
plt.imshow(copie_travail)
plt.show()


# %% =========== code pour changer le codage de flottants à entiers =============

# L'image lena.jpg étant codée par des flottants 32 bits entre 0 et 1,
# utiliser la ligne suivante pour changer son codage en nos entiers 8 bits

image3 = plt.imread("lena.png").tolist()
image_lena = [[[int(255 * image3[i][j][k]) for k in range(3)] 
               for j in range(len(image3[0]))]
               for i in range(len(image3))]
copie3 = deepcopy(image_lena)
plt.imshow(copie3)
plt.show()


