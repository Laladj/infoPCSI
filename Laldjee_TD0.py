#!/usr/bin/python3
-*- coding: utf-8 -*-


#Antoine Laldjee-Deroubaix, HX1
#Exercice 1
"""
1.
// division euclidienne
%  opérateur modulo
** opérateur puissance

2. 20//3 renvoie 6, tandis que 20.0//3 renvoie 6.0. De fait, 20,0 est de classe "flottant", tandis que
20 est un entier

3. les opérations entre parenthèses sont prioritaires sur 
la multiplication, elle-même prioritaire sur l'addition,

4. Dans l'ordre : **, * , + et %

5. l'exponentiation a une priorité plus élevée 
"""
###############################################
#Exercice 2: 
"""
On obtient : SyntaxError: invalid syntax
On place le guillement dans la parenthèse, et le script fonctionne. 

Version fausse : 
note = input"(Quelle note sur 20 avez vous obtenue")
if note >= 10: 
    print"(gg")
else:
    print"(Vous avez echoué")
"""
#Version correcte : 

note = input("Quelle note sur 20 avez vous obtenue")
if note >= 10: 
    print("reussi")
else:
    print("Vous avez echoué")

#######################################################################
#Exercice 3
 
def reussite(x:float):
    if x>=10.0:
        return True
    else:
        return False
 # reussite(9.5) renvoie bien False   

"""
iv
help(Reussite) renvoie : Help on function reussite in module __main__:
reussite(x: float)

on apprend que La fonction reussite attend
 un argument de type float et a été définie dans le script principal (module __main__).

"""
###########
#Exercice 4 
"""
avant l'import du module, cos(pi) renvoie une erreur : NameError: name 'cos' is not defined
Après l'import du module, on obtient : -1 (la valeur de cos(pi), en radians)

##########
#Exercice 5
"""

a,b,c=3 , 5, 7
print (a,b,c)
#le terminal renvoie 3 5 7, il fait donc l'affectation multiple des variables a,b,c
"""
a - b/c renvoie 2,28, soit a - (B/C)
(a-b)/c priorise (a-b), et renvoie -0.285

a +2 = 5, conservant la classe "int"
a conserve son affectation de base
En revanche, a +=2 incrémente de 2 la valeur de a
le terminal renvoie donc a = 5

a = a+ 2 équivaut a a+= 2 
on obtient donc 7, car l'on a déjà incremeneté de 2
a -= 2 incrémente de -2, donc a renvoie 5

"""
hauteur = 20 
largeur = 2*3
a = largeur*hauteur, 2*(largeur+hauteur)
type(a)

#On oberve que la solution renvoyée par le terminal est un tuple. (2-uplet)


###########################################################
#Exercice 6

a = 3 
type(a)
#<class 'int'> : a est un entier

a = 3. 
type(a)
#<class 'float'> : a est un flottant 

a = 'hello'
type(a)
#<class 'str'>

a = 3 + 1j
type(a)
#<class 'complex'> : j  désigne l'unité imaginaire 

type(j)
#NameError: name 'j' is not defined

type(1j)
#<class 'complex'>

1j**2
#(-1+0j), cohérent, car i^2=-1

a.imag
#1.0 , renvoie la partei imaginaire de a, a valant 3 + 1j comme défini plus tôt
type(a.imag)
#<class 'float'> : en effet, a.imag renvoyait 1.0
type('a')
#<class 'str'>, on a mis des guillemets autour de a, on a fait une conversion de type 
'cha'+"peau"
#'chapeau' concaténation
'a'+'1'
#'a1', de même
"cha"*3
#'chachacha', idem
abs(a)
#3.1622776601683795, rend la valeur absolue de l'argument, ici 3+1j, correspond à sqrt(3^2+1), logique
type(abs(a))
#<class 'float'>

(-1+0j)
#(-1+0j)

b = (-1 + 0j == 1)
b
#False, booléen à cause de ==
type(b)
#booléen

a.real
#3.0, conne la partie réelle d'un nombre complexe, sous la forme d'un flottant.
