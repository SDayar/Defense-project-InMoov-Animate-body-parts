## @file Principale.py
## @author Shérine
## @date 24/04/2025
## @brief Frame Menu de l'application qui permet d'accéder aux fonctionnalités : ouvrir la main, fermer la main. Et d'accéder à la frame Jeux.
## @details Ce module définit la frame Menu pour les actions basiques de la main robotisée et accéder à la frame des jeux.
## @class Principale
## @brief Classe représentant la frame menu de l'application.
## @details Permet à l'utilisateur d'ouvrir/fermer la main ou d'accéder aux jeux.
##@package L2L1


##@see customtkinter
import customtkinter as ctk 
##@see PIL.Image
import PIL.Image as openImg
##@see Enumerations.EnumMovement
from Enumerations.EnumMovement import EnumMovement as EM
##@see Movement
from Movement import Movement


class Principale():
    ##@class Principale
    ##@bref Responsable de la frame "Principale".
    ##@package Principale
    

        
    def __init__(self, window): 
        """! 
        @brief Constructeur de la classe Principale.
        @param CTk. La fenêtre principale dans laquelle la frame sera intégrée.
        @return None"""
        ##@var __window
        ##@brief Contient l'instance de la fenêtre du logiciel.
        self.__window = window  # Fenêtre principale
        ##@var __buttonClickfont 
        ##@brief Contient la taille et le style d'écriture des textes placés au niveau des boutons. 
        self.__buttonClickfont = ctk.CTkFont(family="<codec Pro>", size=15)
        ##@var __fileGame
        ##@brief Chemin vers l'image de manette de jeux.
        self.__fileGame="images/game.png"
        ##@var __colorFondImage
        ##@brief Contient un code d'hexadécimale pour les couleurs de fonds des images de la frame.
        self.__colorFondImage="#E6E6FA" 
        ##@var __fileStop
        ##@brief Chemin vers l'image STOP.
        self.__fileStop="images/STOP.png"
        ##@var __fileOhand
        ##@brief Chemin vers l'image openHand.
        self.__fileOhand="images/openHand.png"
        ##@var __fileChand
        ##@brief Chemin vers l'image CloseHand.
        self.__fileChand="images/closeHand.png"
        ##@var __color
        ##@brief Couleur de fond de la frame.
        self.__color="#b9e4f0"  # Couleur de fond
        ##@var __hover_color
        ##@brief Couleur appliquée aux boutons lors d'un survol.
        self.__hover_color="#FFF0F5"  
        ##@var __police
        ##@brief Police appliquée aux textes de la frame.
        self.__police="<codec Pro>"  # Police 
        ##@var __Ptaille
        ##@brief Taille de la police.
        self.__Ptaille=20  # Taille du texte
        ##@var _switchFrame
        ##@brief Contient la méthode qui permettra d'accéder à la frame suivante.
        self._switchFrame = None  #: Méthode pour changer de frame.
        ##var __objectMovement
        ##@brief Instance de la classe Movement. Elle permet d'initier un mouvement.
        self.__object_movement = Movement()  # Instance pour contrôler les mouvements

   
    def __createFramePrincipale(self):
        """!
        @brief Crée et retourne la frame principale avec ses boutons.
        @param None
        @return CTkFrame. Un objet CTkFrame contenant les boutons d'action."""
        framePrincipale = ctk.CTkFrame(self.__window,
                                       width=self.__window.winfo_screenwidth(),
                                       height=self.__window.winfo_screenheight(),
                                       fg_color=self.__color)

        # Bouton STOP
        ##  @details Ce bouton est utilisé pour arrêter tous les mouvements de la main et ouvrir la main.
        stop_button = ctk.CTkImage(light_image=self.load_bg_image(self.__fileStop),
                                   dark_image=self.load_bg_image(self.__fileStop),
                                   size=(200, 130))
        buttonStop = ctk.CTkButton(master=framePrincipale, text="", width=10, height=15,
                                   image=stop_button, bg_color=self.__color, fg_color=self.__color,
                                   hover_color="#FFB3B3", corner_radius=80)
        buttonStop.place(relx=0.78, rely=0.78)

        # Bouton "Open Hand"
        ##  @details Ce bouton est utilisé pour ouvrir la main.
        open_button = ctk.CTkImage(light_image=self.load_bg_image(self.__fileOhand),
                                   dark_image=self.load_bg_image(self.__fileOhand),
                                   size=(200, 250))
        buttonOpen = ctk.CTkButton(master=framePrincipale, text="Open Hand", text_color="black",
                                   width=150, height=100, fg_color=self.__color, hover_color=self.__hover_color,
                                   bg_color=self.__color, image=open_button, compound="top",
                                   font=(self.__police, self.__Ptaille, "bold"), corner_radius=80,
                                   command=lambda: self.__object_movement.create_movement(EM.OPENHAND))
        buttonOpen.place(relx=0.04, rely=0.172)

        # Bouton "Close Hand"
        ##  @details Ce bouton est utilisé pour fermer la main.
        close_button = ctk.CTkImage(light_image=self.load_bg_image(self.__fileChand),
                                    dark_image=self.load_bg_image(self.__fileChand),
                                    size=(188, 180))
        buttonClose = ctk.CTkButton(master=framePrincipale, text="Close Hand", text_color="black",
                                    width=150, height=100, fg_color=self.__color, hover_color=self.__hover_color,
                                    bg_color=self.__color, image=close_button, compound="top",
                                    font=(self.__police, self.__Ptaille, "bold"), corner_radius=80,
                                    command=lambda: self.__object_movement.create_movement(EM.CLOSEHAND))
        buttonClose.place(relx=0.32, rely=0.274)

        # Bouton "Games"
        ##  @details Ce bouton est utilisé pour accéder à la frame des jeux.
        game_button = ctk.CTkImage(light_image=self.load_bg_image(self.__fileGame),
                                   dark_image=self.load_bg_image(self.__fileGame),
                                   size=(200, 200))
        buttonGame = ctk.CTkButton(master=framePrincipale, text="Games", text_color="black",
                                   width=150, height=150, fg_color=self.__colorFondImage,
                                   hover_color=self.__hover_color, bg_color=self.__color,
                                   image=game_button, compound="top",
                                   font=(self.__police, self.__Ptaille, "bold"),
                                   command=lambda: self.execute(self._switchFrame(2)), corner_radius=80)
        buttonGame.place(relx=0.64, rely=0.252)

        return framePrincipale

   
    def load_bg_image(self, imagefile):
        """!
        @brief Charge une image de fond redimensionnée à la taille de la fenêtre.
        @param String. Chemin vers l’image à charger.
        @return PIL.Image. Une image PIL redimensionnée."""
        img = openImg.open(imagefile)
        resized_img = img.resize(size=(self.__window.winfo_screenwidth(),
                                       self.__window.winfo_screenheight()), resample=5)
        return resized_img

   
    def get_frame_principale(self):
        """!
        @brief Retourne la frame principale.
        @param None
        @return CTkFrame. La frame "Menu"."""
        return self.__createFramePrincipale()

    
    def execute(self, function):
        """!
        @brief Méthode utilitaire pour exécuter une fonction passée en paramètre.
        @param function. La fonction à exécuter.
        @return None"""
        lambda: function()
