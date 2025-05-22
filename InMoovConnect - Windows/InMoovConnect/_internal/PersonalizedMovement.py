##@author Saifidine Dayar
##@brief PersonalizedMovement permet d'exécuter un mouvement personnalisé.
##@date 26/04/2025
##@version 08/05/2025
##@file PersonalizedMovement.py
##@package L2L1


##@see Movement est utilisé pour créer les mouvements personnalisés.
from Movement import Movement
##@see tkinter est utilisé pour afficher les messages d'erreurs.
from tkinter import messagebox
class PersonalizedMovement : 
    ##@class PersonalizedMovement
    ##@brief Lancer un mouvement personnalisé.
    ##@details Cette classe permet de lancer un mouvement personnalisé. Elle permet de créer un mouvement personnalisé à partir d'une liste de positions. Elle permet également d'afficher un message d'erreur si la saisie est incorrecte.
    ##@see Movement
    ##@package PersonalizedMovement
    def __init__(self):
        """! Constructeur de la classe PersonalizedMovement.
        @param None
        @return None"""
        pass 
    @staticmethod
    def send_personalized_positions(positions):
        """! Renvoie les mouvements personnalisés pour créer les mouvements valide. 
        @param list. Liste des positions à envoyer.
        @details Cette méthode est statique.
        @return None"""
        list_positions = []
        err = False #Indique qu'il y a eu une erreur de saisi
        for pos in positions :
            try:
                list_positions.append(float(pos))
            except:
                err = True
                list_positions.append(-1)
        if err :
            PersonalizedMovement().local_warning("Attention le système a détecté une/des information(s) erronée(s) dans la saisie. Elle(s) sera(seront) interprétée(s) comme la donnée suivante => -1.")
        Movement.create_movement(list_positions)
    def local_warning(self,e):
        """! Affiche une erreur liée à un mouvement personnalisé.
        @param String. Le message d'erreur à afficher dans l'alerte.
        @return None.
        @details Cette méthode affiche une boîte de dialogue d'alerte avec un message d'erreur spécifique à un mouvement personnalisé."""
        messagebox.showwarning("Erreur ", e)