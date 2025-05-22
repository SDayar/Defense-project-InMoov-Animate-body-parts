##@author Saifidne Dayar
##@file ServoMediator.py
##@brief Mediator entre ServoMotor et le programme de gestion des mouvements en python
##@version 08/05/2025
##@date 22/03/2025
##@package L2L1



##@see time est utilisé pour gérer le temps d'attente entre l'envoi de la commande et la réception de la réponse.
import time 
##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
import tkinter.messagebox as TclError
##@see threading est utilisé pour gérer les threads de connexion avec la carte arduino.
import threading as t
##@see json est utilisé pour encoder et décoder les données envoyées à la carte arduino.
import json
##@see InfoBox est utilisé pour afficher les informations sur le mouvement effectué par chaque doigt.
from InfoBox import InfoBox
##@see PrepareArduinoBoard est utilisé pour vérifierla connexion avec la carte arduino.
from PrepareArduinoBoard import PrepareArduinoBoard
class ServoMediator :
    ##@class ServoMediator
    ##@brief Mediator entre ServoMotor et le programme de gestion des mouvements en python.
    ##@details Cette classe permet de gérer les mouvements des doigts. Elle permet de créer un mouvement, de l'exécuter et de vérifier si le mouvement a été exécuté ou non. Elle permet également de gérer les erreurs lors de l'exécution
    ##@package ServoMediator
    def __init__(self):
        """! Constructeur de la classe ServoMediator.
        @param None
        @return None"""
        ##@var __send_commands_file
        ##@bref Contient le nom du fichier dans lequel les commandes à envoyer à la carte arduino sont stockées.
        self.__send_commands_file = "send_command.txt"
        ##@var __executed_commands_file
        ##@bref Contient le nom du fichier dans lequel les commandes exécutées par la carte arduino sont stockées.
        self.__executed_commands_file= "executed_command.txt"
        ##@var TIME_OUT
        ##@bref Contient le temps d'attente entre l'envoi de la commande et la réception de la réponse.
        global TIME_OUT
        TIME_OUT = 5
        ##@var _copy_state
        ##@bref Contient l'état de la demande d'éxécutionn du mouvement.
        self._copy_state = ""
        ##@var _copy_positions
        ##@bref Contient la liste des positions exécutées par la carte arduino.
        self._copy_positions = ""
    def __create_Movement_Via_Threads(self,movement):
        """! Crée un thread qui va exécuter la connexion avec la carte Arduino.
        @param dict. Dictionnaire contenant les mouvements à exécuter.
        @return None."""
        ##@see Threading
        if(isinstance(movement, dict)):
            thread = t.Thread(target=self.__connexion_To_Arduino,args=(movement,))
            thread.start()
        else:
            self.__stop_movement("L'argument passé lors de la création du thread de connexion n'est pas un dictionnaire de mouvement.")
        

    def __write_command(self,movement,file):
        """! Enregistre une commande dans un fichier.
        @param dict. Dictionnaire contenant les mouvements
        @param String. Nom du fichier dans lequel la commande sera enregistrée."""
        with open("./commands/"+file,"a") as stream:
            stream.write((json.dumps(movement)+'\n'))
            stream.close()

    def __begin_timer(self):
        """! Retourne le temps en seconde.
        @return Float. Le temps en seconde."""
        return time.time()
    def __end_timer(self):
        """! Retourne le temps en seconde.
        @return Float. Le temps en seconde."""
        return time.time() 
    def __connexion_To_Arduino(self,movement):
        """! Se connecte avec la carte Arduino.
        @param dict. Dictionnaire contenant les mouvements à exécuter.
        @return None."""
        ##@see PrepareArduinoBoard
        ##@see SingletonComponant
        ##@see json
        if PrepareArduinoBoard.connected:
            from SingletonComponant import SingletonComponant
            try:
                #Attend que la carte soit prête avant de lui envoyer la commande en écrivant dans un fichier.
                self.__write_command(movement, self.__send_commands_file)
                #Envoyer le message au numéro de série de la carte.
                reponse=""#Contiendra la réponse reçu depuis la board sous-format Json.
                info ="****************** Bilan du dernier mouvement ***********************\n"#Contiendra un amas d'informations reçus depuis la board.
                arduino_uno = PrepareArduinoBoard.get_connected_arduino()
                set_timer = 0#Initialisation du timer
                #On envoie la commande sous format Json
                for position in movement["positions"]:
                    
                    movement_in_json = (json.dumps({"positions":[position]})+'\n').encode("utf-8")
                    set_timer = self.__begin_timer()#Permet d'initialier le timer et d'interrompre le mouvement au cas où le mouvement ne sera pas réalisé.
                    arduino_uno.write(movement_in_json)
                    while (self.__end_timer() - set_timer) < TIME_OUT:  
                            try:
                                line = (arduino_uno.read_until(b'}').decode("utf-8","ignore")).strip()
                            except :
                                #Si un caractère n'a pas pû être décodé avec l'encodage utf-8, on utilise l'encodage ascii.
                                line = (arduino_uno.read_until(b'}').decode("ascii","ignore")).strip()
                            if len(line) > 0:  # Vérifie si la ligne n'est pas vide.
                                try :
                                    reponse = json.loads(line)  # Décode uniquement si la ligne est non vide.
                                    if "state" in reponse and reponse["state"] != None:
                                        if reponse["state"] in ["0\n", "-1\n"]:
                                            if "positions" in reponse and reponse["positions"] != None:
                                                self._copy_positions = reponse["positions"]
                                                self._copy_state = reponse["state"]
                                                set_timer = - (TIME_OUT) #Force la sortie
                                    if "info" in reponse and reponse["info"] != None and set_timer != - (TIME_OUT) and position == movement["positions"][len(movement["positions"])-1]:
                                        #On ne récupère que les informations du dernier mouvement et que si le timer n'a pas été dépassé.
                                        info+="-------> INFO : "+reponse["info"]+"\n"
                                except json.JSONDecodeError as e:
                                    info+="--------> WARNING : réponse non reconnue.\n"
                                    
                    #On renvoie la dernière liste de positions qui a été exécutée. 
                    SingletonComponant.singleton_send_current_positions([position])
                if self._copy_state == "0\n" :
                    #Si un signal de "sucess" a été reçu, la position est enrégistrée et les positions sont mises à jour.
                    self.__write_command({"positions": self._copy_positions},self.__executed_commands_file)
                    info+="--------> SUCCESS : Tâche exécutée avec succès.\n"
                    info+="--------> Positions actuelles : "+str(self._copy_positions)+"\n"
                elif self._copy_state =="-1\n":
                    info+="--------> ERROR: Tâche non exécutée.\n"
                elif set_timer == - (TIME_OUT) :
                    info+="--------> ERROR: Tâche non exécutée. Le temps d'attente d'exécution du mouvement a été dépassé !\n"
                    
                self.__show_progress(info) #Après que toutes les opérations soient effectuées, on affiche les résultats.
                
            except Exception as e :
                #Sinon on affiche l'erreur
                self.__stop_movement(e)
        else :
            PrepareArduinoBoard.error("La carte a été déconnectée. Assurez-vous que la carte soit connectée.")
    def continue_movement(self,movement):
        """! Valide la demande de création de mouvement.
        @param dict. Dictionnaire contenant les mouvements.
        @return None."""
        if(isinstance(movement,dict)):
            if(isinstance(movement["positions"],list)):
            #Si les positions sont bien représentées par une liste 
                self.__create_Movement_Via_Threads(movement)
            else :
                #Sinon on lance une erreur
                self.__stop_movement("Erreur de connexion. Les positions ne sont pas contenues dans une liste.")
        else :
            #Sinon on lance une erreur
            self.__stop_movement("Erreur de connexion. Les données reçues n'est pas un dictionnaire.")        
    def __stop_movement(self,e):
        """! Ne valide pas la demande de création de mouvement.
        @param String.  Message d'erreur à afficher.
        @return None."""
        TclError.showinfo("Erreur de connexion",e)

    def __show_progress(self,e):
        """! Montre la progression de l'exécution du mouvement.
        @param String.  Message d'erreur à afficher.
        @return None."""
        try :
            InfoBox.info = e #On met à jour les résultats
            InfoBox.display()
        except Exception as error :
            TclError.showwarning(error)
        
   
        
