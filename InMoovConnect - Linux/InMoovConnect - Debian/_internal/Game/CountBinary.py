##@author  Saifidine Dayar 
##@brief  Jeu "compter en binaire".
##@date 15/04/2025
##@version 08/05/2025
##@file  CountBinary.py
##@package L2L1.Game

##@see threading
import threading
##@see tkinter.messagebox
from tkinter.messagebox import showerror
##@see time
import time
##@see Movement
from Movement import Movement 
##@see Enumerations.EnumBinary
from Enumerations.EnumBinary import EnumBinary as EB
##@see os
import os
class CountBinary:
    ##@class CountBinary
    ##@brief Jeu "compter en binaire".
    ##@package CountBinary
    def __init__(self):
        """! Constructeur de la classe"""
        ##@var __object_movement Instance de la classe Movement. 
        self.__object_movement = Movement()
        ##@var __number_to_letter Dictionnaire qui comprend 32 couples (int, Mouvement)
        self.__number_to_letter = {0:EB.ZERO,1:EB.ONE, 2:EB.TWO,3:EB.THREE,4:EB.FOUR,5:EB.FIVE,6:EB.SIX,7:EB.SEVEN,8:EB.EIGHT,9:EB.NINE,10:EB.TEN,11:EB.ELEVEN,12:EB.TWELVE,13:EB.THIRTEN,14:EB.FOURTEN,15:EB.FIFTEN,16:EB.SIXTEN,17:EB.SEVENTEN,18:EB.EIGHTEN,19:EB.NINETEN,20:EB.TWENTY,21:EB.TWENTY_ONE,22:EB.TWENTY_TWO,23:EB.TWENTY_THREE,24:EB.TWENTY_FOUR,25:EB.TWENTY_FIVE,26:EB.TWENTY_SIX,27:EB.TWENTY_SEVEN,28:EB.TWENTY_EIGHT,29:EB.TWENTY_NINE,30:EB.THIRTY,31:EB.THIRTY_ONE}
        ##@var __number_in_str Nombre à interpréter en une séquences de mouvements 
        self.__number_in_str = None
        ##@var TIME_OUT Temps de traitement maximal.
        global TIME_OUT 
        TIME_OUT = 3
        ##@var __executed_commands_file Chemin vers le fichier qui enregistre les mouvement exécutés en temps réels.
        self.__executed_commands_file = "../commands/executed_commands"
    def count_to(self,number_in_str):
        """! Traite le numéro renvoyé dans la boite de dialogue.
        @param int. 
        @return None"""
        self.__number_in_str = number_in_str
        if self.__number_in_str is None :
            self.__object_movement.local_error("Aucune valeur n'a été saisie lors")
            return
        try :
            number = int(self.__number_in_str)
            if number >= 0 and number <= 31 :
                #A chaque fois qu'on exécute une position qui correspond à un nombre, on ouvre un nouveau thread.
                thread_movement = threading.Thread(target=self.__pass_number_to_execute,args=(number,))
                thread_movement.start()
                return 
            else:
                 self.__object_movement.local_error("Veuillez entrez un nombre valide (compris entre 0 et 31).")
        except Exception as e:
            self.__object_movement.local_error(e)
    def __begin_timer(self):
        """! Retourne le temps en seconde.
        @param None
        @retrun Float"""
        return time.time()
    def __end_timer(self):
        """! Retourne le temps en seconde.
        @param None
        @retrun Float"""
        return time.time()
    def local_error(self, e):
        """! Génère les erreurs qui sont liès aux fonctionnalités de cette frame. 
        @param String. Le message à afficher.
        @return None"""
        showerror("InMoovConnect", e)
    ##@deprecated Version dépréciée de la méthode pass_number_to_execute_deprecated. Elle consomme beaucoup d'espace mémoire avec la récursivité et augment excessivement le temps d'exécution de la commande.
    def __pass_number_to_execute_deprecated(self,number,starting_number=0):
        """ self -> None 
        Lance l'exécution du mouvement compter jusqu'au nombre"""
        try :
            if starting_number > number+1:#Condition d'arrêt, si starting_number dépasse le nombre saisi
                return
            else : 
                   
                if os.path.exists(self.__executed_commands_file) :
                    #Si le fichier où se trouvent les mouvement executé existe, on le supprime
                    os.remove(self.__executed_commands_file)
                   
                with open(self.__executed_commands_file, "w") as contents_within_commands:
                    pass #Un nouveau fichier est créer
                positions = self.__number_to_letter.get(starting_number)
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
                                self.__pass_number_to_execute_deprecated(number,starting_number+1)#Appel récursif jusqu'à ce que starting_number atteigne le nombre voulu
                            else:
                                contents_within_commands.close()
                                self.local_error("Mouvements interrompu. Le temps d'attente d'exécution du mouvement précédent a été dépassé !")
                                return
        except Exception as e :
            self.local_error("Une erreur est survenue lors de l'exécution du mouvement. Veuillez réessayer avec un autre nombre!")
    

    def __pass_number_to_execute(self, number):
        """! Traite la demande en créeant une liste de mouvements jusqu'au nombre indiqué et transfert le résultat.
        @param int. 
        @return None"""
        list_positions = []
        if isinstance(number,int):
            for i in range(0,number+1):
                list_positions.append(self.__number_to_letter[i].value)
            Movement.create_movement(list_positions)


   