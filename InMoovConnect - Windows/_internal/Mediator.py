## @author  Saifidine Dayar
## @date  03/03/2025
## @brief Contient la classe Mediator qui permet de gérer les fenêtres de l'application.
##       Cette classe permet de gérer les fenêtres de l'application. Elle permet de lancer une fenêtre, de la fermer, de gérer les erreurs lors de l'ouverture d'une fenêtre.
## @version 08/05/2025
## @file  Mediator.py
##@package L2L1

##tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
import tkinter.messagebox as TkError
##@see ENUM_STATUS_FRAME
from Enumerations.ENUM_STATUS_FRAME import ENUM_STATUS_FRAME as SF
##@see Games
from Games import Games
##@see Principale
from Principale import Principale
##@see PPC
from PPC import PPC
##@see CommandeVocale
from CommandeVocale import CommandeVocale
class Mediator():
    ##@class Mediator
    ##@brief Permet de gérer les différentes frames de l'application.
    ##@details Cette classe permet de gérer les différentes frames de l'application. Elle reçoit des demandes de changements de frames puis procède au changement de frame en faisant appel à la méthode renderFrame de la classe Main. Elle gère également les erreurs lors de l'ouverture d'une frame.
    ##@see Main
    ##@see Games
    ##@see Principale
    ##@see PPC
    ##@see CommandeVocale
    ##@see ENUM_STATUS_FRAME
    ##@package Mediator
      
    def __init__(self):
        """! Constructeur de la classe Mediator.
        @param None
        @return None
        """
        ##@var _defaultFrame
        ## @brief Contient la frame par défaut de l'application
        ## @see Main
        self.__defaultFrame = None 

        ##@var win
        ## @brief Contient la fenêtre de l'application
        ## @see Main
        self.win = None 

        ##@var _objectMenu
        ## @brief Contient un objet de la classe Principale.
        ## @see Principale
        self.__objectMenu = None 

        ##@var _objectPPC
        ##@brief Contient un objet de la classe PPC.
        ##@see PPC
        self.__objectPPC = None 

        ##@var _objectCV
        ##@brief Contient un objet de la classe CcommandeVocale.
        ##@see CommandeVocale
        self.__objectCV = None

        ##@var _objectGames
        ##@brief Contient un objet de la classe Games.
        ##@see Games
        self.__objectGames = None 

        ##@var __framesInfo
        ##@brief Contient un dictionnaire d'informations sur l'application et son état à l'instant t.
        self.__framesInfo= None 

        ##@var renderFrame
        ##@brief Contient la méthode renderFrame de la classe Main.
        self.renderFrame = None 

        ##@var _back
        ##@brief Contient la méthode qui permet à toutes les frames de revenir en arrière.
        self._back = None

        ##@var _switchFrame
        ##@brief Contient la méthode qui permet de changer de frame.
        self._switchFrame = None
    def _init_ObjectModules(self):
        """! Initialise les objets des autres modules et le registre de l'application. 
        @param None
        @return None
        """
        self.__objectGames = Games(self.win)
        self.__objectGames._back = self._back
        self.__objectGames._switchFrame = self._switchFrame
        
        self.__objectMenu = Principale(self.win)
        self.__objectMenu._switchFrame = self._switchFrame
        

        self.__objectPPC = PPC(self.win)
        self.__objectPPC._back = self._back
        self.__objectPPC._switchFrame = self._switchFrame

        self.__objectCV = CommandeVocale(self.win)
        self.__objectCV._back = self._back
        self.__objectCV._switchFrame = self._switchFrame  

        self.__framesInfo = {0:[self.__defaultFrame,SF.RUNNING], 1:[self.__objectMenu.get_frame_principale(),SF.NOT_RUNNING],2:[self.__objectGames.getFrameGames(),SF.NOT_RUNNING], 3:[self.__objectPPC.getFramePPC(),SF.NOT_RUNNING], 4:[self.__objectCV.getFrameCV(),SF.NOT_RUNNING]}#NUM_FRAME = [CTkFrame, STATUS]
    def errorLaunchingFrame(error):
        """! Avertit l'utilisateur s'il y a eu une erreur lors de l'exécution du service.
        @param String.  message d'erreur à afficher
        @return None"""
        TkError.showerror(title="Erreur lors de l'éxécution", message=error)
   
    def __alreadyRendered(self,N_FRAME):
        """! Retourne True si une frame est déjà lancée. False sinon.
        @param int. ID de la frame à charger
        @return boolean. True si la frame est déjà lancée. False sinon.
        """ 
      
        if([self.__framesInfo[N_FRAME]][0] == SF.RUNNING):#On vérifie le status de la frame
            #Si la frame est déjà affichée alors on ne l'affiche pas en retournant True
            return True
        #Sinon on l'affiche en retournant False
        return False
    def renderFrameOrNo(self, N_FRAME):
        """! Si la frame n'est pas déjà affichée, il dit à au Main de l'afficher. Sinon, un message d'erreur seul un message d'alerte est affichée.
        @param int. ID de la frame à charger
        @return None
        """
        if(not(self.__alreadyRendered(N_FRAME))):
            #Si la frame n'est pas affichée alors on l'affiche
            self.__framesInfo[N_FRAME][1] = SF.RUNNING # On change le statut de la frame en "RUNNING"
            self.renderFrame(self.__framesInfo[N_FRAME][0])#On transfère la framme en "RUNNING"
                
                
        else:
            #Sinon on affiche un message d'erreur pour dire que la fenêtre est déjà imprimée
            Mediator.errorLaunchingFrame("La frame est déjà affichée")

    
    