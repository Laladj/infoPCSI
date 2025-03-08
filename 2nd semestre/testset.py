liste2 = [('tente', 14, 128),('sac_de_couchage',2, 32), ('réchaud', 5, 20),
          ('livre', 1, 5), ('ordinateur', 6,18), ('mini_frigo',8, 80)]

def masse(objet:tuple)->float:
    """args : tuple : (nom, masse, valeur)
      returns : float : masse"""
    return objet[1]

liste1 = sorted(liste2,key = lambda x: x[1], reverse=True )
print(liste1)


liste = [[False]*8]
print(liste)
liste2 = [False]*8
print(liste2)