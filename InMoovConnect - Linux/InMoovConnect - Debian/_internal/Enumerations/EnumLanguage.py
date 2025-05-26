## @file EnumLanguage.py
#  @brief Ce fichier définit l'énumération "EnumLanguage" représentant les mouvements de la main pour chaque lettre de l'alphabet en langue des signes.
#         Chaque valeur correspond à une configuration spécifique des cinq doigts et du poignet, exprimée en degrés.
#  @author Shérine
#  @date 02/04/2025
## @class EnumLanguage
##package L2L1.Enumerations
from enum import Enum
from Enumerations.EnumMovement import EnumMovement



class EnumLanguage(Enum):
     
    """!
        @brief Énumération des mouvements associés aux lettres de l'alphabet en langue des signes.

        Chaque membre de l'énumération représente une lettre (A-Z), avec une configuration des doigts et du poignet
        spécifiée soit par une constante de "EnumMovement", soit par une liste de six entiers (un par articulation).
        Les valeurs "-1" indiquent une position par défaut ou non utilisée.
        @see EnumMovement"""
    ##@package EnumLanguage
    
    ## @brief Lettre A en langue des signes.
    ##  @details Le pouce est ouvert (OPENTHUMB), les autres doigts sont fermés.
    A = EnumMovement.OPENTHUMB

    ## @brief Lettre B en langue des signes.
    ##  @details Le pouce est fermé (CLOSETHUMB), les autres doigts sont ouverts.
    B = EnumMovement.CLOSETHUMB

    C = [0, 45, 45, 45, 45, -1]
    D = [45, 0, 45, 45, 45, -1]
    E = [10, 10, 10, 10, 10, -1]
    F = [0, 45, 0, 0, 0, -1]
    G = [0, 0, 90, 90, 90, -1]
    H = [0, 90, 0, 0, 90, -1]
    I = EnumMovement.OPENPINKY
    J = [0, 90, 90, 90, 0, -1]
    K = [0, 0, 45, 90, 90, -1]
    L = [0, 0, 90, 90, 90, -1]
    M = [90, 0, 0, 0, 0, 90]
    N = [90, 0, 0, 90, 90, -1]
    O = [45, 45, 45, 45, 45, -1]
    P = [90, 10, 20, 90, 90, -1]
    Q = [0, 0, 90, 90, 90, -1]
    R = [90, 0, 0, 90, 90, -1]
    S = EnumMovement.CLOSEHAND
    T = [0, 45, 0, 0, 0, -1]
    U = [90, 0, 0, 90, 90, -1]
    V = [90, 0, 0, 90, 90, -1]
    W = [90, 0, 0, 0, 90, -1]
    X = [90, 45, 45, 90, 90, -1]
    Y = [0, 90, 90, 90, 0, 90]
    Z = [90, 0, 90, 90, 90, 90]
    ## @brief Espace entre les mots.
    ##  @details Représente un temps d'arrêt pour délimiter chaque mot d'une phrase.
    SPACE = [-1, -1, -1, -1, -1, -1]
