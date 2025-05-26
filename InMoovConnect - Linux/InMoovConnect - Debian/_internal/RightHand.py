##@authors 
# - Shérine Meziane
# - Saifidine Dayar
##@file RightHand.py
##@brief Il s'agit de la main. Elle est composée de 5 doigts et d'un poignet.
##@details La main droite est composée de 5 doigts et d'un poignet.
##@date 14/04/2025
##@version 08/05/2025
##@package L2L1

##@see Finger est utilisé pour créer les doigts de la main droite.
from Finger import Finger
##@see Wrist est utilisé pour créer le poignet de la main droite.
from Wrist import Wrist
##@see SingletonComponant est utilisé pour créer la main droite.
from SingletonComponant import SingletonComponant as SC
##@see tkinter.messagebox est utilisé pour afficher les messages d'erreurs.
from tkinter.messagebox import showerror
class RightHand(SC,Finger,Wrist) :
    #Les membres de la main sont déclarés comme étant statiques car chaque mouvement concerne les mêmes doigts.
    ##@class RightHand
    ##@brief Il s'agit de la main. Elle est composée de 5 doigts et d'un poignet.
    ##@details Ces membres sont déclarés comme étant statiques car chaque mouvement concerne les mêmes doigts.
    ##@package RightHand
    
    ##@var __thumb 
    ##@brief Contient le pouce de la main.
    __thumb = None
    ##@var __index 
    ##@brief Contient l'index de la main.
    __index = None
    ##@var __middleFinger 
    ##@brief Contient le majeur de la main.
    __middleFinger = None
    ##@var __ringFinger 
    ##@brief Contient l'annulaire de la main.
    __ringFinger = None
    ##@var __pinky 
    ##@brief Contient l'auriculaire de la main.
    __pinky = None
    ##@var __wrist 
    ##@brief Contient le poignet de la main.
    __wrist = None
    
    def __init__(self):
        """! Constructeur de la classe RightHand.
        @param None
        @return None"""
        RightHand.__thumb=RightHand.__bases__[1]("thumb")
        RightHand.__index = RightHand.__bases__[1]("index")
        RightHand.__middleFinger=RightHand.__bases__[1]("middleFinger")
        RightHand.__ringFinger=RightHand.__bases__[1]("ringFinger")
        RightHand.__pinky=RightHand.__bases__[1]("pinky")
        RightHand.__wrist=RightHand.__bases__[2]("rightWrist")
    
    ##@deprecated Version dépréciée de la méthode de classe personalized_movement
    ##@see personalized_movement
    def personalized_movement_deprecated(self, listdegrees):
        """! Initialise le mouvement de la main.
        @param list. Liste des positions à envoyer.
        @return None."""
        try :
            self.__singleton.send_new_positions_to_execute([self._thumb.personalized_position(listdegrees[0]),self._index.personalized_position(listdegrees[1]),self._middleFinger.personalized_position(listdegrees[2]),self._ringFinger.personalized_position(listdegrees[3]),self._pinky.personalized_position(listdegrees[4]),listdegrees[5]])
        except Exception as e :
            self.local_error("Une erreur inconnue a surgi : "+e.__str__())
    def local_error(self,e):
        """! Affiche une alerte d'erreur liée à un mouvement personnalisé.
        @param String. Le message d'erreur à afficher.
        @return None."""
        showerror("Erreur au niveau de RighHand : ",e)
    
    @classmethod
    def personalized_movement(cls,list_degrees):
        """! Initialise le mouvement de la main. 
        @param list. Liste des positions à envoyer.
        @return None."""
        try :
            complex_list_of_movement = []
            if not isinstance(list_degrees[0],list):
                #S'il s'agit d'un mouvement 'simple', il est imbriqué dans une liste
                list_buffer = list_degrees
                list_degrees = []
                list_degrees.append(list_buffer)
            for tab_pos in list_degrees :
                complex_list_of_movement.append([cls.__thumb.personalized_position(tab_pos[0]),cls.__index.personalized_position(tab_pos[1]),cls.__middleFinger.personalized_position(tab_pos[2]),cls.__ringFinger.personalized_position(tab_pos[3]),cls.__pinky.personalized_position(tab_pos[4]),cls.__wrist.personalized_position(tab_pos[5])])
            cls.__bases__[0].get_instance().send_new_positions_to_execute(complex_list_of_movement)
                 
        except Exception as e :
            RightHand().local_error("Une erreur inconnue a surgi : "+str(e))
    
    @classmethod
    def set_actual_position(cls,current_positions):
        """! Met à jour la position actuelle de la main.
        @param list. Liste des positions actuelles à envoyer.
        @return None."""
        if  len(current_positions) == 6:
            #Si la position est différente de la position "INACTIF"
            cls.__thumb.set_current_position(current_positions[0])
            cls.__index.set_current_position(current_positions[1])
            cls.__middleFinger.set_current_position(current_positions[2])
            cls.__ringFinger.set_current_position(current_positions[3])
            cls.__pinky.set_current_position(current_positions[4])
            cls.__wrist.set_current_position(current_positions[5])
            
    
        



