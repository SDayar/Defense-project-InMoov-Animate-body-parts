##@file PPC.py
##@brief Ce fichier contien la classe la classe PPC qui gère la frame du jeu Pierre-Papier-Ciseaux. Elle permettra a l'utilisateur de jouer au jeu pierre feuille ciseau. Elle propose différent bouton comme pierre, feuille ciseau et aléatoire, permettant par l'envoie de signeau, que la main exécute ses commandes..
##@author Jacques
##@date 17/04/2024
##@version  11/05/2025
##@package L2L1

##@see customtkinter
import customtkinter as ctk
##@see Enumerations.EnumMovement
from Enumerations.EnumMovement import EnumMovement as EM 
##@see Movement
from Movement import Movement
##@see PIL.Image
from PIL import Image as openImg
##@see GameFactory
import GameFactory

class PPC():
    def __init__(self, window):
        """! Constructeur de la classe PPC.
        @param CTk. La fenêtre principale de l'application.
        @details Cette méthode initialise les attributs de la classe, charge les images nécessaires, crée les boutons et configure l'interface utilisateur.
        @return None."""
        ##@var __window CTk. 
        # La fenêtre principale du logiciel
        self.__window = window
        ##@var __labelBgcolor 
        ##@bref La couleur de l'arrière plan
        self.labelBgcolor = "#CCCCFF"
        ##@var color 
        ##@brief La couleur de fond de l'interface.
        self.color = "#b9e4f0"
        ##@var police 
        ##@brief La police du texte
        self.police = "Bahnschrift SemiBold Condensed"
        ##@var Ptaille 
        ##@var La taille de la police
        self.Ptaille = 20  # Taille du texte
        ##@var __hover_color 
        # Couleur du bouton quand la souris passe dessus
        self.hover_color = "#FFF0F5"
        ##@var __stop 
        ##@brief Le chemin de l'image du bouton stop.
        self.fileStop = "images/STOP.png"
        ##@var __back 
        ##@brief Le chemin de l'image du bouton retour.
        self.fileBack = "images/back.png"
        ##@var __menu 
        ##@brief Le chemin de l'image du bouton menu.
        self.fileMenu = "images/menu.png"
        ##@var __fond 
        ##@brief Le chemin de l'image d'arrière-plan.
        self.fileBg = "images/background.png"
        ##@var __fileRock 
        ##@brief Le chemin de l'image de la Pierre.
        self.fileRock = "images/pierre.png"
        ##@var __filePaper 
        ##@brief Le chemin de l'image de la feuille
        self.filePaper = "images/papier.png"
        ##@var __fileScissors 
        ##@brief Le chemin de l'image du ciseau
        self.fileScissors = "images/ciseaux.png"
        ##@var __fileRandom 
        ##@brief Le chemin de l'image du bouton au hasard
        self.fileRandom = "images/random.png"
        ##@var _back 
        ##@brief La fonction de retour au thread précédent.
        self._back = None
        ##@var _switchFrame 
        ##@brief La fonction de changement de frame.
        self._switchFrame = None
        ##@var __game_pfc 
        ##@brief L'objet de la classe GameFactory responsable de la gestion du jeu Pierre-Papier-Ciseaux.
        self._game_pfc = GameFactory.GameFactory("PPC").get_game()
    def __createFramePPC(self):
        """! Configure la frame PPC avec tout les boutons présents.
        @param None
        @return CTK frame: la frame de l'interface PPC"""
        framePPC = ctk.CTkFrame(self.__window, width=self.__window.winfo_screenwidth(),
                                height=self.__window.winfo_screenheight()
                                , fg_color=self.color)
        # bouton stop
        stop_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileStop),
                                   dark_image=self.loadBgImage(self.fileStop), size=(250, 180))
        buttonStop = ctk.CTkButton(framePPC, text="", text_color="black", width=20, height=20, bg_color=self.color,
                                   fg_color=self.color, hover_color=self.hover_color, image=stop_button,
                                   corner_radius=40, command=lambda:Movement.create_movement(EM.STOP))
        buttonStop.place(relx=0.75, rely=0.7)

        # bouton retour
        back_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileBack),
                                   dark_image=self.loadBgImage(self.fileBack), size=(130, 100))
        buttonBack = ctk.CTkButton(framePPC, text="", text_color="black", width=150, height=200,
                                   bg_color=self.color,
                                   fg_color=self.color, hover_color=self.hover_color, image=back_button,
                                   corner_radius=40, command=lambda: self.execute(self._back()))
        buttonBack.place(relx=0, rely=0)

        # bouton menu
        menu_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileMenu), dark_image=self.loadBgImage(self.fileMenu), size=(130, 100))
        homeButton = ctk.CTkButton(framePPC, text="", text_color="black", width=140, height=120, bg_color=self.color,
                                   fg_color=self.color, hover_color=self.hover_color, image=menu_button,
                                   corner_radius=20, command=lambda:self.execute(self._switchFrame(1)))
        homeButton.place(relx=0, rely=0.35)

        # rock button
        rock_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileRock),
                                   dark_image=self.loadBgImage(self.fileRock), size=(160, 130))
        buttonRock = ctk.CTkButton(framePPC, text="ROCK", text_color="black", width=20, height=20,
                                   bg_color=self.color,
                                   fg_color=self.color, hover_color=self.hover_color, image=rock_button,
                                   corner_radius=80, compound="top",
                                   font=(self.police, self.Ptaille, "bold"), command=lambda:Movement.create_movement(EM.ROCK))
        buttonRock.place(relx=0.2, rely=0.35)

        # Paper button
        paper_button = ctk.CTkImage(light_image=self.loadBgImage(self.filePaper),
                                    dark_image=self.loadBgImage(self.filePaper), size=(160, 130))
        buttonPaper = ctk.CTkButton(framePPC, text="PAPER", text_color="black", width=20, height=20,
                                    bg_color=self.color,
                                    fg_color=self.color, hover_color=self.hover_color, image=paper_button,
                                    corner_radius=80, compound="top",
                                    font=(self.police, self.Ptaille, "bold"), command=lambda:Movement.create_movement(EM.PAPER))
        buttonPaper.place(relx=0.45, rely=0.35)

        # Scissor button
        scissor_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileScissors),
                                      dark_image=self.loadBgImage(self.fileScissors), size=(160, 130))
        buttonScissor = ctk.CTkButton(framePPC, text="SCISSORS", text_color="black", width=20, height=20,
                                      bg_color=self.color,
                                      fg_color=self.color, hover_color=self.hover_color, image=scissor_button,
                                      corner_radius=80, compound="top",
                                      font=(self.police, self.Ptaille, "bold"), command=lambda:Movement.create_movement(EM.SCISSOR))
        buttonScissor.place(relx=0.7, rely=0.35)

        # Random button
        random_button = ctk.CTkImage(light_image=self.loadBgImage(self.fileRandom),
                                     dark_image=self.loadBgImage(self.fileRandom), size=(180, 150))
        buttonRandom = ctk.CTkButton(framePPC, text="Random", text_color="black", width=20, height=20,
                                     bg_color=self.color,
                                     fg_color=self.color, hover_color=self.hover_color, image=random_button,
                                     corner_radius=80, compound="top",
                                     font=(self.police, self.Ptaille, "bold"), command=lambda:self._game_pfc.rockPaperScissors())
        buttonRandom.place(relx=0.45, rely=0.68)
        return framePPC

    def loadBgImage(self, imagefile):
        """! Renvoie une image redimensionnée pour l'interface.
        @param String. Chemin de l'mage à charger
        @return CTkImage. L'image redimensionnée pour l'interface.
        @details Cette méthode utilise la bibliothèque Pillow pour ouvrir et redimensionner une image"""
        img = openImg.open(imagefile)
        resized_img = img.resize(size=(self.__window.winfo_screenwidth(), self.__window.winfo_screenheight()),
                                 resample=5)
        return resized_img

    def getFramePPC(self):
        """! Renvoie le cadre principal de l'interface.
        @param  None
        @return  CTkFrame. Le cadre principal de l'interface.
        @details Cette méthode est utilisée pour obtenir le cadre principal de l'interface utilisateur."""
        return self.__createFramePPC()

    def execute(self, function):
        """! Cette fonction est utilisée pour exécuter une fonction passée en paramètre.
        @param function. La fonction à exécuter.
        @return  None."""
        function()