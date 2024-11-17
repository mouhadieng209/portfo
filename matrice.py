import numpy as np


# Créer une matrice 3x3
matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# # Afficher la matrice
# print("Matrice:")
# print( matrice)


# # Accéder à un élément (ligne 2, colonne 3)
# element = matrice[-1, -2]
# print("\nÉlément à la ligne 3, colonne 2:", element)


matrice[1,1] = 2




# # Afficher la matrice apres la mise a jour
# print("Matrice:")
# print(matrice)


# Ajouter une nouvelle ligne à la matrice
nouvelle_ligne = np.array([34, 6, 13])
matrice = np.vstack([matrice, nouvelle_ligne])
print("\nMatrice après ajout d'une nouvelle ligne:")
print(matrice)


# Ajouter une nouvelle colonne à la matrice
nouvelle_colonne = np.array([[13], [14], [15], [16]])
matrice = np.hstack([matrice, nouvelle_colonne])
print("\nMatrice après ajout d'une nouvelle colonne:")
print(matrice)


matrice[-1, -1] = 20
# Afficher la matrice apres la mise a jour
print("Matrice:")
print(matrice)
