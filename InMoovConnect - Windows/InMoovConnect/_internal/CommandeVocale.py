##@file  CommandeVocale.py
##@brief Ce fichier contient la classe CommandeVocale qui gère les commandes vocales pour contrôler une main robotique.
#Ce module regroupe toutes les fonctionnalités nécessaires pour les actions de la main
#robotique prise par la commande vocale et enoncé par l'utilisateur.Ces actions vont être transmise 
#à la main a l'aide de signaux fourni par Arduino.
##@authors  
# - Loic Jin
# - Saifidine Dayar 
##@version  11/05/2025 

##@package L2L1


import customtkinter as ctk
##@see matplotlib.pyplot est utilisé pour afficher le graphique de l'intensité du son.
from PIL import Image
##@see tkinter est utilisé pour créer l'interface graphique de l'application.
import tkinter as tk
##@see os 
import os
##@see speech_recognition est utilisé pour la reconnaissance vocale.
import speech_recognition as reconaissance_de_son
##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter.messagebox import showinfo,showerror
##@see Movement est utilisé pour gérer les mouvements de la main robotique.
from Movement import Movement
##@see Enumerations.EnumMovement est utilisé pour gérer les mouvements de la main robotique.
from Enumerations.EnumMovement import EnumMovement as EM
##@see GameFactory est utilisé pour créer instancier des jeux.
from GameFactory import GameFactory
##@see PersonalizedMovement est utilisé pour traiter les mouvements personnalisés de la main robotique.
from PersonalizedMovement import PersonalizedMovement


#La classe CommandeVocale est responsable de la gestion des commandes vocales pour contrôler les mouvements de la main robotique.
#Elle utilise la bibliothèque speech_recognition pour reconnaître les commandes vocales et exécuter les mouvements appropriés.
#Elle crée également une interface utilisateur avec des boutons pour interagir avec la main robotique.

class CommandeVocale:
    ##@class CommandeVocale
    ##@brief La classe CommandeVocale est responsable de la gestion des commandes vocales pour contrôler les mouvements de la main robotique.
    ##@package CommandeVocale
    __created = False
    def __init__(self, window):
        """! Constructeur de la classe CommandeVocale.
        @param CTk. La fenêtre principale de l'interface graphique. Il est nécessaire à la création des "top-level".
        @return None"""
        ##@param window : CTk. La fenêtre principale de l'application.
        ##@details Cette méthode initialise les attributs de la classe, charge les images nécessaires, crée les boutons et configure l'interface utilisateur.
        ##@return None."""
        ##@var __window CTk. La fenêtre principale du logiciel.
        self.__window = window
        ##@var __fond str. Le chemin de l'image d'arrière-plan.
        self.__fond = "images/Bg.png" 
        ##@var __back str. Le chemin de l'image du bouton retour.
        self.__back = "images/back.png" 
        ##@var __stop str. Le chemin de l'image du bouton stop.
        self.__stop = "images/STOP.png"  
        ##@var __voc str. Le chemin de l'image du bouton de commande vocale.
        self.__voc = "images/micro.png"  
        ##@var __menu str. Le chemin de l'image du bouton menu.
        self.__menu = "images/menu.png"  
        ##@var __logo str. Le chemin de l'image du logo.
        self.hover_color = "#FFF0F5" 
        ##@var color str. La couleur de fond de l'interface.
        self.color = "#b9e4f0"
        ##@var __logo str. Le chemin de l'image du logo.
        self.__logo="images/logo.ico"
        ##@var _family CTkFont. La police de caractères utilisée dans l'interface.
        self._family=ctk.CTkFont(family="<codec Pro>",size=15)
        ##@var _buttonClickcolor str. La couleur de fond des boutons au clic.
        self._buttonClickcolor="#b9e4f0"
        ##@var _back None. La fonction de retour au thread précédent.
        self._back = None 
        ##@var _switchFrame None. La fonction de changement de frame.
        self._switchFrame = None 
        ##@var _object_movement Movement. L'objet responsable de la gestion des mouvements de la main.
        self.__object_movement = Movement()
        ##@var __game_sign_language GameFactory. L'objet responsable de la gestion du langage des signes.
        self.__game_sign_language = GameFactory("SignLanguage").get_game()
        ##@var __game_pfc GameFactory. L'objet responsable de la gestion du jeu Pierre-Papier-Ciseaux.
        self.__game_pfc = GameFactory("PPC").get_game()
        ##@var _vocaleBox None. La boîte de dialogue pour la commande vocale.
        self._vocaleBox=None
        ##@var _contrainte: None. La contrainte pour la saisie des degrés.
        self._contrainte=self.__window.register(self._constraint)
        ##@var _createButtonFrame: CTkFrame. Le cadre principal de l'interface.
        self._createButtonFrame()
        ##@var _list_commmande_ambigu: list. La liste des commandes ambiguës.
        self.__list_commmande_ambigu = ["ouvrir", "fermer","compter","ouvre","ferme","jeu"]
        ##var _list_commande_non_ambigu: list. La liste des commandes non ambiguës.
        self.__list_commande_non_ambigu = [
                        "pierre" ,
                        "papier",
                        "ciseau",
                        "stop",
                        "ouvre la main",
                        "ourvrir la main",
                        "ferme la main",
                        "fermer la main",
                        "ouvre l'index",
                        "ouvrir l'index",
                        "fermer l'index",
                        "ferme l'index",
                        "ouvre le majeur",
                        "ouvrir le majeur",
                        "ferme le majeur",
                        "fermer le majeur",
                        "ouvre l'annulaire",
                        "ouvrir l'annulaire"
                        "ferme l'annulaire", 
                        "fermer l'annulaire",
                        "ouvre l'auriculaire",
                        "ouvrir l'auriculaire",
                        "ferme l'auriculaire",
                        "fermer l'auriculaire"
                        "ouvre le pouce",
                        "ouvrir le pouce"
                        "fermer le pouce",
                        "ferme le pouce",
                        
                        ]  
         
        if os.path.exists(self.__fond):  
            Image.open(self.__fond)
        else: 
            print(f"Erreur : L'image '{self.__fond}' est introuvable.")

    def load_img(self, path, size):
        """! Renvoie une image redimensionnée pour l'interface."""
        ##@param String . Le chemin de l'image à charger.
        ##@param tuple. La taille de l'image à redimensionner.
        ##@return  CTkImage. L'image redimensionnée pour l'interface.
        ##@details Cette méthode utilise la bibliothèque Pillow pour ouvrir et redimensionner une image,
        
        img = Image.open(path)  # Ouverture de l'image avec Pillow
        img = img.resize(size)  # Redimensionne l'image
        return ctk.CTkImage(light_image=img, dark_image=img, size=size) # Crée l'image CTk pour CustomTkinter
    
    def _createButtonFrame(self):
        """! Cette fonction permet la dimensionnement des boutons dans la fenêtre."""
        ##@param None.
        ##@return CTkFrame. Le cadre principal de l'interface.
        frameCV = ctk.CTkFrame(self.__window, width=self.__window.winfo_screenwidth(),
                                        height=self.__window.winfo_screenheight(), fg_color=self.color)
        
        subframe1 = self.subFrame(frameCV,0.6,0.4,4.5,5)
        subframe2 = self.subFrame(frameCV,0.6,0.1,5,5.6)
        subframe1.configure(fg_color=self.color,corner_radius=30)
        subframe2.configure(fg_color=self.color,corner_radius=30)
        # Bouton retour
        backButtonImage = self.load_img(self.__back, (130, 100))
        backButton = ctk.CTkButton(frameCV, image=backButtonImage, text="",
                                   hover_color=self.hover_color, fg_color=self.color,
                                   bg_color=self.color, corner_radius=40, width=150, height=200,command=lambda: self.execute(lambda:self._back()))
        backButton.place(relx=0, rely=0)
        # Bouton menu
        menuButtonImg = self.load_img(self.__menu, (130, 100))
        menuButton = ctk.CTkButton(frameCV, image=menuButtonImg,text="",
                                   hover_color=self.hover_color, fg_color=self.color,
                                   bg_color=self.color, corner_radius=20, width=140, height=120,
                                   command=lambda: self.execute(lambda:self._switchFrame(1)))
        menuButton.place(relx=0, rely=0.35)
        # Bouton stop
        stopButtonImage = self.load_img(self.__stop, (200, 130))
        stopButton = ctk.CTkButton(frameCV, image=stopButtonImage, text="",
                                   fg_color=self.color, bg_color=self.color, width=20, height=20,
                                   hover_color=self.hover_color, corner_radius=40,command=lambda:self.__object_movement.create_movement(EM.STOP))
        stopButton.place(relx=0.75, rely=0.7)
        # Bouton de commande vocale
        recognitionButtonImg = self.load_img(self.__voc, (130, 100))
        recognitionButton = ctk.CTkButton(frameCV, image=recognitionButtonImg, text="Voice control",
                                          compound="top", font=self._family, text_color="black",
                                          fg_color=self.color, bg_color=self.color, hover_color=self.hover_color,
                                          command=self.vocale, corner_radius=30)
        recognitionButton.place(anchor="center", relx=0.3, rely=0.5)
        #************************************************************************************************************************************************#
        #Frame pour bouger individuellement des doigts
        label_language = ctk.CTkLabel(subframe2, text="Enter a sentence",font=self._family,text_color="black",width=-100,height=1)
        label_language.place(anchor="ne",relx=0.6,rely=0.1)
        
        word = ctk.CTkEntry(subframe2, width=100, font=self._family, justify="center", fg_color="white",text_color="black",bg_color="white")
        word.place(anchor="ne",relx=0.64,rely=0.3)
        button_send_word = ctk.CTkButton(subframe2, corner_radius=20, text="Submit your sentence", text_color="black", bg_color= self.color,font=self._family,command=lambda:self.__game_sign_language.mimic_language(word.get()))
        button_send_word.place(anchor="ne",relx=0.72,rely=0.7)
        #****************************************************************************************************************************************************#
        label_degree = ctk.CTkLabel(subframe1, text="Enter degrees",font=self._family,text_color="black",width=-100,height=1)
        label_degree.place(anchor="ne",relx=0.69 , rely=0.1)
        self.create_numeric_entries_and_labels(frameCV)
        return frameCV

   
    def create_numeric_entries_and_labels(self, frameCV):
        """! Crée des champs de saisie pour les angles des doigts."""
        ##@param CTkFrame. Le cadre dans lequel les champs de saisie et les labels seront placés.
        ##@return None.
        ##@details Cette méthode crée six champs de saisie pour les angles des doigts(pouce, index, majeur, annulaire, auriculaire et poignet)"""
        self.entries = []
        x_pos = 680
        i=0
        for i in range(6):
            entry = ctk.CTkEntry(frameCV, width=40, font=self._family, 
                                 justify="center",
                                 text_color="black",bg_color="white",
                                 ) 
            entry.place(x=x_pos, y=350)
            self.entries.append(entry)
            x_pos += 50 #décalage entre les cases de 50px
        #**********************************************************************************************************************************************#

        ##@brief Ajout des labels en bas des champs de saisi. L'ordonné de chaque label est décalé de 50 px par rapport à celui de son champs de saisi respectif.
        thumb_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),
                                   text="Thumb",text_color="black",bg_color=self.color,
                                   fg_color="transparent")
        thumb_label.place(x=680,y=380)
        index_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),text="Index",
                                   text_color="black",bg_color= self.color,
                                   fg_color="transparent")
        index_label.place(x=730,y=380)
        mf_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),text="M.\nFinger",
                                text_color="black",bg_color= self.color,
                                fg_color="transparent")
        mf_label.place(x=780,y=380)
        ring_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),text="Ring",
                                  text_color="black",bg_color= self.color,
                                  fg_color="transparent")
        ring_label.place(x=830,y=380)
        pinky_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),text="Pinky",
                                   text_color="black",bg_color= self.color,
                                   fg_color="transparent")
        pinky_label.place(x=880,y=380)
        wrist_label = ctk.CTkLabel(frameCV, width=40, font=(self._family,12),text="Wrist",
                                   text_color="black",bg_color= self.color,
                                   fg_color="transparent")
        wrist_label.place(x=930,y=380)
        entry_button = ctk.CTkButton(frameCV, corner_radius=20, text="Submit positions ! ",
                                      text_color="black", bg_color= self.color,
                                      font=self._family, command=lambda:PersonalizedMovement.send_personalized_positions([entry.get() for entry in self.entries]))
        
        entry_button.place(x=(680+((930-680)/3)),y=420) #La position de ce bouton se trouve sur la médiane entre les positions (680,450) et (930,450)


    
    def _constraint(self, val):
        """! Cette fonction est utilisée pour valider la saisie de l'utilisateur."""
        ##@param String. La valeur saisie par l'utilisateur.
        ##@return  boolean. True si la valeur est valide, False sinon.
        ##@details Cette méthode vérifie si la valeur saisie est un entier compris entre 0 et 180 pour les doigts."""
        if val == "":
            return True
        if not val.isdigit() :
            showerror("Type non autorisée","Veuillez saisir un nombre entier")
            return False
        nb=int(val)
        if 0<=nb<=180:
            return True
        showerror("Plage de nombre non autorisée","Veuillez saisir une valeur comprise entre 0 et 180 !")  
        return False
   
    def vocale(self):
        """! Cette fonction crée une nouvelle fenêtre pour la commande vocale."""
        ##@param  None   
        #@return None
        #@details Cette méthode crée une nouvelle fenêtre pour la commande vocale et y place un bouton pour activer la reconnaissance vocale."""
        if CommandeVocale.__created == False :
            CommandeVocale.__created = True
            vocale_box = tk.Toplevel(self.__window) #création de la deuxième fenêtre
            vocale_box.geometry("700x700")
            vocale_box.configure(bg="#7acefa")
            vocale_box.resizable(False, False)
            vocale_box.iconbitmap(self.__logo)
            vocale_box.overrideredirect(True)
            self.__window.update_idletasks()#obtenir les dimensions de la fenêtre principale   
            width = self.__window.winfo_width()
            height = self.__window.winfo_height()
            TopLevelx = self.__window.winfo_rootx()
            TopLevely = self.__window.winfo_rooty()
            w, h = 700, 700                       
            x = TopLevelx + (width - w) // 2
            y = TopLevely + (height - h) // 2
            vocale_box.geometry(f"{w}x{h}+{x}+{y}") #centre la deuxième fenêtre au milieu de la première
        
       



            self.voc = ctk.CTkButton(vocale_box,
                                text="Tap to Talk",text_color="black",
                                fg_color="white",
                                width=80,
                                height=40,
                                hover_color=self.hover_color,
                                corner_radius=80,
                                command=self.user_sound)
            
            quitter = ctk.CTkButton(vocale_box,
                                text="Close",text_color="black",
                                fg_color="white",
                                width=80,
                                height=40,
                                hover_color=self.hover_color,
                                corner_radius=80,command=lambda:quit())
            self.voc.pack(pady=20)
            quitter.pack(pady=60)
            
            def quit():
                CommandeVocale.__created = False
                vocale_box.destroy()

    #la fonction suivante est utilisé pou connecter le micro au graphe afin d'afficher 
    #l'intensite du son de l'utilisateur en temps réel.
    #Autre solution est d'afficher le graphe sur un autre fenêtre mais cela rendrait 
    #l'interface trop lourde en terme de consommation mémoire 
    """def on_speak(self):
        Self -> None
            Cette fonction lance le graphique si le micro est detecter .
        if self.voc.isrunning:
            self.audio_effect.start()
            self.audio_effect.update_audio()
        thread = threading.Thread(target=self.user_sound)
        thread.start()
        """
    
    def user_sound(self):
        """! Cette fonction est utilisée pour activer la reconnaissance vocale.
        @param  None
        @return  None
        @details Cette méthode utilise la bibliothèque speech_recognition pour écouter la voix de l'utilisateur
        et reconnaître la commande vocale. Si la commande est reconnue, elle est traitée.Sinon elle renvoie une erreur.
        """
        
        son = reconaissance_de_son.Recognizer()
        with reconaissance_de_son.Microphone() as source: #activation de la reconnaissance vocale
                # showinfo("Information"  , " Veuillez énoncer votre commande :")
                try:
                    audio = son.listen(source, timeout=10, phrase_time_limit=10)
                    texte = son.recognize_google(audio, language="fr-FR") #cette ligne convertit la commande en francais 
                    
                    if texte in self.__list_commmande_ambigu: #execute l'action si reconnu dans le dictionnaire
                        self.parse_command(texte)
                    elif texte in self.__list_commande_non_ambigu : #execute l'action si reconnu dans le dictionnaire
                        self.treat_command(texte) 
                    else: #sinon envoie une erreur sous forme de boite de dialogue
                        showinfo("Erreur" , "Commande non reconnue. Essayez encore.")
                        return None
                except reconaissance_de_son.UnknownValueError: #Lève une erreur si la commande n'est pas reconnue. 
                    showinfo("Erreur" ,  "Votre commande n'est pas compréhensible")
                    return None
    

  
    def getFrameCV(self):
        """! Renvoie le cadre principal de l'interface.
        @param  None
        @return  CTkFrame. Le cadre principal de l'interface.
        @details Cette méthode est utilisée pour obtenir le cadre principal de l'interface utilisateur."""
        return self._createButtonFrame()
    
    
    def execute(self, function):
        """! Cette fonction est utilisée pour exécuter une fonction passée en paramètre.
        @param function. La fonction à exécuter. 
        @return  None."""
        function()
        
    
 

    
    
    def subFrame(self,frame,X, Y, divX ,divY):
        """! Creation de sous frame dans la frame principale.
        @author Saifidine Dayar
        @param frame :CTkFrame(). la frame principale
        @param X :float. la position de la frame sur l'axe des abscisses.
        @param Y :float. la position de la frame sur l'axe des ordonnées. 
        @param divX :float. le diviseur de la largeur de la frame principale.
        @param divY :float. le diviseur de la hauteur de la frame principale.
        @return CTkFrame(). la sous frame créée.
        """
        subFrame = ctk.CTkFrame(frame, width=frame.winfo_screenwidth()//divX, height=frame.winfo_screenheight()//divY,fg_color=self.color)
        subFrame.place(relx=X, rely=Y)
        return subFrame
    def parse_command(self,command):
        """! Transforme une commande vocale reconnue en une suite de mouvements.
        @author Saifidine Dayar
        @param command :str. la commande vocale reconnue.
        @return None.
        """
        if command == "ouvrir":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant le membre à ouvrir : Main, pouce , index, auriculaire, majeur, ou annulaire.")
        elif command == "fermer":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant le membre à fermer : Main, pouce , index, auriculaire, majeur, ou annulaire.")
        elif command  == "compter":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant jusqu'à quel nombre compter : 0 à 31.")
        elif command == "ouvre":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant le membre à ouvrir : Main, pouce , index, auriculaire, majeur, ou annulaire.")
        elif command == "ferme":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant le membre à fermer : Main, pouce , index, auriculaire, majeur, ou annulaire.")
        elif command == "jeu":
            showinfo("Information ","Votre commande est ambiguë. Veuillez réessayer en précisant le jeu à lancer : Pierre, papier, ciseaux.")
        else:
            showinfo("Information ","Commande non reconnue. Essayez encore.")
    def treat_command(self,command):
        """! Traite une commande vocale reconnue et non ambigûe.
        @author Saifidine Dayar
        @param command : str. La commande vocale reconnue et non ambigûe.
        @return  None"""
        if command == "pierre":
            self.__game_pfc.rock()
        elif command == "papier":
            self.__game_pfc.paper()
        elif command == "ciseau":
            self.__game_pfc.scissor()
        elif command == "stop":
            self.__object_movement.create_movement(EM.STOP)
        elif command == "ouvre la main" or command == "ouvrir main" or command == "main ouvrir":
            self.__object_movement.create_movement(EM.OPENHAND)
        elif command == "ferme la main" or command == "fermer main" or command == "main fermer":
            self.__object_movement.create_movement(EM.CLOSEHAND)
        elif command == "ouvre l'index":
            self.__object_movement.create_movement(EM.OPENINDEX)
        elif command == "ferme l'index":
            self.__object_movement.create_movement(EM.CLOSEINDEX)
        elif command == "ouvre le majeur":
            self.__object_movement.create_movement(EM.OPENMIDDLE)
        elif command == "ferme le majeur":
            self.__object_movement.create_movement(EM.CLOSEMIDDLE)
        elif command == "ouvre l'annulaire":
            self.__object_movement.create_movement(EM.OPENRING)
        elif command == "ferme l'annulaire":
            self.__object_movement.create_movement(EM.CLOSERING) 
        elif command == "ouvre l'auriculaire":
            self.__object_movement.create_movement(EM.OPENPINKY) 
        elif command == "ferme l'auriculaire":
            self.__object_movement.create_movement(EM.CLOSEPINKY) 
        elif command == "ouvre le pouce":
            self.__object_movement.create_movement(EM.OPENTHUMB) 
        elif command == "ferme le pouce":
            self.__object_movement.create_movement(EM.CLOSETHUMB)
        else:
            showinfo("Information ","Commande non reconnue. Essayez encore.")
    #**************************************************************************************************************#
      

