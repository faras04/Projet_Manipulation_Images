import numpy as np
import pandas as pd
import math


#calcul de nombres parfaits
### 
# Un nombre parfait  est un entier positif égal à la somme de ses diviseurs propres (les diviseurs autres que le nombre lui même)
# Exemple : 6 est un nombre parfait, car ses diviseurs propres sont 1, 2 et 3 et 1+2+3=6
#  

# Ecrire une fonction est_nombre_parfait(n) qui prend un entier n en argument et renvoie True si n est un nombre parfait, et False sinon
#  
"""
def est_nombre_parfait(n):
    if n>0:
        diviseurs = []
        somme_diviseurs=0
        for i in range(1,n):
            if(n%i==0):
                diviseurs.append(i)
        for d in diviseurs:
            somme_diviseurs+=d
        if(somme_diviseurs==n):
            return True
        else: return False
    raise ValueError("Le nombre {} n'est pas un entier positif".format(n))

"""

def est_nombre_parfait(n):
    if n>0:
        somme_diviseurs = sum( i for i in range(1,n) if n%i==0)
        return somme_diviseurs==n
    raise ValueError("Le nombre {} n'est pas un entier positif".format(n))

# Ecrire une fonction trouver_nombre_parfait(limit) qui trouve tous les nombres parfaits inférieurs ou égaux à une limite donnée
#  

"""
def trouver_nombre_parfait(limit):
    liste_nombres_parfaits=[]
    for i in range(1,limit+1):
        if est_nombre_parfait(i):
            liste_nombres_parfaits.append(i)
    return liste_nombres_parfaits
"""

def trouver_nombre_parfait(limit):
    return [i for i in range(1,limit+1) if est_nombre_parfait(i)]


#Multiplication de matrices

##Ecrire une fonction multiplier_matrices(mat1,mat2) qui prend deux matrices sous forme de liste 2D et renvoie leur produit

def multiplier_matrices(mat1,mat2):

    nb_lignes_mat1 = len(mat1)
    nb_colonnes_mat2 = len(mat2[0])
    if nb_lignes_mat1==nb_colonnes_mat2:
        produit=np.zeros((nb_lignes_mat1,nb_colonnes_mat2))

        #parcours des lignes
        for i in range(0,len(mat1)):
            #parcours des colones
            for j in range(0,len(mat2[i])):
                for k in range(len(mat2)):
                    produit[i][j]+=mat1[i][k]*mat2[k][j]
        return produit
    raise ValueError("Les matrices {} et {} ne sont pas à la bonne taille pour faire leur produit".format(mat1,mat2)) 




