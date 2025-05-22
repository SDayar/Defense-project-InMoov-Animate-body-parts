## @file Movement.py
## @authors 
# - Dayar  
# - Shérine
## @date 26/03/2025
##@brief Gère la création et l’envoi de mouvements à la main robotique.
## @class Movement
# @details La classe Movement hérite de RightHand. Elle permet de créer un mouvement à envoyer à la carte Arduino, en vérifiant la validité des positions. Elle interagit également avec l’interface graphique pour afficher les erreurs.
# @details Permet de créer un mouvement avant de le transférer au système de traitement du mouvement.
##@package L2L1

##@see RightHand
from RightHand import RightHand 
##@see tkinter.messagebox
from tkinter.messagebox import showerror 
##@see PrepareArduinoBoard
from PrepareArduinoBoard import PrepareArduinoBoard



class Movement(RightHand):
    ##@class Movement
    ##@brief Cette classe sert à créer un mouvement.
    ##@package Movement
    def __init__(self):
        """!
        @brief Constructeur de la classe Movement. Initialise la main droite via le constructeur parent.
        @details Ce constructeur appelle le constructeur de la classe parente RightHand. Il prépare la main pour l'exécution des mouvements.
        @return None
        @param None"""
        super().__init__()

    
    def local_error(self,e):
        """!
        @brief Affiche une boîte d’erreur liée aux mouvements.
        @param String. Le message d’erreur à afficher.
        @return None"""
    
        #@details Cette méthode est utilisée pour afficher une erreur à l’utilisateur via une boîte de dialogue. Elle est appelée dans le cas où un mouvement n'est pas correctement créé ou transmis.
           
        showerror("Erreur au niveau de Movement ", e)

    ##@deprecated 
    def create_movement_deprecated(self,positions):
        """! 
        @brief Crée un mouvement. Ancienne version de la méthode create_movement(cls,positions)
        @return None
        @param list. Liste de 6 positions (ou liste de listes pour des mouvements composés)."""
        
        if positions == [] or positions == None:
            self.local_error("Aucun mouvement n'a été créé.")
            return
        elif not isinstance(positions, list):
            self.local_error("Le mouvement doit être une structurée à partir d'une liste.")
            return
        elif len(positions) != 6:
            self.local_error("Le mouvement doit contenir 6 positions. Mais "+str(len(positions))+" ont été renseignés. ")
            return
        super().personalized_movement(positions)

    
    @classmethod
    def create_movement(cls, positions):
        """!
        @brief Crée et envoie un mouvement à la main robotique.
        @param list. Liste de 6 positions (ou liste de listes pour des mouvements composés).
        @details Cette méthode de classe vérifie que la carte Arduino est connectée avant d’envoyer les mouvements. Elle accepte soit une liste de 6 entiers (mouvement simple), soit une liste de plusieurs listes de 6 entiers (mouvement complexe ou séquence). Elle lève des erreurs en cas d’incohérences. Si la carte Arduino n'est pas connectée, un message d'erreur est affiché.
        @return None"""
        # Vérifie si la carte Arduino est connectée
        if PrepareArduinoBoard.connected :
            
            # Vérifie si la liste de positions est vide ou mal définie
            if positions == [] or positions == None:
                Movement().local_error("Aucun mouvement n'a été créé.")
                return
            
            # Vérifie que les positions sont bien sous forme de liste
            elif not isinstance(positions, list):
                Movement().local_error("Le mouvement doit être une liste.")
                return
            
            # Vérifie si les positions sont une liste de listes (mouvement composé)
            elif isinstance(positions[0], list):
                # Vérifie que chaque sous-liste contient 6 positions
                if not all(len(pos) == 6 for pos in positions):
                    Movement().local_error("Chaque sous-liste doit contenir 6 positions.")
                    return
            
            # Si ce n'est pas un mouvement composé, vérifie que la liste contient bien 6 positions
            elif len(positions) != 6:
                Movement.local_error("La sous-liste doit être composée de 6 positions exactement")
            
            # Appelle la méthode de la classe parente pour exécuter le mouvement
            super().personalized_movement(positions)
        else :
            # Affiche une erreur si la carte Arduino n'est pas connectée
            PrepareArduinoBoard.error("Assurez-vous que la carte Arduino soit connectée.")
