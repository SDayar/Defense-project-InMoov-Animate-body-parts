##@author Saifidine Dayar
##@brief Initialise un jeu qui est disponible. 
##@date 15/04/2025
##@version 08/05/2025
##@file GameFactory.py

##@package L2L1
##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter.messagebox import showerror
##@see GamePPC, CountBinary, SignLanguage sont les jeux disponibles dans l'application.
from Game import GamePPC, CountBinary, SignLanguage
class GameFactory():
    ##@class GameFactory
    ##@brief Initialise un jeu qui est disponible.
    ##@details Cette classe permet d'initialiser un jeu qui est disponible dans l'application. Elle permet de créer une instance du jeu qui est sélectionné par l'utilisateur. Elle permet également de vérifier si le jeu est disponible ou non.
    ##@package GameFactory
    def __init__(self, game):
        """! Constructeur de la classe GameFactory.
        @param String. Le nom du jeu à initialiser (par exemple, "PPC", "CountBinary", "SignLanguage").
        @return None"""
        ##@var __game
        ##@brief Contient le nom du jeu à initialiser.
        self.__game = game
    def get_game(self):
        """! Renvoie une instance du jeu choisie par l'utilisateur.
        @param None
        @return Object. L'instance du jeu choisie par l'utilisateur s'il existe, sinon None."""
        if self.__game == "countBinary":
            return CountBinary.CountBinary()
        elif self.__game == "PPC":
            return  GamePPC.GamePPC()
        elif self.__game == "SignLanguage":
            return  SignLanguage.SignLanguage()
        else :
            showerror("Le jeu "+str(self.__game)+" n'existe pas.\nLes jex disponibles sont les suivants :\n- Pierre papier ciseau. \n- Compter en binaire. \n-Language de signes.")
            return None
    
    def get_name_of_the_game(self):
        """! Retourne le nom du jeu.
        @param None 
        @return String. Le nom du jeu."""
        return self.__game
    