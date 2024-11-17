#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
# Created By  : Antoine Laldjee--Deroubaix, HX1 
# Created Date: 22/10/2024
# version ='1.0'
# ---------------------------------------------------------------------------
""" DM2 """  
# ---------------------------------------------------------------------------
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
    """Renvoie le pgcd des deux entiers (méthode d'Euclide)"""
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    while b:
        a, b = b, a % b
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
def suite_liste(L1:list,L2:list,n:int)->list:
    """ Prend en argument deux listes de reels, et Renvoie 
la liste constituée des n premiers termes de la suite récurrente
linéaire d'ordre P= len(L1)
C'est à dire les termes du 0ème au n-1ème
    
    La première liste comporte les coefficients (a1, a2....an)
    la seconde liste comporte la liste de reels (u0...un-1)

    Exemple : L1 contient les coefficients : A0 A1 et A2 tels que Un+3 = A0*un + A1*un+1 + A2*un+2
            L2 contient u0 = 3, u1= 2, u2 = 5 (premiers termes de la suite recurrente linéaire d'ordre p=3)
    
             """
    troncation_a_la_plus_courte(L1,L2)
    un = 0
    p = len(L2) #on stocke l'ordre de la suite 
    
    if n <= len(L2):
        return L2[0:n]
    else:
        for i in range(len(L2),n):
            un = sum([L1[x]*L2[-p+x] for x in range(p)])
            #print(f"Iteration {i}, listeActuelle: {L2}, prochain Terme: {un}") #breakpoint
    
            #on calcule la suite a partir des p derniers termes de la liste. 
            L2.append(un)
            # print(L2)
        return L2
            


#on essaie la suite de fibonacci
fib1 = [1,1]
fib2 = [0,1]    
suite_liste(fib1,fib2,10)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#ii
suite_liste(coefs,donnees,40)
#le résultat est très grand

#on essaie la suite de fibonacci
fib1 = [1,1]
fib2 = [0,1]    
suite_liste(fib1,fib2,10)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#iii
"""En construisant la suite à partir de deux listes de longueur 1 : on obtient
une suite récurrente linéaire d'ordre 1, c'est à dire une suite géométrique
Application : suite géométrique de premier terme 1, et de raison 2"""
L1, L2 = [2], [1]
suite_liste(L1,L2,10)
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

#iv
def suite_terme(L1,L2,n)->float:
     """renvoie le terme un-1 de la suite linéaire
     recurrente donnée par L1 et L2.
     Cf suite_liste()"""
     
     (L1,L2)=troncation_a_la_plus_courte(L1,L2)
     un = 0
     p = len(L2) #ordre de la liste, nombre de termes à "conserver"
     #on cherche a disposer d'une liste de seulement p termes,
     # afin de pouvoir employer notre hypothèse de recurrence. 
     if n<= len(L2):
        return L2[n-1]
     else:
        for i in range(len(L2),n):
            un = sum([L1[x]*L2[-p+x] for x in range(p)])
            L2.append(un)
            L2.pop(0)
        return L2[-1]


#v
suite_terme(coefs,donnees,110) 
suite_terme(coefficients,donnees_initiales,40)
L1, L2 = [2], [1]
suite_terme(L1,L2,10) #fonctionne

# Question 4 : équirépartition modulaire. 
def suite_restes(L1:list,L2:list,N:int=1000,m:int=7)->tuple:
     """Prend 4 arguments: 
        L1 : Liste ,les coefficients de la suite récurrente linéaire
        L2 :, Liste les  premiers termes de la suite
        N  : Entier naturel, dernier terme de la suite Rk étudié
        m  : Entier naturel supérieur ou égal à 2
        
        considérons une suite récurrente linéaire finie de N termes
        (allant de 0 à N-1)
        Renvoie un tuple décrivant la proportion des termes de la suite 
        dont le reste de la division euclidienne vaut le terme de la suite 
        """
     L_modulo = [suite_terme(L1,L2,x)%m for x in range(0,N)] 
     L_count = [L_modulo.count(x)/len(L_modulo) for x in range(0,m)]

     return tuple(L_count)

suite_restes(coefficients,donnees)
#(0.135, 0.135, 0.128, 0.159, 0.139, 0.163, 0.141)
# on obtient bien un 7-uplet dont la somme vaut 1. 

#2 
#i
def dist(L1:list,L2:list,N:int=1000,m:int=7)->float:
     """Prend en argument deux listes et deux entiers, 
     et determine la distance statistique"""
     

     return max([abs (x - (1/m) ) for x in suite_restes(L1,L2,N,m)])

dist(coefficients,donnees)
# on obtient 0.02014
# cela correspond bien à la distance entre le plus grand nombre
# de suite_restes(coefficients,donnees) - 1/7
#ii
"""  pour N=2000, on obtient 0.0148
 pour N=3000, on obtient 0.0145
 on notera que dist() est de complexité O(n^2), les calculs
deviennent donc rapidement longs """

#######
# Après recherche, je me suis aidé d'internet
# On établit une suite de fibonacci modulo 1 

coefficients_suite = [1, 1]
termes_initiaux = [1, 0]
dist(L1, L2, 4, 2)
# on obtient bien 0, on notera que cela ne fonctionne qu'avec 2 et 4

#######a traiter : essayer de trouver le cas général pour tout M qui divise N 

#IV
def dist_moy(L1:list,N:int,m)->float:
     """prend en argument une liste L1, et construit les n-1 premiers
     termes d'une suite recurrente prenant pour coefficients L1, 
     et des premiers termes générés aléatoirement"""
     L2 = [rd.randrange(0,301) for _ in range(N)]
     return dist(L1,L2,N,m)

dist_moy(coefficients,1000,7)
#après plusieurs exécutions, on obtient des valeurs entre
# 0,02 et 0,06 
# d'après le TCL, un grand nombre d'execution succesives
#convergerait vers une distribution normale, comme la v.a reste inchangée

#3 faire la phase de tests

#======Question 5===== Problème de Skolem

#1 
#En théorie additive des nombres, le théorème de Skolem-Mahler-Lech déclare 
#que si une suite de nombres est engendrée par une relation de récurrence linéaire, 
#alors, avec des exceptions finies, 
#les positions auxquelles la suite est nulle forment un motif qui se répète. (wikipédia)

def zeros(L1:list,L2:list, N:int=1000)->list:
     """arguments:
        L1 :comporte les coefficients (a1, a2....an)
        L2 :comporte la liste de reels (u0...un-1)
        renvoie les indices des termes nuls de la suite reccurente linéaire
        construite à partir de L1 et L2. """
     troncation_a_la_plus_courte(L1,L2)
     suite = suite_liste(L1, L2, N)
     zerosListe = [x for x, nombre in enumerate(suite) if nombre == 0]
     return zerosListe


(coefs, donnees)= troncation_a_la_plus_courte(coefficients,donnees_initiales)
print(zeros(coefficients,donnees))
          

# 2 
# La suite reccurente linéaire : un+2 = un. Cette dernière alterne entre 0 et 1
UN1= [1,0]
UN2 = [0,1]
print(zeros(UN1,UN2,1000))
#renvoie bien toutes les positions paires
#3 
# la suite de fibonacci ne contient qu'un seul terme nul par stricte monotonie de cette dernière
fibonacci1 = [1,1]
fibonacci2 = [0,1]
print(zeros(fibonacci1,fibonacci2))
#ne revoie que l'indice 0. 