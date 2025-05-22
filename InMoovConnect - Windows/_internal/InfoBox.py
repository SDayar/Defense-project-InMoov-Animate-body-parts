##@authors
# - Shérine 
# - Saifidine Dayar
##@file  InfoBox.py
##@brief Permet d'afficher une boite de dialogue qui contient ce que chaque doigt a effectué comme mouvement.
##@date  24/04/2025
##@version 08/05/2025
##@package L2L1

##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter import messagebox

class InfoBox:
    ##@class InfoBox
    ##@brief Permet d'afficher une boite de dialogue qui contient ce que chaque doigt a effectué comme mouvement.
    ##@details Après avoir effectué un mouvement, la boite de dialogue s'affiche pour afficher les informations sur le dernier mouvement effectué par chaque doigt.
    ##@package InfoBox
    ##@var info. 
    ##@brief Contient les informations sur le mouvement effectué par chaque doigt.
    info = None
    @classmethod
    def display(cls):
        """! Affiche le text_box où sera affiché les informations supplémentaire.
        @param None
        @details Il s'agit d'une méthode de classe.
        @return None
        """
        messagebox.showinfo("Informations sur les doigts", InfoBox.info) # affichage de la boite de dialogue avec le texte
    



