## @file EnumBinary.py
#  @brief Ce fichier définit l'énumération "EnumBinary" qui contient des configurations de mouvement pour la main.
#         Chaque élément de l'énumération correspond à une combinaison spécifique de positions des doigts
#         et du poignet, utilisées pour représenter les nombres en binaire, allant de 0 à 31.
#  @author Shérine
#  @date 02/04/2025
#  @class EnumBinary

# @package L2L1.Enumerations
from enum import Enum
from Enumerations.EnumMovement import EnumMovement



class EnumBinary(Enum):
    """! 
    @brief Enumération des mouvements de la main pour compter en binaire.

    L'énumération "EnumBinary" définit une série de positions pour les doigts et le poignet, utilisées pour
    représenter des nombres en binaire, allant de zéro (00000) à trente et un (11111). Chaque valeur de l'énumération
    correspond à un ensemble spécifique de degrés qui dépendent de l'état de chaque doigt et du poignet.

    Cette énumération est utilisée pour gérer les mouvements de la main dans des applications comme la reconnaissance
    gestuelle pour les nombres binaires."""
    ##@package EnumBinary
    
    ## @brief Zéro : main fermée.
    #  @details Représente le chiffre 0, la main est complètement fermée (CLOSEHAND).
    ZERO = EnumMovement.CLOSEHAND

    ## @brief Un : pouce ouvert.
    #  @details Représente le chiffre 1, le pouce est ouvert (OPENTHUMB).
    ONE = EnumMovement.OPENTHUMB

    ## @brief Deux : index ouvert.
    #  @details Représente le chiffre 2, l'index est ouvert (OPENINDEX).
    TWO = EnumMovement.OPENINDEX

    ## @brief Trois : pouce et index ouverts.
    #  @details Représente le chiffre 3, le pouce et l'index sont ouverts (OPENTHUMB et OPENINDEX).
    THREE = [0, 0, 90, 90, 90, 0]

    ## @brief Quatre : majeur ouvert.
    #  @details Représente le chiffre 4, le majeur est ouvert (OPENMIDDLE).
    FOUR = EnumMovement.OPENMIDDLE

    ## @brief Cinq : pouce et majeur sont ouvets.
    #  @details Représente le chiffre 5, pouce et majeur sont à 90°, autres doigts ouverts.
    FIVE = [0, 90, 0, 90, 90, 0]

    ## @brief Six : pouce et index ouverts, majeur et annulaire à 90°.
    #  @details Représente le chiffre 6, pouce et index ouverts, majeur et annulaire à 90°.
    SIX = [90, 0, 0, 90, 90, 0]

    ## @brief Sept : pouce, index et majeur ouverts.
    SEVEN = [0, 0, 0, 90, 90, 0]

    ## @brief Huit : annulaire ouvert.
    #  @details Représente le chiffre 8, l'annulaire est ouvert (OPENRING).
    EIGHT = EnumMovement.OPENRING

    ## @brief Neuf : pouce et annulaire ouverts.
    #  @details Représente le chiffre 9, pouce et annulaire sont ouverts (OPENTHUMB et OPENRING).
    NINE = [0, 90, 90, 0, 90, 0]

    ## @brief Dix : index et annulaire ouverts.
    #  @details Représente le chiffre 10, index et annulaire sont ouverts.
    TEN = [90, 0, 90, 0, 90, 0]

    ## @brief Onze : pouce, index et annulaire ouverts.
    ELEVEN = [0, 0, 90, 0, 90, 0]

    ## @brief Douze : majeur et annulaire ouverts.
    TWELVE = [90, 90, 0, 0, 90, 0]

    ## @brief Treize : pouce, majeur et annulaire ouverts.
    THIRTEN = [0, 90, 0, 0, 90, 0]

    ## @brief Quatorze : index, majeur et annulaire ouverts.
    FOURTEN = [90, 0, 0, 0, 90, 0]

    ## @brief Quinze : pouce, index, majeur et annulaire ouverts.
    FIFTEN = [0, 0, 0, 0, 90, 0]

    ## @brief Seize : auriculaire ouvert.
    SIXTEN = [90, 90, 90, 90, 0, 0]

    ## @brief Dix-sept : pouce et auriculaire ouverts.
    SEVENTEN = [0, 90, 90, 90, 0, 0]

    ## @brief Dix-huit : index et auriculaire ouverts.
    EIGHTEN = [90, 0, 90, 90, 0, 0]

    ## @brief Dix-neuf : pouce, index et auriculaire ouverts.
    NINETEN = [0, 0, 90, 90, 0, 0]

    ## @brief Vingt : majeur et auriculaire ouverts.
    TWENTY = [90, 90, 0, 90, 0, 0]
    ## @brief Vingt et un : pouce, majeur et auriculaire ouverts.
    TWENTY_ONE = [0, 90, 0, 90, 0, 0]
    ## @brief Vingt-deux : index, majeur et auriculaire ouverts.
    TWENTY_TWO = [90, 0, 0, 90, 0, 0]

    ## @brief Vingt-trois : pouce, index, majeur et auriculaire ouverts.
    TWENTY_THREE = [0, 0, 0, 90, 0, 0]

    ## @brief Vingt-quatre : annulaire et auriculaire ouverts.
    TWENTY_FOUR = [90, 90, 90, 0, 0, 0]

    ## @brief Vingt-cinq : pouce, annulaire et auriculaire ouverts.
    TWENTY_FIVE = [0, 90, 90, 0, 0, 0]

    ## @brief Vingt-six : index, annulaire et auriculaire ouverts.
    TWENTY_SIX = [90, 0, 90, 0, 0, 0]

    ## @brief Vingt-sept : pouce, index, annulaire et auriculaire ouverts.
    TWENTY_SEVEN = [0, 0, 90, 0, 0, 0]

    ## @brief Vingt-huit : majeur, annulaire et auriculaire ouverts.
    TWENTY_EIGHT = [90, 90, 0, 0, 0, 0]

    ## @brief Vingt-neuf : pouce, majeur, annulaire et auriculaire ouverts.
    TWENTY_NINE = [0, 90, 0, 0, 0, 0]

    ## @brief Trente : index, majeur, annulaire et auriculaire ouverts.
    THIRTY = [90, 0, 0, 0, 0, 0]

    ## @brief Trente et un : main ouverte.
    #  @details Représente le chiffre 31, tous les doigts sont ouverts (OPENHAND).
    THIRTY_ONE = EnumMovement.OPENHAND
