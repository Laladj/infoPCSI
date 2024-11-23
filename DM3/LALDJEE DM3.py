#!/usr/bin/env python3.8.2  
# -*- coding: utf-8 -*- 
# ----------------------------------------------------------------------------
"""
Created By  : Antoine Laldjee--Deroubaix, HX1 
Created Date: 11/18/2024
version ='1.0'
"""
# ---------------------------------------------------------------------------
""" DM 3 : Manipulation de fichiers en Python. """  
# ---------------------------------------------------------------------------

#Exercice 1
def transcription(ch:str)->str:
    """str->str
    renvoie la transcription d'une chaine de caractères passée en argument
    à l'aide du codage de Cesar"""
    string = ""
    for element in ch:
        if element == " " or element == "-":
            string += "0"
        else:
            string += str(ord(element)-96)
        string +=" " #ord(a)= 97 cf table ASCII
#https://fr.wikipedia.org/wiki/Fichier:ASCII-Table-wide.svg
    return string.strip()
    #return string[:-1] if string[-1]== " " else string


transcription("blaise de vigenere")
#'2 12 1 9 19 5 0 4 5 0 22 9 7 5 14 5 18 5'
#2
with open('identité.txt', 'w') as fichier:
    fichier.write(f"Nom : {transcription('laldjee deroubaix')}\n\nPrenom : {transcription('antoine')}")


#exercice 2
def decode(ch:str)->str:
    output =""
    ch = elements = ch.strip().split()
    for element in ch:
        if element == " ":
            pass
        elif element == 0:
            output += " "
        else:
            output += str(chr(int(element)+96))
    return output

decode("1 14 20 15 9 14 5 ")
#antoine
#iii
with open("identité.txt", 'r') as identite:
    lignes = identite.readlines()  # Liste contenant toutes les lignes
    ch1 = lignes[0].strip().replace("Nom : ", "") if len(lignes) > 0 else ""  # Supprime "Nom : "
    ch2 = lignes[2].strip().replace("Prenom : ", "") if len(lignes) == 3 else ""  # Supprime "Prenom : "

print(f"Nom: {decode(ch1)}")
print(f"Prenom: {decode(ch2)}")


#-------Fin du devoir------------