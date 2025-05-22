##@authors
# - Saifidine Dayar
# - Jacques 
##@brief  Implémente la fonctionnalité "Compter en binaire".
##@date 15/04/2025
##@version 08/05/2025
##@file  GamePPC.py
##@package L2L1.Game


##@see time 
import time
##@see Movement
from Movement import Movement as mv
##@see Enumerations.EnumMovement
from Enumerations.EnumMovement import EnumMovement
##@see random
import random 
class GamePPC :
    ##@class GamePPC
    ##@brief Responsable d'implémenter la fonctionnalité pierre - papier- ciseau.
    ##@package GamePPC
    def __init__(self):
        """! Constructeur de classe GamePPC. 
        @param None
        @return None"""
        pass
    def rockPaperScissors(self):
            """! Génère un mouvement pierre, papier ou ciseau de manière aléatoire.
            @param None
            @return None"""
            val = random.randint(0,2)
            if val == 0:  # la valeur 0 pour faire pierre
                mv.create_movement(EnumMovement.ROCK)
            elif val == 1:
                mv.create_movement(EnumMovement.PAPER)
            elif val == 2:
                mv.create_movement(EnumMovement.SCISSOR)

    def rock(self):
            """! Génère un mouvement "pierre".
             @param None 
              @return None """
            mv.create_movement(EnumMovement.ROCK)
    def paper(self):
            """! Génère un mouvement "papier".
             @param None
              @return None """
            mv.create_movement(EnumMovement.PAPER)
    def scissor(self):
            """! Génère un mouvement "cisea". 
            @param None 
            @return None"""
            mv.create_movement(EnumMovement.SCISSOR)   

    ##@deprecated Version dépréciée de la méthode __count_number_to_execute
    ##@see CountBinary
    def number_Binary_deprecated(self, val):
            """! Exécute une suite de mouvements à partir d'un entier indiqué en paramètre.
            @param int. 
            @return None"""
            # self.__stateFinger = enumState.ACTIVE  # REST -> Jeu  en activité
            if val >= 0 and val <= 31:
                # Conversion en binaire sur 5 bits avec remplissage à gauche
                binaire = format(val, '05b')

                # Création d'une liste en remplaçant les bits 1 par 90
                listeBits = [90 if bit == '1' else int(bit) for bit in binaire]

                # La position
                mv.create_movement(listeBits)
    ##@deprecated Version dépréciée de la méthode __count_number_to_execute_deprecated
    ##@see CountBinary
    def count_Binary_deprecated(self):
            """! Exécute une suite de mouvements en commençant par 0.
            @param None
            @return None"""
            # self.__stateFinger = enumState.ACTIVE  # REST -> Jeu  en activité
            for i in range(0, 31):
                self.number_Binary(i)
                time.sleep(1)  # voir la l'unité de cette fonction


        # faire une fonction pour la gestion d'erreur en cas d'une valeur val entrée qui n'est pas entre 0 et 31
        