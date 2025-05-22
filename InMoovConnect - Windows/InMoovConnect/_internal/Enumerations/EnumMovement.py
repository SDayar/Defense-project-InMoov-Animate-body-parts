## @file EnumMovement.py
#  @brief Ce fichier définit les configurations de mouvements standards des doigts et du poignet.
#         Chaque configuration correspond à une posture particulière de la main utilisée en langue des signes ou dans des gestes spécifiques.
#  @author Shérine
#  @date 02/04/2025
# @class EnumMovement
##package L2L1.Enumerations
from enum import Enum


#  @brief Contient des configurations de mouvement pour la main.
#
#  Chaque attribut est une liste représentant les degrés d’articulation pour :
#  [pouce, index, majeur, annulaire, auriculaire, poignet].
#  Les degrés sont exprimés en angles d’ouverture/fermeture.

class EnumMovement:
    ##package EnumMovement
    ## @brief Main complètement ouverte.
    OPENHAND = [0, 0, 0, 0, 0, -1]

    ## @brief Main complètement fermée.
    #  @details Tous les doigts sont fermés, le poignet reste immobile.
    CLOSEHAND = [90, 90, 90, 90, 90, -1]

    ## @brief Pouce ouvert uniquement.
    OPENTHUMB = [0, 90, 90, 90, 90, -1]

    ## @brief Pouce fermé uniquement.
    CLOSETHUMB = [90, 0, 0, 0, 0, -1]

    ## @brief Index ouvert uniquement.
    OPENINDEX = [90, 0, 90, 90, 90, -1]

    ## @brief Index fermé uniquement.
    CLOSEINDEX = [0, 90, 0, 0, 0, -1]

    ## @brief Majeur ouvert uniquement.
    OPENMIDDLE = [90, 90, 0, 90, 90, -1]

    ## @brief Majeur fermé uniquement.
    CLOSEMIDDLE = [0, 0, 90, 0, 0, -1]

    ## @brief Annulaire ouvert uniquement.
    OPENRING = [90, 90, 90, 0, 90, -1]

    ## @brief Annulaire fermé uniquement.
    CLOSERING = [0, 0, 0, 90, 0, -1]

    ## @brief Auriculaire ouvert uniquement.
    OPENPINKY = [90, 90, 90, 90, 0, -1]

    ## @brief Auriculaire fermé uniquement.
    CLOSEPINKY = [0, 0, 0, 0, 90, -1]

    ## @brief Geste des ciseaux : index et majeur ouverts, autres doigts fermés.
    SCISSOR = [90, 0, 0, 90, 90, -1]

    ## @brief Geste "rock" : tous les doigts fermés.
    ROCK = [90, 90, 90, 90, 90, -1]

    ## @brief Geste "papier" : tous les doigts ouverts.
    PAPER = [0, 0, 0, 0, 0, -1]

    # CATCH = [90, 90, 90, 90, 90]  # configuration potentielle avec capteurs de pression

    ## @brief Commande d’arrêt, équivalente à OPENHAND.
    STOP = OPENHAND
