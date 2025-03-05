import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image 
import os


def charger_image_en_niveaux_gris(lien_image : str ) -> np.ndarray[int]:
    """
    
    fonction permettant de charger une image en niveaux de gris (grayscale)

    @Argument : 
        lien_image chaine de caractère indiquant le lien de l'image

    @Return : Tableau de pixel niveau gris de l'image
    
    """

    try:
        image = Image.open(lien_image)
        image.load() #vérifie si l'image chargée est bien une image --> la fonction verify renvoie un type None qui bloque la suite
        print("Image chargée avec succès")
        image = image.convert("L") #conversion en niveaux gris
        return np.array(image)
    except FileNotFoundError:
        #Exception si le fichier n'existe pas
        raise FileNotFoundError(f"L'image '{lien_image}' n'a pas été trouvé")
    except (IOError, SyntaxError):
        #Exception si le fichier n'est pas image valide
        raise ValueError(f"le fichier '{lien_image}' n'es pas une image valide")
    

def inverser_couleurs_de_l_image(image_array : np.ndarray[int] ) -> np.ndarray[int]:
    """
        Fonction permettant l' Inversion des couleurs : Transformez une image en noir et blanc en inversant ses pixels 
        (par exemple, 255−valeur_du_pixel255−valeur_du_pixel).

        @Argument : 
            image_array tableau de pixels de l'image

        @Return : Tableau de pixels inversés de l'image
    
    """
    return 255 - image_array
    

def luminosite_image(image_array : np.ndarray[int], gamma : int) -> np.ndarray[int]:
    """
    Fonction permettant de jouer avec la Luminosité : Augmentez ou diminuez la luminosité en ajoutant une constante à chaque pixel.
       
        @Argument : 
            image_array : tableau de pixels de l'image
            gamma : constante de luminosité

        @Return : Tableau de pixels de l'image après ajout de la constante de luminosité
    """

    return np.clip(gamma + image_array,0,255) #clip pour ne passortir des valeurs de 0 à 255

def rognage_image(image_array : np.ndarray[int], x_deb : int, x_fin : int, y_deb : int, y_fin : int) -> np.ndarray[int]:
    """
    Rognage : Découpez une partie de l'image en extrayant un sous-tableau de la matrice.
       
        @Argument : 
            image_array : tableau de pixels de l'image
            x_deb : num de la ligne de debut
            x_fin : num de la ligne fin
            y_deb : num de la colone debut
            y_fin : num de la colone fin 

        @Return : Tableau de pixels de l'image après ajout de la constante de luminosité

    """

    return image_array[x_deb:x_fin][y_deb:y_fin]


def flou_gaussien(image_array : np.ndarray[int]) -> np.ndarray[int]:
    """
    Flou gaussien : Appliquer le flou gaussien sur une image

    Le flou gaussien (Gaussian blur en anglais) est une technique de traitement d’image qui a
        pplique un flou à une image en utilisant une fonction gaussienne. Cela permet de lisser l’image et de réduire les détails et le bruit.
    Principe du Flou Gaussien
        Le flou est obtenu en appliquant un filtre gaussien, c'est-à-dire en remplaçant chaque pixel par une moyenne pondérée des pixels environnants, 
        avec un poids qui suit une distribution gaussienne (en cloche).

        @Argument : 
            imge_array : tableau de pixels de l'image

        @return : Tableau de pisels de l'image après application du flou gaussien
    
    """
    

    



def afficher_images(image_arrays : np.ndarray[int], titres : str) -> None: 



    """Affiche une liste d'images avec leurs titres."""
    plt.figure(figsize=(12, 6))
    for i, img in enumerate(image_arrays):
        plt.subplot(1, len(image_arrays), i + 1)
        plt.imshow(img, cmap="gray")
        plt.title(titres[i])
        plt.axis("off")
    plt.show()


def enregistrer_image(image, path):
    """
    Fonction permettant d'enregistrer une image modifiée.
    
    @Argument : 
    """
    Image.fromarray(image.astype("uint8")).save(path)
