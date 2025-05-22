##@authors 
# - Shérine Meziane
# - Saifidine Dayar
##@file Finger.py
##@brief Ce fichier contient la définition de la classe Finger, qui permet de gérer les mouvements des doigts.
##@details Classe qui permet de gérer les mouvements d'un doigt.
##@date 26/03/2025
##@version 16/05/2025
##@package L2L1

## @see tkinter.messagebox est utilisé pour afficher des messages d'erreurs.

from tkinter.messagebox import showwarning


class Finger:
    ## @class Finger
    ## @brief Classe représentant un doigt et ses mouvements individuels.
    ## @details Cette classe permet de gérer les mouvements d'un doigt.
    ## @package Finger

    def __init__(self, nameFinger):
        """! Constructeur de la classe Finger.
        @param nameFinger (str) Le nom du doigt (par exemple, "Index", "Thumb").
        @details Le constructeur initialise un doigt avec un nom et définit sa position à -1 (inconnue).
        @return None.
        """
        ## @var __nameFinger 
        ## @brief Nom du doigt (par exemple, "Index", "Thumb"). 
        self.__nameFinger = nameFinger 

        ## @var __current_position 
        ## @brief Position actuelle du doigt. I 
        self.__current_position = -1    

    def personalized_position(self, degree):
        """! Déplace le doigt à un angle donné.
        @param degree (float) L'angle en degrés auquel le doigt doit se positionner.
        @return float Le nouvel angle si le mouvement a été effectué, sinon -1 si le doigt est déjà à cette position.
        @details Si le doigt est déjà à la position demandée, la méthode retourne -1 pour indiquer qu'aucun mouvement n'a eu lieu.
        Si l'angle est en dehors des limites autorisées, -1 est retourné.
        """
        if not(self.exceed_degree_limitations(degree)):
            if self.equals_current_position(degree):
                return -1
            return degree
        else:
            return -1

    def local_error(self, e):
        """! Affiche une alerte d'erreur liée à un doigt.
        @param e (str) Le message d'erreur à afficher dans l'alerte.
        @return None.
        @details Cette méthode affiche une boîte de dialogue d'alerte avec un message d'erreur spécifique à un doigt.
        """
        showwarning("Erreur sur le niveau des doigts", e)

    def exceed_degree_limitations(self, degree):
        """! Vérifie si l'angle donné dépasse les limites autorisées (0° <= angle <= 90°).
        @param degree (float) L'angle à vérifier.
        @return bool True si l'angle dépasse les limites (hors plage), sinon False.
        """
        if(degree >= 0 and degree <= 90):
            return False
        return True

    def equals_current_position(self, new_position):
        """! Vérifie si la position actuelle du doigt est égale à une nouvelle position donnée.
        @param new_position (float) La nouvelle position à comparer avec la position actuelle.
        @return bool True si la position actuelle est égale à la nouvelle position, sinon False.
        @details Cette méthode compare la position actuelle du doigt avec une nouvelle position spécifiée
        """
        if(self.__current_position == new_position):
            self.__current_position = new_position
            return True
        return False

    def __str__(self):
        """! Retourne le nom du doigt.
        @return str Le nom du doigt sous forme de chaîne de caractères.
        """
        return self.__nameFinger

    def get_current_position(self):
        """! Renvoie la position actuelle du doigt.
        @return float La position actuelle du doigt (en degrés).
        @details La position actuelle représente l'angle du doigt.
        """
        return self.__current_position

    def set_current_position(self, new_position):
        """! Définit une nouvelle position pour le doigt.
        @param new_position (float) La nouvelle position à définir pour le doigt.
        @return None.
        @details Cette méthode permet de définir une nouvelle position pour le doigt si elle est différente de -1. Si la position est -1, cela signifie que le doigt n'a pas bougé.
        """
        if new_position != -1:
            self.__current_position = new_position
