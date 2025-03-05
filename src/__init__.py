import module_math as mm
import module_operations_images as moi

#programme principal

if __name__ == "__main__":

    liste_n=[6,2,26,28]
    """
        try:
            for n in liste_n:
                if est_nombre_parfait(n):
                    print("Le nombre {} est un nombre parfait".format(n))
                else: print("Le nombre {} n'est pas un nombre parfait".format(n))

            liste_limites = [2,8,28]

            for l in liste_limites:
                print("La liste des nombres parfaits jusqu'à {} est {}".format(l, trouver_nombre_parfait(l)))
        except ValueError as e:
            print(e)

    """
    """
    liste_des_mat1_mat2 = [([[1,0],[0,1]], [[1,3,3],[2,4,3]]),([[1,0],[0,1]],[[1,3],[2,4]])]

    for mat1,mat2 in liste_des_mat1_mat2:
        
        try:
            print(mm.multiplier_matrices(mat1,mat2))

        except ValueError as e:
            print(e)

    """
    """
    ###########################################################################################################

    ### Manipulation d'images

    ###########################################################################################################
    """
    lien_image='C:/Users/faaras/OneDrive - Capgemini/Desktop/Python/ProjetPython1/data/images/landscape.jpg'
    try:
        array_image = moi.charger_image_en_niveaux_gris(lien_image)
        array_image_inversee = moi.inverser_couleurs_de_l_image(array_image)
        array_image_illuminee = moi.luminosite_image(array_image_inversee,20)
        array_image_rognee = moi.rognage_image(array_image_illuminee,50,100,50,100)
        print(array_image)
        moi.afficher_images([array_image, array_image_inversee, array_image_illuminee, array_image_rognee],["originale", "inversee", "illuminee", "rognee"])
    except Exception as e:
        print(e)
