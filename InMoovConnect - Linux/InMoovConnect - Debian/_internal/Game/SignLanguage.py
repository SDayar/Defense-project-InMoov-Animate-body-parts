##@author  Saifidine Dayar 
##@brief  Responsable de l'interprétation d'une phrase en language de signe.
##@date 15/04/2025
##@version 08/05/2025
##@file  SignLanguage.py
##@package L2L1.Game


##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter.messagebox import showerror
##@see threading est utilisé pour gérer les threads.
import threading
##@see time est utilisé pour garder une trace du temps d'éxécution.
import time
##@see Enumerations.EnumLanguage est utilisé pour définir les mouvements de chaque doigt.
from Enumerations.EnumLanguage import EnumLanguage as EL
##@see Movement est utilisé pour génerer les mouvements des doigts.
from Movement import Movement 
##@see os est utilisé pour gérer les fichiers.
import os

class SignLanguage: 
    ##@class SignLanguage
    ##@brief Responsable de l'interprétation d'une phrase en language de signe.
    ##@details Cette classe est responsable de l'interprétation d'une phrase en language de signe. Elle permet de convertir une phrase en une liste de mouvements à effectuer par les doigts. Elle utilise la classe Movement pour effectuer les mouvements et la classe EnumLanguage pour définir les mouvements de chaque doigt.
    ##@see Movement
    ##@see EnumLanguage
    ##@package SignLanguage
    
    def __init__(self):
        """! Constrcuteur de la classe SignLanguage.
        @param None
        @return None"""
        ##@var _letters_to_movement Dictionnaire qui associe chaque lettre à un mouvement.
        ##@see EnumLanguage
        self._letters_to_movement ={"A":EL.A,"B":EL.B,"C":EL.C,"D":EL.D,"E":EL.E,"F":EL.F,"G":EL.G,"H":EL.H,"I":EL.I,"J":EL.J,"K":EL.K,"L":EL.L,"M":EL.M,"N":EL.N,"O":EL.O,"P":EL.P,"Q":EL.Q,"R":EL.R,"S":EL.S,"T":EL.T,"U":EL.U,"V":EL.V,"W":EL.W,"X":EL.X,"Y":EL.Y,"Z":EL.Z," ":EL.SPACE}
        ##@var TIME_OUT Temps d'attente maximal pour l'exécution d'un mouvement.
        global TIME_OUT
        TIME_OUT = 3 #Temps d'attente maximale fixé à 3 secondes
        ##@var __object_movement Objet de la classe Movement qui permet de créer les mouvements associés à chaque lettre.
        ##@see Movement
        self.__object_movement = Movement()
        ##@var __sentence Phrase à interpréter en langage des signes.
        self.__sentence = None
        ##@var __executed_commands_file Fichier qui contient les mouvements exécutés.
        self.__executed_commands_file = "../commands/executed_commands.txt"
    def mimic_language(self,sentence):
        """! Interprète un mot en language des signes.
        @param String | None. Le mot à interpréter.
        @return None."""
        self.__sentence = sentence
        if len(self.__sentence) > 0:
            list_letters = []
            for car in self.__sentence:
                list_letters.append(car.capitalize())#On rend la lettre en majuscule
            thread_movement = threading.Thread(target=self.pass_letters_to_execute,args=(list_letters,))
            thread_movement.start()
        else :
            self.local_error("Aucun mot n' été saisie")
    def __begin_timer(self):
        """! Retourne le temps en seconde.
        @param None
        @return  Float. Le temps en seconde."""
        return time.time()
    def __end_timer(self):
        """! Retourne le temps en seconde. 
        @param None
        @return  Float. Le temps en seconde."""
        return time.time()
    def local_error(self, e):
        """! Génère les erreurs qui sont liès aux fonctionnalités de cette classe.
        @param String. Le message d'erreur à afficher dans l'alerte.
        @return None."""
        showerror("Erreur au niveau de SignLanguage", e)
    ##@deprecated  Première version de la méthode pass_letters_to_execute. Cette version est basée sur un comportement récursif. 
   
    def pass_letters_to_execute_deprecated(self,list_letters):
        """! Lance l'exécution du mouvement compter jusqu'au nombre.
        @param list. Liste des lettres à interpréter.
        @return None."""
        try :
            if len(list_letters) == 0:#Condition d'arrêt, si starting_number dépasse le nombre saisi
                return
            else : 
                   
                if os.path.exists(self.__executed_commands_file) :
                    #Si le fichier où se trouvent les mouvement executé existe, on le supprime
                    os.remove(self.__executed_commands_file)
                with open(self.__executed_commands_file, "w") as contents_within_commands:
                    pass #Un nouveau fichier est créer
                positions = self._letters_to_movement.get(list_letters[0])
                self.__object_movement.create_movement(positions.value)
                with open(self.__executed_commands_file, "r") as contents_within_commands:
                    #Initialisation du timer
                    timer = self.__begin_timer()
                    command_line = contents_within_commands.readline()
                    while len(command_line) == 0 and (self.__end_timer()-timer) < TIME_OUT:#Si aucune commande n'a été enrégistré dans la liste des mouvements exécutés, ou si le timer ne dépasse pas TIME_OUT
                        contents_within_commands.close() #Fermeture de la
                        with open(self.__executed_commands_file,"r") as contents_within_commands:
                            command_line = contents_within_commands.readline()
                    with open(self.__executed_commands_file,"r") as contents_within_commands:
                            command_line = contents_within_commands.readline()
                            if len(command_line) > 0:
                                contents_within_commands.close()
                                self.pass_letters_to_execute(list_letters[1:])#Appel récursif en retirant le premier élément
                            else:
                                contents_within_commands.close()
                                self.local_error("Mouvements interrompu. Le temps d'attente d'exécution du mouvement précédent a été dépassé !")
                                return
        except Exception as e :
            self.local_error("Une erreur est survenue lors de l'exécution du mouvement. Veuillez réessayer avec un autre nombre !")
    
    def pass_letters_to_execute(self, list_letters):
        """! Envoie la liste des positions au système de gestions de mouvements.
            Il s'agit de la version améliorée de la fonction pass_letters_to_execute_v.
        @param list. Liste des lettres à interpréter.
        @return None."""
        list_positions= []
        for car in list_letters :
            if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ " :
                #Si le caractère est reconnu 
                list_positions.append(self._letters_to_movement[car].value)
            else:
                #Sinon on rien ne bouge
                list_positions.append([-1,-1,-1,-1,-1,-1])
        Movement.create_movement(list_positions)
