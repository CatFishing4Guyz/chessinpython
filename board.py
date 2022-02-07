from whitemoves import whitemoves
from whitevariables import whitevariables
from blackmoves import blackmoves
from blackvariables import blackvariables

def board():
    print("1 |                 |")
    print("2 |                 |")
    print("3 |                 |")
    print("4 |                 |")
    print("5 |                 |")
    print("6 |                 |")
    print("7 |                 |")
    print("8 |                 |")
    print("    A B C D E F G H  ")

    whiteboardpos = [firstpawnpos, secondpawnpos, thirdpawnpos, fourthpawnpos, fifthpawnpos, sixthpawnpos, seventhpawnpos, eighthpawnpos,
             westrookpos, eastrookpos, westknightpos, eastknightpos, westbishoppos, eastbishoppos,
             queenpos, kingpos]

    black = [firstpawnpos, secondpawnpos, thirdpawnpos, fourthpawnpos, fifthpawnpos, sixthpawnpos, seventhpawnpos, eighthpawnpos,
             westrookpos, eastrookpos, westknightpos, eastknightpos, westbishoppos, eastbishoppos,
             queenpos, kingpos]
whitevariables()
