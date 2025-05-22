##  @author Saifidine Dayar
##  @date 06/03/2025
##  @brief Main.py Contient la classe Main qui permet de gérer la fenêtre principale de l'application.
##  @version 08/05/2025
##  @file Main.py
##  @package L2L1


## Tkinter est une bibliothèque standard de Python pour créer des interfaces graphiques.
import tkinter as tk
## CustomTkinter est une bibliothèque tierce qui permet de créer des interfaces graphiques plus modernes et personnalisables.
import customtkinter as ctk
##@see Mediator
from Mediator import Mediator
##@see PrepareArduinoBoard
from PrepareArduinoBoard import PrepareArduinoBoard
## threading est une bibliothèque standard de Python pour créer des threads.
from threading import Thread
class Main():
    ## @class Main
    ## @brief Main Permet de créer la fenêtre principale de l'application qui par défaut contient la frame d'accueil.
    ## @details Elle permet de créer la fenêtre principale de l'application, de la configurer, de créer la frame d'accueil et de gérer les erreurs lors de l'ouverture d'une fenêtre.
    ##          De plus, elle est programmée afin de de placer ou de cacher une frame, de changer de frame, de revenir à la frame précédente et de mettre à jour le status de la carte Arduino sur le GUI.
    ## @see Mediator
    ## @see PrepareArduinoBoard
    ## @package Main
    def __init__(self):
        """! Initialise la fenêtre de l'application et les objets nécessaires à son fonctionnement.
        @param None
        @return None"""
        ##@var __window.
        ##@bref Contient la fenêtre du logiciel.
        self.__window = ctk.CTk()

        ##@var ___object_prepare_arduino
        ##@bref Objet de la classe PrepareArduinoBoard qui permet de préparer la carte Arduino.
        self.__object_prepare_arduino = PrepareArduinoBoard()

        ##@var __labelBgcolor 
        ##@bref Contient la couleur de fond des widgets de la fenêtre d'accueil.
        self.__labelBgcolor = "#b9e4f0"
        self.__win_config()

        ##@var __textTouchFont  
        ##@bref Contient les paramètres du style de font apporté aux textes de la fenêtre d'accueil.
        self.__textTouchfont = ctk.CTkFont(family="<codec Pro>",size=118)

        ##@var __textWorld_withfont
        ##@bref Ces paramètres sont appliqués à une partie du texte de la fenâtre d'accueil.
        self.__textWorld_withfont = ctk.CTkFont(family="<codec Pro>",size=18)

        ##@var __textInmoovfont
        ##@bref Ces paramètres sont appliqués à une partie du texte de la fenâtre d'accueil.
        self.__textInmoovfont = ctk.CTkFont(family="<Migra>",slant="italic", size=34)

        ## @var __textBgTouchcolor 
        ##@bref Contient la couleur de fond d'une partie du texte de la fenêtre d'accueil.
        self.__textBgTouchcolor="#b9e4f0"

        ## @var __textBgWorld_withcolor 
        ## @bref Contient la couleur de fond d'une partie du texte de la fenêtre d'accueil.
        self.__textBgWorld_withcolor="#b9e4f0"

        ## @var __textBgWorld_withcolor 
        ## @bref Contient la couleur de fond d'une partie du texte de la fenêtre d'accueil.
        self.__textInmoovcolor = "#b9e4f0"

        ## @var __buttonClickcolor 
        ## @bref Contient la couleur de fond d'une partie du texte de la fenêtre d'accueil.
        self.__buttonClickcolor = "#b9e4f0"

        ##@var __buttonClickfont 
        ## @bref Ces paramètres sont appliqués à tous les boutons de la fenâtre d'accueil.
        self.__buttonClickfont = ctk.CTkFont(family="<codec Pro>", size=15)

        ## @var __objectMediator 
        ## @bref Un objet de la classe Mediator.
        ## @ref Mediator
        self.__objectMediator = Mediator() 
        
        ## Initialise l'attribut de Mediator chargé de contenur la frame par défaut.
        self.__objectMediator.__defaultFrame = self.set_default_frame

        #Initialise l'attribut de Mediator chargé de contenir la méthode pour la fonctionnalité back
        self.__objectMediator._back=self.__back
        #Initialise l'attribut de Mediator chargé de contenir la méthode pour la fonctionnalité switch
        self.__objectMediator._switchFrame = self.__switchFrame
        #Initialise l'attribut de Mediator chargé de contenir la fenêtre.
        self.__objectMediator.win = self.get_window()
        #Initialise l'attribut de Mediator chargé de contenir la méthode pour renderFrame.
        self.__objectMediator.renderFrame = self.render_frame 
        #Exécute la second constructeur dans le médiator.
        self.__objectMediator._init_ObjectModules()
        #On initialise la frame actuelle et la frame précédente. La frame actuelle est la frame par défaut du logiciel. Et la précédente est None car il n'y avait pas de fenêtre précédente lors du lancement du logiciel.
        ##@var __actualFrame 
        ##@bref Frame d'accueil. Elle est affichée dès l'exécution du logiciel.
        self.__actualFrame = self.set_default_frame()
        ##@var __previousFrame
        ##@bref Frame Précédente.
        self.__previousFrame = None
        ##Affichage de la frame par défaut lors de l'exécution du logiciel.
        self.render_frame(self.__actualFrame)
    def __win_config(self):
        """! Configure la fenêtre du logiciel. 
        @param None
        @return None"""
        self.__window.title("InMoovConnect")
        self.__window.geometry("1100x700+{}+{}".format(self.__window.winfo_screenwidth()//2 - 450, self.__window.winfo_screenheight()//2 -355))
        self.__window.iconbitmap("images/logo.ico")#On met l'icone de la fenêtre
        self.__window.resizable(False, False)
        t_prepare_arduino = Thread(target=self.__object_prepare_arduino.set_arduino_board_ready)
        t_prepare_arduino.start()
    def render_frame(self,newframe):
        """! Affiche une frame. 
        @param CTkFrame. Une frame de type CTkFrame.
        @return None
        @see Mediator"""
        try:
            self.__previousFrame = self.__actualFrame
            if type(self.__actualFrame) == ctk.CTkFrame:
                self.hide_frame(self.__actualFrame)
            self.__actualFrame = newframe
            self.__actualFrame.pack(fill="both", expand=True)
        except tk.TclError as e:
            self.__objectMediator.errorLaunchingFrame(e)

    def hide_frame(self,frame):
        """! Cache une frame.
        @param CTkFrame. Une frame de type CTkFrame.
        @return None"""
        frame.pack_forget()
    def get_window(self):
        """! Renvoie la fenêtre du logiciel.
        @param None
        @return CTk. La fenêtre de l'application de type CTk."""
        return self.__window
    def __create_default_frame(self):
        """! Crée et configure le service Welcome
        @param None
        @return CTkFrame. La frame d'accueil de type CTkFrame."""
        
        defaultFrame= ctk.CTkFrame(self.__window, bg_color=self.__labelBgcolor, fg_color="transparent")

        labelTouchText = ctk.CTkLabel(defaultFrame,fg_color="transparent",bg_color=self.__textBgTouchcolor,
                                       text="Touch",text_color="white", font=self.__textTouchfont)
        labelTouchText.place(relx=0.07,rely=0.1)

        labelWorldWithText = ctk.CTkLabel(defaultFrame,bg_color=self.__textBgWorld_withcolor,fg_color="transparent",
                                       text="the world with",text_color="white", font=self.__textWorld_withfont)
        labelWorldWithText.place(relx=0.08,rely=0.27)

        labelInmoovtext = ctk.CTkLabel(defaultFrame, bg_color=self.__textInmoovcolor, fg_color="transparent",
                                   text="InMoovConnect",text_color="black", font=self.__textInmoovfont)
        labelInmoovtext.place(relx=0.67,rely=0.3)
         
        buttonToMain = ctk.CTkButton(defaultFrame, corner_radius=20, text="Click here to continue !",text_color="black", bg_color=self.__buttonClickcolor, font=self.__buttonClickfont, command=lambda:self.__switchFrame(1))
        buttonToMain.place(relx=0.4,rely=0.6)
        self.__status_frame = ctk.CTkLabel(self.__window, width=500, height=30, corner_radius=20, fg_color="red", bg_color=self.__labelBgcolor,text=PrepareArduinoBoard.info,text_color="white", font=ctk.CTkFont(family="<Migra>",slant="italic", size=10))
        self.__status_frame.place(relx=0.3,rely=0.01)
        t_update_status_frame = Thread(target=self.__update_arduino_status)
        t_update_status_frame.start()
        return defaultFrame
    def set_default_frame(self):
        """! Retourne la frame d'accueil
        @param None
        @return CTkFrame. La frame d'accueil de type CTkFrame. Qui est la frame par défaut de l'application."""
        return self.__create_default_frame()
    def __switchFrame(self,N_FRAME):
        """! Permet de changer de frame.
        @param int. Un entier qui représente l'ID de la frame à afficher.
        @return None
        @see Mediator"""
        self.__objectMediator.renderFrameOrNo(N_FRAME)
    def __back(self):
        """! Permet de revenir au frame précédent sans passer par le médiateur.
        @param None
        @return None
        @see Mediator"""
        try : 
            self.render_frame(self.__previousFrame)
        except Exception as e :
            self.__objectMediator.errorLaunchingFrame("Désolé ! Aucune fenêtre ne précède celle-là.\nDescription technique : "+e)
    def __update_arduino_status(self):
        """! Met à jour le status de la carte Arduino sur le GUI.
        @param None
        @return None
        @see PrepareArduinoBoard"""
        if PrepareArduinoBoard.connected:
            self.__status_frame.configure(text=PrepareArduinoBoard.info, fg_color="#7ed079")
            self.__object_prepare_arduino.set_arduino_board_ready()
        else:
            self.__status_frame.configure(text=PrepareArduinoBoard.info, fg_color="red")
            self.__object_prepare_arduino.set_arduino_board_ready()
        self.__window.after(100, self.__update_arduino_status)

        
    

## @var AppInMoovConnect 
##@bref Un objet de la classe Main qui permet de gérer la fenêtre principale de l'application.
AppInMoovConnect = Main()
##@brief Lancement de l'application InMoovConnect.
AppInMoovConnect.get_window().mainloop()#On lance la loupe de la fenêtre
         
