## @file Games.py
##  @brief Frame "jeux" de l'interface graphique proposant plusieurs jeux pour la main : 
##         Compter en binaire, Pierre-Feuille-Ciseau, attraper un objet, mouvements personnalisés.
##  @author Shérine
##  @date 22/02/2025

 
##  @package L2L1
##  @see tkinter est utilisé pour créer l'interface graphique.
import customtkinter as ctk
##  @see PIL est utilisé pour charger et redimensionner les images.
import PIL.Image as openImg
##  @see Enumerations.EnumMovement est utilisé pour définir les mouvements de la main robotique.
from Enumerations.EnumMovement import EnumMovement as EM
##  @see Movement est utilisé pour créer les mouvements de la main robotique.
from Movement import Movement
##  @see GameFactory est utilisé pour créer une instance du jeu sélectionné par l'utilisateur.
import GameFactory



class Games():
    ##@class Games
    ##@brief Gère l'affichage d'une frame de jeux avec plusieurs boutons menant à des fonctionnalités de la main.
    ##@details Cette classe construit une frame avec des boutons d'accès à différentes fonctionnalités de mouvement ou jeux.
    ##@package Games
    def __init__(self, window):
        """! Constructeur de la classe Games.
        @brief Initialise les variables et images nécessaires à l'affichage.
        @param CTk. La fenêtre customtkinter dans laquelle les éléments seront affichés.
        @return None"""
        ##@var __window. 
        ##@bref Fenêtre principale du logiciel.
        self.__window = window
        ##@var __fileMenu. chemin vers l'image du bouton menu.
        self.__fileMenu = "images/menu.png"
        ##@var __fileStop. chemin vers l'image du bouton STOP.
        self.__fileStop = "images/STOP.png"
        ##@var __fileBack. chemin vers l'image du bouton de retour en arrière.
        self.__fileBack = "images/back.png"
        ##@var __fileCatc. chemin vers l'image du bouton Catch.
        self.__fileCatch = "images/catch.png"
        ##@var __fileMicro. chemin vers l'image du bouton PersonalizedMovement.
        self.__fileMicro = "images/micro.png"
        ##@var __filePfc. chemin vers le bouton de jeu pierre papier ciseau.
        self.__filePfc = "images/pfc.png"
        ##@var __fileCount. 
        ##@bref Chemin vers l'image du jeu compter en binaire
        self.__fileCount = "images/count.png"
        ##@var __color.
        ##@bref couleur de la frame.
        self.__color = "#b9e4f0"
        ##@var __hover_color.
        ##@bref Couleur de survol.
        self.__hover_color = "#FFF0F5"
        ##@var __police.
        ##@bref Police d'écriture.
        self.__police = "<codec Pro>"  # police d'écriture
        ##@var __Ptaile
        ##@bref Taille de la police.
        self.__Ptaille = 20  # taille du texte
        ##@var _back
        ##@bref Fonction implémentant la fonctionnalité retour en arrière.
        ##@see Mediator
        self._back = None
        ##@var _switchFrame
        ##@bref Fonction implémentant la fonctionnalité changer de frame.
        ##@see Mediator
        self._switchFrame = None
        ##@var __game_count
        ##@bref Instance de la GameFactory qui implémente le jeu compter en binaire.
        ##@see GameFactory
        self.__game_count = GameFactory.GameFactory("countBinary").get_game()

    
    def __createFrameGames(self):
        """! 
        @brief Crée et configure la frame principale contenant les boutons interactifs. 
        @details Chaque bouton représente une fonctionnalité de la main robotisée : menu, arrêt, retour, attraper, mouvements personnalisés, Pierre-Feuille-Ciseau, et compter en binaire.
        @param None
        @return La frame CTk contenant les boutons de commande."""
        
       
        
        frameGames = ctk.CTkFrame(self.__window, width=self.__window.winfo_screenwidth(), height=self.__window.winfo_screenheight(),
                                  fg_color=self.__color)
        
        # Bouton Menu
        menu_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileMenu), dark_image=self.loadBgImage(self.__fileMenu), size=(130, 100))
        buttonMenu = ctk.CTkButton(master=frameGames, text="", width=140, height=120, image=menu_button, bg_color=self.__color,
                                   fg_color=self.__color, hover_color=self.__hover_color, corner_radius=20, command=lambda: self.execute(self._switchFrame(1)))
        buttonMenu.place(relx=0, rely=0.35)

        # Bouton Stop
        ##  @details Ce bouton est utilisé pour arrêter tous les mouvements de la main robotisée et ouvrir la main.
        stop_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileStop), dark_image=self.loadBgImage(self.__fileStop), size=(200, 130))
        buttonStop = ctk.CTkButton(master=frameGames, text="", width=10, height=15, image=stop_button, bg_color=self.__color,
                                   fg_color=self.__color, hover_color="#FFB3B3", corner_radius=80, command=lambda: Movement.create_movement(EM.STOP))
        buttonStop.place(relx=0.79, rely=0.78)

        # Bouton Retour
        ##  @details Ce bouton est utilisé pour revenir à la fenêtre précédente.
        back_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileBack), dark_image=self.loadBgImage(self.__fileBack), size=(130, 100))
        buttonBack = ctk.CTkButton(frameGames, text="", width=150, height=200, bg_color=self.__color, fg_color=self.__color,
                                   hover_color=self.__hover_color, image=back_button, corner_radius=40, command=lambda: self._back())
        buttonBack.place(relx=0, rely=0)

        # Bouton Attraper un objet
        ##  @details Ce bouton est utilisé pour activer la fonctionnalité d'attraper un objet.
        catch_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileCatch), dark_image=self.loadBgImage(self.__fileCatch), size=(150, 180))
        buttonCatch = ctk.CTkButton(frameGames, text="Catch", text_color="black", width=150, height=100, bg_color=self.__color,
                                    fg_color=self.__color, hover_color=self.__hover_color, image=catch_button, corner_radius=40,
                                    compound="top", font=(self.__police, self.__Ptaille, "bold"))
        buttonCatch.place(relx=0.22, rely=0.48)

        # Bouton Mouvements personnalisés
        ##  @details Ce bouton est utilisé pour accéder aux fonctionnalitées de commande vocale et de mouvements personnalisés.
        micro_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileMicro), dark_image=self.loadBgImage(self.__fileMicro), size=(180, 150))
        buttonMicro = ctk.CTkButton(frameGames, text="Personalized movements", text_color="black", width=50, height=50,
                                    fg_color=self.__color, hover_color=self.__hover_color, bg_color=self.__color, image=micro_button,
                                    corner_radius=40, compound="top", font=(self.__police, self.__Ptaille, "bold"),
                                    command=lambda: self.execute(self._switchFrame(4)))
        buttonMicro.place(relx=0.52, rely=0.52)

        # Bouton Pierre-Feuille-Ciseau
        ##  @details Ce bouton est utilisé pour accéder au jeu Pierre-Feuille-Ciseau.
        pfc_button = ctk.CTkImage(light_image=self.loadBgImage(self.__filePfc), dark_image=self.loadBgImage(self.__filePfc), size=(200, 200))
        buttonpfc = ctk.CTkButton(frameGames, text="Rock Paper Scissors", text_color="black", width=150, height=100,
                                  fg_color=self.__color, hover_color=self.__hover_color, bg_color=self.__color, image=pfc_button,
                                  corner_radius=40, compound="top", font=(self.__police, self.__Ptaille, "bold"),
                                  command=lambda: self.execute(self._switchFrame(3)))
        buttonpfc.place(relx=0.49, rely=0.07)

        # Bouton Compter en binaire
        ##  @details Ce bouton est utilisé pour compter en binaire, il permet d'accéder à une boite de dialogue qui permettra d'entrer un nombre.
        count_button = ctk.CTkImage(light_image=self.loadBgImage(self.__fileCount), dark_image=self.loadBgImage(self.__fileCount), size=(130, 180))
        buttonCount = ctk.CTkButton(frameGames, text="Count in binary", text_color="black", width=150, height=100, fg_color=self.__color,
                                    hover_color=self.__hover_color, bg_color=self.__color, image=count_button, corner_radius=20,
                                    compound="top", font=(self.__police, self.__Ptaille, "bold"), command=lambda: self.create_input_dialog())
        buttonCount.place(relx=0.25, rely=0.1)

        return frameGames

    
    def loadBgImage(self, imagefile):
        """! 
        @brief Charge une image et l’adapte à la taille de la fenêtre.
        @param String. Le chemin du fichier image à charger.
        @return PIL.Image. Une image redimensionnée pour s’adapter à l’écran.
        @see PIL.Image"""
        img = openImg.open(imagefile)
        resized_img = img.resize(size=(self.__window.winfo_screenwidth(), self.__window.winfo_screenheight()), resample=5)
        return resized_img

    
    def getFrameGames(self):
        """!
        @brief Crée et retourne la frame contenant les boutons des jeux.
        @param None
        @return CTkFrame. La frame créée via __createFrameGames()."""
        return self.__createFrameGames()

    
    def execute(self, function):
        """!
        @brief Fonction d’appel indirecte pour exécuter une fonction donnée.
        @param function. Fonction à exécuter.
        @return None."""
        lambda: function()

    
    def create_input_dialog(self):
        """! 
        @brief Crée une boîte de dialogue pour entrer un nombre (0–31) et lance le jeu de comptage en binaire.
        @param None
        @return None"""
        window_dialog = ctk.CTkInputDialog(
            fg_color=self.__color,
            text_color="black",
            button_fg_color="white",
            button_hover_color=self.__hover_color,
            button_text_color="black",
            entry_border_color=None,
            entry_text_color="black",
            entry_fg_color="white",
            title="InMoovConnect",
            font=None,
            text="Enter a number between 0 and 31."
        )
        window_dialog.geometry("400x400")
        self.__game_count.count_to(window_dialog.get_input())
