#Exercice 1
def teste_type(arg):
    if type(arg)== int:
        return "entier"
    elif type(arg)== float:
        return "flottant"
    elif type(arg)== str : 
        return "chaine"
    else:
        return "inconnu"  

print(teste_type(3))
print(teste_type(3.2))
print(teste_type("banane"))
print(teste_type(False))

#Exercice 2
#i
def moy1(liste : list):
    count = 0
    for element in liste:
        count += element
    return count/len(liste)
#ii
L = [8.15, 16, 11.5]
#on trouve bien 11.883, on vérifie le résultat obtenu en calculant print(sum(L)/len(L))
moy1(L)
#iii
def barycentre(L:list, A:list):
    count = 0
    for valeur in L:
        for coefficient in A:
            count += (valeur*coefficient)
    return count/sum(A)
#iv
L = [8.5,16,11.5]
A = [5,0.75,11]
print(barycentre(L,A)) #on trouve bien 36.0

##Exercice 3
#a)
def presence(a:str, ch:str): #a reprendre
    if a in chr:
        return True
    else:
        False
print(presence("a","alice"))

#b)
def trouve_indice(L:list,d:int):
    div = 
    if d == 0:
        raise ValueError("L'argument ne doit pas être nul.")
    else : 