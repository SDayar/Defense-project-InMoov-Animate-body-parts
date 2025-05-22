## @author  Saifidine Dayar 
## @brief Ce fichier contient la classe ENUM_STATUS_FRAME qui est une énumération qui permet de définir deux champs qui vont déterminer le status de chaque frame de l'application.
## @date  03/03/2025
## @version 08/05/2025
## @file  ENUM_STATUS_FRAME.py


## @see enum
import enum
##@package L2L1.Enumerations
class ENUM_STATUS_FRAME(enum.Enum):
    ##@class ENUM_STATUS_FRAME
    ##@brief Cette classe est une énumération qui permet de définir deux champs qui vont déterminer le status de chaque frame de l'application.
    ##@package ENUM_STATUS_FRAME
    ##@see Mediator
    
    ##@var RUNNING: Champ qui permet de définir le status d'une frame qui est en cours d'exécution.
    RUNNING = True

    ##@var NOT_RUNNING: Champ qui permet de définir le status d'une frame qui n'est pas en cours d'exécution
    NOT_RUNNING = False
