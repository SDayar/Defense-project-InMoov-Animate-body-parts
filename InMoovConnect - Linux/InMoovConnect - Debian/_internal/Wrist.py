##@authors
# - Jacques
# - Saifidine Dayar
##@file Wrist.py
##@brief Cette classe permet de gérer les mouvements du poignet. Elle permet de bouger le poignet à un angle donné. Elle permet également de vérifier si le poignet est déjà dans cette position ou non. 
##@date 03/03/2025
##@version 08/05/2025
##@package L2L1

##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter.messagebox import showwarning
class Wrist:
    ##@class Wrist
    ##@brief Cette classe permet de gérer les mouvements du poignet. Elle permet de bouger le poignet à un angle donné. Elle permet également de vérifier si le poignet est déjà dans cette position ou non.
    ##@package Wrist
    def __init__(self,name):
        """! Constructeur de la classe Wrist.
        @param String. Le nom du poignet (par exemple, "Gauche", "Droit").
        @details Le constructeur initialise un poignet avec un nom et définit sa position à -1 (inconnue).
        @return None"""
        self.__name =name
        self.__current_position=-1
    def local_error(self,e):
        """! Soulève un erreur qui concerne le fonctionnement d'un doigt.
        @param String. Le message d'erreur à afficher.
        @return None.""" 
        showwarning("Erreur sur le niveau du poignet",e)

    def personalized_position(self,degree):
        """! 
        @param Float. L'angle en degrés auquel le doigt doit se positionner.
        @return Float. Le nouvel angle si le mouvement a été effectué, sinon -1 si le doigt est déjà à cette position.
        Bouge un doigt à un angle donné. Si le doigt est déjà dans cette position, on ne bouge pas le doigt en renvoyant -1."""
        if(not(self.__exceed_degree_limitations(degree))):
            if(self.__equals_current_position(degree)):
                return -1
            return degree
        else:
            return -1
    def __exceed_degree_limitations(self,degree):
        """! Renvoie true si le degré est valide ou non.
        @param Float. L'angle à vérifier.
        @return boolean. True si l'angle dépasse les limites (hors plage), sinon False.""" 
        if(degree >= 0 and degree <= 180):
            return False
        return True 
    def __equals_current_position(self,new_position):
        """! Vérifie si la position actuelle est semblable à la nouvelle position.
        @param Float. La nouvelle position à vérifier.
        @return boolean. True si la position actuelle est semblable à la nouvelle position, sinon False."""
        if(self.__current_position == new_position):
            return True
        return False
    def get_current_position(self):
        """! Renvoie la position actuelle du doigt. 
        @param None
        @return Float. La position actuelle du doigt."""
        return self.__current_position
    def set_current_position(self,new_position):
        """! Définit la position actuelle du doigt. 
        @param Float. La nouvelle position à définir.
        @return None."""
        if new_position != -1:
            self.__current_position = new_position
    def __str__(self):
        """! Renvoie le nom du poignet.
        @param None
        @return str. Le nom du poignet."""
        return self.__name