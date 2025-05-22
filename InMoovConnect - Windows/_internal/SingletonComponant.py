##@authors
# - Shérine 
#- Saifidine Dayar
##@date 02/04/2025
##@brief Classe qui gère le singleton de la main. Permet de créer un seul objet et par ce fait d’assurer qu’il n’y aura qu’une seule main constituée de 5 doigts et d’un poignet.
##@version 08/05/2025
##@file SingletonComponant.py
##@package L2L1

##@see ServoMediator est utilisé pour servir de pont d'échanges de communications entre le programme en Arduino et l'interface de traitements de signaux en python. 
from ServoMediator import ServoMediator as SM
class SingletonComponant:
    ##@class SingletonComponant
    ##@brief Classe qui gère le singleton de la main. Permet de créer un seul objet et par ce fait d’assurer qu’il n’y aura qu’une seule main constituée de 5 doigts et d’un poignet.
    ##@var __instance: Contient l'instance de la classe SingletonComponant.
    ##@package SingletonComponant
    __instance = None
    def __init__(self):
        """! Constructeur de la classe SingletonComponant.
             Il s'assure qu'il n'y a qu'une seule instance de la classe SingletonComponant.
             @param None
        @return None"""
        if SingletonComponant.__instance is not None:
                SM.__stop_movement("Erreur au niveau de SingletonComponent. Utilisez getInstance() pour accéder à cette classe. ")
                exit
        
        self.__object_mediator = SM()  
        SingletonComponant.__instance = self

    @classmethod
    def get_instance(cls):
        """! Retourne l'instance du singleton.
        @details Il s'agit d'une méthode de classe qui permet de créer une instance de la classe SingletonComponant si elle n'existe pas déjà.
        @param None
        @return SingletonComponant"""
        
        if cls.__instance is None:
            cls.__instance = SingletonComponant()
        return cls.__instance
   
    @classmethod
    def singleton_send_current_positions(cls,current_positions):
        """! Envoie les nouvelles positions vers le RightHand qui est la seule classe fille de cls.
        @param list. Liste des positions à envoyer.
        @details Cette méthode est statique.
        @return None."""
        cls.__subclasses__()[0].set_actual_position(current_positions[0])
    def send_new_positions_to_execute(self,new_positions):
        """! Construit un dictionnaire avec les positions reçues pour les exécuter.
        @param list. Liste des positions à envoyer.
        @return None.""" 
        self.__object_mediator.continue_movement({"positions":new_positions})
        
    def __str__(self):
        """! Retourne le nom de la classe.
        @param None
         @return String."""
        return "Main"
    


    





    