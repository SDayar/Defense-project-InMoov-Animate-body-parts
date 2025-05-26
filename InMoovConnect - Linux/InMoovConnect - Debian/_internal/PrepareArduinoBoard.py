##@author  Saifidine Dayar
##@brief  Etablit la connexion avec la carte arduino.
##@date  07/04/2025
##@version 08/05/2025
##@file  PrepareArduinoBoard.py
##@package L2L1

##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
import serial.tools.list_ports as s
##@see serial est utilisé pour établir la connexion avec la carte arduino.
import serial as serial
##@see tkinter est utilisé pour afficher les messages d'erreurs.
import tkinter.messagebox as TclError

class PrepareArduinoBoard:
    ##@class PrepareArduinoBoard
    ##@brief Etablit la connexion avec la carte arduino.
    ##@details Cette classe permet d'établir la connexion avec la carte arduino. Elle permet de vérifier si la carte est connectée ou non. Elle permet également de préparer la carte à recevoir des commandes.
    ##@see tkinter.messagebox
    ##@see serial.tools.list_ports
    ##@see serial
    ##@package PrepareArduinoBoard
    ##@var arduino: Contient la reférence à la carte arduino.
    arduino = None
    ##@var available_port: Contient le port dont la carte arduino est connectée.
    available_port = None 
    ##@var connected: Contient un booléen qui indique si la carte est connectée ou non.
    connected = False
    ##@var info: Contient un message qui indique si la carte est connectée ou non.
    info = "Carte non connectée"
    def __init__(self):
        """! Constructeur de la classe PrepareArduinoBoard.
        @param None
        @return None"""
        ##@var __ports 
        ##@bref Contient une liste des ports en activité ou disponible en temps réel.
        self.__ports = s.comports()
        ##@var TIME_OUT
        ##@bref Contient le temps d'attente maximale pour recevoir une réponse depuis la carte.
        global TIME_OUT 
        TIME_OUT = 2

    def set_arduino_board_ready(self):
            """! 
            Prépare la carte Arduino à recevoir des commandes.
            @param None
            @return None"""
            
            try:
                ##@var __ports: Contient la liste des ports disponibles sur l'ordinateur.
                self.__ports = s.comports()
                if len(self.__ports) > 0:

                    for port in self.__ports:
                        
                        if PrepareArduinoBoard.arduino == None:
                            PrepareArduinoBoard.arduino = serial.Serial(port.device,baudrate=9600,timeout=1)
                        if port.serial_number =="7593231373835171A1C1" and PrepareArduinoBoard.arduino.is_open: #Envoyé le message au numéro de série de la carte
                            PrepareArduinoBoard.available_port = port
                            PrepareArduinoBoard.connected= True#On sort de la boucle
                            PrepareArduinoBoard.info = "Carte connectée."
                            break
                        else:
                            PrepareArduinoBoard.available_port = port
                            PrepareArduinoBoard.connected= False#On sort de la boucle
                            PrepareArduinoBoard.arduino = None
                            PrepareArduinoBoard.info = "Carte non connectée."
                            break
                   
                else: 
                    PrepareArduinoBoard.available_port = None
                    PrepareArduinoBoard.connected= False
                    PrepareArduinoBoard.info = "Carte non connectée."
                    PrepareArduinoBoard.arduino = None
                    
                        

            except Exception as e :
                #Sinon on affiche l'erreur
                self.__warning(str(e))
                    
    def __warning(self,e):
        """! 
        Emet un avertissement sans pour autant stoper la création d'un mouvement.
        @param String. Le message d'erreur à afficher dans l'alerte.
        @return None."""
        TclError.showwarning("Connexion avec la carte Arduino",e)
    @staticmethod
    def error(e):
        """! 
        Affiche une erreur de type, connexion impossible.
        @details Cette méthode est statique et ne doit pas être instanciée.
        @param String. Le message d'erreur à afficher dans l'alerte.
        @return None."""
        TclError.showerror("Connexion avec la carte Arduino",e)
    @classmethod
    def get_connected_arduino(cls):
        """! 
        Renvoie la reférence à la carte Arduino.
        @param None
        @return None
        @details Il s'agit d'une méthode de classe et ne doit pas être instanciée."""
        return cls.arduino
    @classmethod
    def get_connected_port(cls):
        """! 
        Renvoie le port de connexion avec la carte Arduino.
        @param None
        @return None
        @details Il s'agit d'une méthode de classe et ne doit pas être instanciée."""
        return cls.available_port
    
